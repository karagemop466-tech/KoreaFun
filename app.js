"use strict";

const STATUS_ORDER = ["confirmed", "established", "recheck", "watch", "unavailable"];
const STATUS_LABELS = {
  confirmed: "Confirmed",
  established: "Established",
  recheck: "Re-check",
  watch: "Watch",
  unavailable: "Unavailable"
};

const state = {
  data: null,
  query: "",
  city: "all",
  status: "all"
};

const elements = {
  filters: document.querySelector("#filters"),
  search: document.querySelector("#search-input"),
  city: document.querySelector("#city-select"),
  statusButtons: document.querySelector("#status-buttons"),
  cityIndex: document.querySelector("#city-index"),
  clear: document.querySelector("#clear-button"),
  resultCount: document.querySelector("#result-count"),
  updated: document.querySelector("#updated"),
  loading: document.querySelector("#loading"),
  error: document.querySelector("#error"),
  empty: document.querySelector("#empty"),
  results: document.querySelector("#results"),
  retry: document.querySelector("#retry-button"),
  entryStat: document.querySelector("#entry-stat"),
  cityStat: document.querySelector("#city-stat"),
  sourceStat: document.querySelector("#source-stat")
};

let searchTimer;

function normalize(value) {
  return String(value || "")
    .normalize("NFKD")
    .replace(/[\u0300-\u036f]/g, "")
    .toLocaleLowerCase();
}

function formatNumber(value) {
  return new Intl.NumberFormat("en-US").format(value);
}

function validatePayload(payload) {
  if (!payload || !payload.meta || !Array.isArray(payload.entries)) {
    throw new Error("Unexpected data shape");
  }
  for (const entry of payload.entries) {
    if (!entry.id || !entry.city || !entry.name || !entry.status || !Array.isArray(entry.officialSources) || entry.officialSources.length === 0) {
      throw new Error(`Invalid entry: ${entry.id || "unknown"}`);
    }
  }
  return payload;
}

function readQueryParameters() {
  const parameters = new URLSearchParams(window.location.search);
  state.query = (parameters.get("q") || "").trim();
  state.city = parameters.get("city") || "all";
  state.status = parameters.get("status") || "all";
}

function updateQueryParameters() {
  const parameters = new URLSearchParams();
  if (state.query) parameters.set("q", state.query);
  if (state.city !== "all") parameters.set("city", state.city);
  if (state.status !== "all") parameters.set("status", state.status);
  const next = parameters.size ? `${window.location.pathname}?${parameters}` : window.location.pathname;
  window.history.replaceState(null, "", next);
}

function createElement(tag, className, text) {
  const node = document.createElement(tag);
  if (className) node.className = className;
  if (text !== undefined) node.textContent = text;
  return node;
}

function searchableText(entry) {
  const sourceNames = entry.officialSources.map((source) => `${source.name} ${source.type}`).join(" ");
  return normalize(`${entry.name} ${entry.city} ${entry.area} ${entry.statusLabel} ${sourceNames}`);
}

function getFilteredEntries() {
  const terms = normalize(state.query).split(/\s+/).filter(Boolean);
  return state.data.entries.filter((entry) => {
    if (state.city !== "all" && entry.city !== state.city) return false;
    if (state.status !== "all" && entry.status !== state.status) return false;
    if (!terms.length) return true;
    const haystack = searchableText(entry);
    return terms.every((term) => haystack.includes(term));
  });
}

function getCities() {
  const counts = new Map();
  for (const entry of state.data.entries) {
    counts.set(entry.city, (counts.get(entry.city) || 0) + 1);
  }
  return [...counts.entries()].sort(([cityA], [cityB]) => cityA.localeCompare(cityB, "en"));
}

function populateStatistics() {
  const meta = state.data.meta;
  elements.entryStat.textContent = formatNumber(meta.entryCount);
  elements.cityStat.textContent = formatNumber(meta.cityCount);
  elements.sourceStat.textContent = formatNumber(meta.officialSourceCount);
  elements.updated.textContent = `Data generated ${meta.generatedOn}`;
}

function populateCityOptions() {
  const cities = getCities();
  const availableCities = new Set(cities.map(([city]) => city));
  if (state.city !== "all" && !availableCities.has(state.city)) state.city = "all";

  const fragment = document.createDocumentFragment();
  for (const [city, count] of cities) {
    const option = createElement("option", "", `${city} (${formatNumber(count)})`);
    option.value = city;
    fragment.append(option);
  }
  elements.city.append(fragment);
  elements.city.value = state.city;
}

function renderStatusButtons() {
  const counts = new Map(STATUS_ORDER.map((status) => [status, 0]));
  for (const entry of state.data.entries) {
    counts.set(entry.status, (counts.get(entry.status) || 0) + 1);
  }

  const statuses = ["all", ...STATUS_ORDER.filter((status) => counts.get(status))];
  if (!statuses.includes(state.status)) state.status = "all";

  const fragment = document.createDocumentFragment();
  for (const status of statuses) {
    const label = status === "all" ? "All" : STATUS_LABELS[status];
    const count = status === "all" ? state.data.entries.length : counts.get(status);
    const button = createElement("button", "filter-chip");
    button.type = "button";
    button.dataset.status = status;
    button.setAttribute("aria-pressed", String(state.status === status));
    button.append(document.createTextNode(label), createElement("span", "", formatNumber(count)));
    fragment.append(button);
  }
  elements.statusButtons.replaceChildren(fragment);
}

function renderCityIndex() {
  const fragment = document.createDocumentFragment();
  for (const [city, count] of getCities()) {
    const button = createElement("button", "city-chip");
    button.type = "button";
    button.dataset.city = city;
    if (state.city === city) button.setAttribute("aria-current", "true");
    button.setAttribute("aria-label", `Show ${formatNumber(count)} entries in ${city}`);
    button.append(createElement("span", "", city), createElement("span", "", formatNumber(count)));
    fragment.append(button);
  }
  elements.cityIndex.replaceChildren(fragment);
}

function createSourceList(entry) {
  const list = createElement("ul", "source-list");
  for (const source of entry.officialSources) {
    const item = document.createElement("li");
    const link = createElement("a", "source-link");
    link.href = source.url;
    link.target = "_blank";
    link.rel = "noopener noreferrer";
    link.setAttribute("aria-label", `${source.name} — ${source.type} (opens in a new tab)`);
    link.append(
      createElement("span", "source-link-name", source.name),
      createElement("span", "source-link-type", source.type)
    );
    item.append(link);
    list.append(item);
  }
  return list;
}

function createCell(label) {
  const cell = document.createElement("td");
  cell.dataset.label = label;
  return cell;
}

function createEntryRow(entry) {
  const row = document.createElement("tr");

  const nameCell = createCell("Place or event");
  const name = createElement("div", "entry-name");
  const icon = createElement("span", "entry-icon", entry.icon);
  icon.setAttribute("aria-hidden", "true");
  name.append(icon, createElement("span", "", entry.name));
  nameCell.append(name);

  const areaCell = createCell("Area");
  areaCell.append(createElement("span", "area", entry.area));

  const statusCell = createCell("Planning state");
  statusCell.append(
    createElement("span", `status-pill status-${entry.status}`, entry.statusLabel),
    createElement("p", "planning-note", entry.planningNote)
  );

  const sourceCell = createCell("Official / primary sources");
  sourceCell.append(createSourceList(entry));

  row.append(nameCell, areaCell, statusCell, sourceCell);
  return row;
}

function createCitySection(city, entries) {
  const section = createElement("section", "city-section");
  section.id = `city-${city.toLocaleLowerCase().replace(/[^a-z0-9]+/g, "-")}`;
  section.setAttribute("aria-labelledby", `${section.id}-title`);

  const heading = createElement("div", "city-heading");
  const title = createElement("h3", "", city);
  title.id = `${section.id}-title`;
  heading.append(title, createElement("span", "", `${formatNumber(entries.length)} ${entries.length === 1 ? "entry" : "entries"}`));

  const wrapper = createElement("div", "table-wrap");
  const table = document.createElement("table");
  const caption = createElement("caption", "sr-only", `${city} places and events with primary sources`);
  const head = document.createElement("thead");
  const headerRow = document.createElement("tr");
  for (const label of ["Place or event", "Area", "Planning state", "Official / primary sources"]) {
    const header = createElement("th", "", label);
    header.scope = "col";
    headerRow.append(header);
  }
  head.append(headerRow);

  const body = document.createElement("tbody");
  for (const entry of entries) body.append(createEntryRow(entry));
  table.append(caption, head, body);
  wrapper.append(table);
  section.append(heading, wrapper);
  return section;
}

function renderResults() {
  const entries = getFilteredEntries();
  const grouped = new Map();
  for (const entry of entries) {
    if (!grouped.has(entry.city)) grouped.set(entry.city, []);
    grouped.get(entry.city).push(entry);
  }

  const querySuffix = state.query ? ` for “${state.query}”` : "";
  elements.resultCount.textContent = `${formatNumber(entries.length)} ${entries.length === 1 ? "result" : "results"}${querySuffix}`;
  elements.empty.hidden = entries.length > 0;
  elements.results.hidden = entries.length === 0;

  const fragment = document.createDocumentFragment();
  for (const [city, cityEntries] of grouped) {
    fragment.append(createCitySection(city, cityEntries));
  }
  elements.results.replaceChildren(fragment);

  const filtered = state.query || state.city !== "all" || state.status !== "all";
  elements.clear.hidden = !filtered;
  elements.city.value = state.city;
  renderStatusButtons();
  renderCityIndex();
  updateQueryParameters();
}

function setLoading(isLoading) {
  elements.loading.hidden = !isLoading;
  if (isLoading) {
    elements.error.hidden = true;
    elements.empty.hidden = true;
    elements.results.hidden = true;
  }
}

async function loadData() {
  setLoading(true);
  try {
    const response = await fetch("data.json", { cache: "no-store" });
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    state.data = validatePayload(await response.json());
    readQueryParameters();
    populateStatistics();
    populateCityOptions();
    elements.search.value = state.query;
    setLoading(false);
    renderResults();
  } catch (error) {
    console.error("Could not load KoreaFun data:", error);
    setLoading(false);
    elements.error.hidden = false;
    elements.resultCount.textContent = "Guide unavailable";
  }
}

elements.filters.addEventListener("submit", (event) => event.preventDefault());

elements.search.addEventListener("input", () => {
  window.clearTimeout(searchTimer);
  searchTimer = window.setTimeout(() => {
    state.query = elements.search.value.trim();
    renderResults();
  }, 120);
});

elements.city.addEventListener("change", () => {
  state.city = elements.city.value;
  renderResults();
});

elements.statusButtons.addEventListener("click", (event) => {
  const button = event.target.closest("button[data-status]");
  if (!button) return;
  state.status = button.dataset.status;
  renderResults();
});

elements.cityIndex.addEventListener("click", (event) => {
  const button = event.target.closest("button[data-city]");
  if (!button) return;
  state.city = state.city === button.dataset.city ? "all" : button.dataset.city;
  renderResults();
  document.querySelector(".results-bar").scrollIntoView({ behavior: "smooth", block: "start" });
});

elements.clear.addEventListener("click", () => {
  state.query = "";
  state.city = "all";
  state.status = "all";
  elements.search.value = "";
  renderResults();
  elements.search.focus();
});

elements.retry.addEventListener("click", loadData);

window.addEventListener("popstate", () => {
  if (!state.data) return;
  readQueryParameters();
  elements.search.value = state.query;
  renderResults();
});

loadData();

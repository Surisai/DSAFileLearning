# Milestone 2 Analysis

## Assumptions and Decisions

**Paris → Legacy mapping**  
- Paris CSV files use different headers.  
- In `merge_athlete_bio()` and `merge_events()`, we use a mapping dictionary to align Paris fields (`name`, `gender`, `birth_date`, `country_code`, etc.) to the legacy schema order.  
- `clean_birth_date()` normalizes dates to `dd-Mon-YYYY`.

**Duplicate athletes**  
- We assume the Paris athlete code is the `athlete_id`.  
- `merge_athlete_bio()` builds an `existing_by_id` set to skip duplicates.  
- A secondary check (`existing_by_name`) uses lowercase name + birth year for extra safety.

**Events with quoted commas**  
- Some events contain commas inside quotes (e.g., `"Individual, Men"`).  
- `read_csv_file()` uses Python’s `csv.reader` to preserve correct parsing.  
- Inner commas are cleaned only when required by the project rubric.

**Age calculation**  
- Age is computed after merging to ensure all data is available.  
- Implemented in `add_age()` as: `event_year - birth_year`.  
- If parsing the event year fails, we default to `2024` for Paris events.  
- If no birth year exists, age remains blank.

**Medal mapping**  
- Medal names are standardized to `G`, `S`, or `B` (capital first letter) in `merge_events()`.  
- `isTeamSport` defaults to `False` unless added to a whitelist.

**Games table**  
- `add_games()` ensures `Paris 2024` exists; appends `Milano-Cortina 2026` Winter entry if missing.

**No pandas**  
- Only Python standard libraries are used (`csv`, `re`, `datetime`, `collections`) to match course rules and keep dependencies minimal.

---

## Data Structures Used

- **List of lists**  
  - Used for raw CSV rows and output data.  
  - Keeps header at index `0`, followed by data rows.  
  - Read in `read_csv_file()`, written with `write_csv_file()`.

- **Dictionary**  
  - Used for quick lookups of header indexes and enrichment maps.  
  - Example: `birth_year_by_id` in `add_age()`.

- **Set**  
  - Used to track existing athlete IDs (`existing_by_id`) and prevent duplicate medal counting (`seen_medals`).  
  - O(1) average membership checks.

- **Defaultdict**  
  - Used in `generate_tally()` for medal counting without manual key existence checks.

---

## General Data Flow

1. **Read**: Load all CSV inputs with `read_csv_file()`.  
2. **Clean**:  
   - `clean_athlete_birth_dates()` normalizes `born` values.  
   - `clean_game_dates()` standardizes Games date ranges.  
3. **Merge**:  
   - `merge_athlete_bio()` maps Paris bios to legacy schema, appending only new IDs.  
   - `merge_events()` appends Paris medalists with edition metadata.  
   - `merge_countries()` adds missing NOCs.  
4. **Enrich**: `add_age()` calculates ages from merged bios and event years.  
5. **Tally**: `generate_tally()` groups medal counts by edition and country.  
6. **Write**: `write_csv_file()` outputs all processed tables.

---

## Why These Data Structures

- **List** – Natural for ordered tabular data and easy CSV writing.  
- **Dictionary** – O(1) average time for joins/lookups.  
- **Set** – O(1) average time for duplicate detection.  
- **Defaultdict** – Simplifies counters by avoiding manual key checks.

---

## Example Keys, Benefits, and Costs

- **`birth_year_by_id`** (dict)  
  - Key: `athlete_id`  
  - Benefit: Direct age calculation per event row.  
  - Cost: O(a) space.  
  - Speed: O(1) average lookup.

- **`tally[(edition, country)]`** (dict)  
  - Key: `(edition, country)` tuple  
  - Benefit: Clear grouping.  
  - Cost: O(G) space where G is number of groups.  
  - Speed: O(1) average update.

- **`seen_medals`** (set)  
  - Elements: `(edition, event, country, medal)` tuples  
  - Benefit: Prevents duplicate medal counting.  
  - Cost: O(U) space where U is unique medals.  
  - Speed: O(1) average membership check.

---

## Variables for Data Sizes

- `n` = rows in `olympic_athlete_event_results.csv`  
- `a` = rows in `olympic_athlete_bio.csv`  
- `p` = rows in Paris athletes CSV  
- `e` = rows in Paris events CSV  
- `m` = rows in Paris medallists CSV

---

## Runtime Analysis

**Cleaning**  
- `clean_athlete_birth_dates()` → O(a)  
- `clean_game_dates()` → O(1) (small constant table size)

**Merging Paris Data**  
- Build `existing_by_id` → O(a)  
- Append Paris bios → O(p)  
- Append Paris medalists → O(m)  
- Merge countries → O(#NOCs) ≈ O(1) in practice  
- **Overall**: O(a + p + m)

**Enrichment (Age)**  
- Build `birth_year_by_id` → O(a + p)  
- Fill ages for events → O(n + m)  
- **Overall**: O(a + p + n + m)

**Medal Tally**  
- One pass over events → O(n + m)  
- Optional sort → O(G log G)  
- **Overall**: O(n + m + G log G)

---

## Approximate Runtimes

- Cleaning: O(a)  
- Merging: O(a + p + m)  
- Enrichment: O(a + p + n + m)  
- Medal Tally: O(n + m) + O(G log G)  
- I/O (reading/writing CSVs) is linear in row count and dominates small dataset runtime.

---

## Corner Cases and Handling

- **Malformed Dates**: `clean_birth_date()` returns empty string; `add_age()` defaults to 2024 for Paris if year parsing fails.  
- **Quoted Commas in Events**: `csv.reader` preserves quotes; inner cleaning only if rubric requires.  
- **Missing Headers**: Header lookups in try/except blocks; use defaults if missing.  
- **ID Collisions**: Checked first with `existing_by_id`, then `existing_by_name`.  
- **Team Sports**: `isTeamSport` defaults to False; whitelist can override.

---

## Potential Improvements

- Add unit tests for mapping and date-cleaning functions.  
- Validate table structure after each processing step.  
- Create a robust date parser with multiple format fallbacks and logging.  
- Add performance timing for each major phase.

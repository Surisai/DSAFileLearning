# Milestone 2 Analysis and Application Description

## Assumptions and Decisions

**Paris → Legacy Mapping**  
- Paris CSV files use different headers than legacy data.  
- In `merge_athlete_bio()` and `merge_events()`, a mapping dictionary aligns Paris fields (`name`, `gender`, `birth_date`, `country_code`, etc.) to the legacy schema order.  
- `clean_birth_date()` normalizes dates to `dd-Mon-YYYY`.

**Duplicate Athletes**  
- Paris athlete code is treated as the `athlete_id`.  
- `merge_athlete_bio()` builds an `existing_by_id` set to skip duplicates.  
- Secondary check `existing_by_name` (lowercase name + birth year) catches mismatches.

**Events with Quoted Commas**  
- Some events contain commas inside quotes (e.g., `"Individual, Men"`).  
- `read_csv_file()` uses Python’s `csv.reader` to correctly handle them.  
- Inner commas are removed only when required by project rubric.

**Age Calculation**  
- Performed after merging to ensure complete data.  
- Implemented in `add_age()` as: `event_year - birth_year`.  
- Defaults to `2024` for Paris events if year parsing fails.  
- If no birth year, age remains blank.

**Medal Mapping**  
- Medal names are standardized to `G`, `S`, or `B` (capitalized first letter).  
- `isTeamSport` defaults to `False` unless whitelisted.

**Games Table Updates**  
- `add_games()` ensures `Paris 2024` is present.  
- Adds `Milano-Cortina 2026` Winter entry if missing.

**No Pandas**  
- Only standard Python libraries (`csv`, `re`, `datetime`, `collections`) are used to comply with course rules and avoid external dependencies.

---

## Data Structures Used

- **List of lists**  
  - Stores raw CSV rows and final output.  
  - Header at index `0`, followed by data rows.  
  - Used by `read_csv_file()` and `write_csv_file()`.

- **Dictionary**  
  - Fast lookups for header indexes and enrichment maps.  
  - Example: `birth_year_by_id` in `add_age()`.

- **Set**  
  - Tracks `existing_by_id` for duplicate detection.  
  - Tracks `seen_medals` to prevent double-counting.  
  - O(1) average membership checks.

- **Defaultdict**  
  - Simplifies medal tally generation without manual key checks.

---

## General Data Flow

1. **Read**: Load all CSV inputs with `read_csv_file()`.  
2. **Clean**:  
   - `clean_athlete_birth_dates()` fixes birth date format.  
   - `clean_game_dates()` standardizes Games date ranges.  
3. **Merge**:  
   - `merge_athlete_bio()` maps Paris bios to legacy schema, adding only new IDs.  
   - `merge_events()` appends Paris medalists with edition info.  
   - `merge_countries()` adds missing NOCs.  
4. **Enrich**: `add_age()` calculates athlete ages.  
5. **Tally**: `generate_tally()` counts medals per edition and country.  
6. **Write**: `write_csv_file()` outputs all processed tables.

---

## Why These Data Structures

- **List** – Best for ordered tabular data and easy CSV I/O.  
- **Dictionary** – O(1) lookups for joins and mappings.  
- **Set** – O(1) checks for duplicates.  
- **Defaultdict** – Cleaner code for counters.

---

## Example Keys, Benefits, and Costs

- **`birth_year_by_id` (dict)**  
  - Key: `athlete_id`  
  - Benefit: Direct, fast age calculation.  
  - Cost: O(a) space.  
  - Speed: O(1) average lookup.

- **`tally[(edition, country)]` (dict)**  
  - Key: `(edition, country)` tuple  
  - Benefit: Direct grouping.  
  - Cost: O(G) space.  
  - Speed: O(1) update.

- **`seen_medals` (set)**  
  - Elements: `(edition, event, country, medal)` tuples  
  - Benefit: Avoids duplicate medals.  
  - Cost: O(U) space.  
  - Speed: O(1) check.

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
- `clean_game_dates()` → O(1) (small table)

**Merging Paris Data**  
- Build `existing_by_id` → O(a)  
- Append Paris bios → O(p)  
- Append Paris medalists → O(m)  
- Merge countries → O(#NOCs) ≈ O(1)  
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
- I/O: Linear in total row count.

---

## Corner Cases and Handling

- **Malformed Dates**: `clean_birth_date()` returns empty; `add_age()` defaults Paris year to 2024 if missing.  
- **Quoted Commas**: `csv.reader` handles them; inner cleanup only if rubric says so.  
- **Missing Headers**: Defaults used if header not found.  
- **ID Collisions**: Checked by `existing_by_id` then `existing_by_name`.  
- **Team Sports**: `isTeamSport` defaults to False unless whitelisted.

---

## Potential Improvements

- Unit tests for mapping and date cleaning.  
- Schema validation after each merge.  
- Robust multi-format date parser with logging.  
- Performance timers for each major step.

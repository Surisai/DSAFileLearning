# DSAFileLearning

# Prompt Record: Date Cleaning Functions

## Context
These prompts were used to generate and improve Python functions for cleaning and standardizing date formats in athlete and game datasets. The data is in list-of-lists format, with the first row being the header.

---

### 🔧 Function: `clean_birth_date(date_str)`

| AI Tool       | Prompt |
|---------------|--------|
| GitHub Copilot | Write a Python function that takes a date string and returns it in `dd-MMM-yyyy` format. It should handle inputs like `yyyy`, `yyyy-mm-dd`, or already-formatted `dd-MMM-yyyy`, and return an empty string if the value is invalid or missing. Use regex and `datetime` for parsing. |

**Result**: Generated a date parsing function that checks the format with regex and uses `datetime.strptime()` to convert to the expected format.

**Alterations**: Added fallback for `'NA'`, `'n/a'`, and empty strings. Added specific regex checks to validate input structure.

---

### 🔄 Function: `clean_athlete_birth_dates(data)`

| AI Tool       | Prompt |
|---------------|--------|
| GitHub Copilot | Write a function that takes a list of lists representing CSV data. It should clean the `'born'` column by using a helper function to reformat dates. The first row is the header, and the rest are data rows. |

**Result**: Generated correct logic to find the `'born'` column index and apply the cleaning function row by row.

**Alterations**: Added check to ensure the header exists and `'born'` is in the header.

---

### 📆 Function: `clean_date_format(date_str)`

| AI Tool       | Prompt |
|---------------|--------|
| GitHub Copilot | Create a helper function that converts a string date in formats like `yyyy-mm-dd` or `dd-MMM-yyyy` to a consistent format `dd-MMM-yyyy`. Return empty string if invalid. |

**Result**: Successfully handled two `datetime.strptime()` patterns with fallback.

**Alterations**: Added `.strip()` to avoid leading/trailing space issues.

---

### 🎯 Function: `clean_game_dates(data)`

| AI Tool       | Prompt |
|---------------|--------|
| GitHub Copilot | Write a function to clean game date fields in a dataset: `start_date`, `end_date`, and `competition_date`. For `competition_date` formatted as `12 July -- 25 July`, convert to `12-Jul-2024 to 25-Jul-2024`. The input is a list of lists, first row is the header. |

**Result**: Accurately split the range, extracted the month from the first part, and constructed the final string in consistent format.

**Alterations**: Added fallback checks and ensured safe index access.

---

## Summary
This set of prompts was used to help build reusable and robust date cleaning functions for multiple parts of the dataset. They reflect best practices in using Copilot for transforming irregular real-world data into a consistent format for analysis.


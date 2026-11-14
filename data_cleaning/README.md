@'
# W1D3: Data Loading, Cleaning and Inspection

## Objective
Load, inspect, clean, and validate a dirty cafe sales dataset using Python, NumPy, and Pandas.

## Dataset
- Dataset: Cafe Sales - Dirty Data
- Original records: 10,000
- Original columns: 8
- File: dirty_cafe_sales.csv

## Cleaning Steps
1. Loaded the CSV dataset using Pandas.
2. Inspected dataset shape, columns, data types, and missing values.
3. Identified ERROR and UNKNOWN placeholders and replaced them with missing values.
4. Converted numerical columns to numeric data types.
5. Converted Transaction Date to datetime.
6. Filled categorical missing values using mode.
7. Filled Quantity and Price Per Unit using median.
8. Recalculated missing Total Spent values using Quantity × Price Per Unit.
9. Checked and removed duplicate records.
10. Used the IQR method to identify potential outliers.
11. Validated Total Spent against Quantity × Price Per Unit and corrected 733 mismatches.

## Final Results
- Final records: 10,000
- Final columns: 8
- Missing values: 460 in Transaction Date; zero in all other columns.
- All 10,000 Total Spent values match Quantity × Price Per Unit after correction.
- Missing transaction dates were retained because reliable replacement values were unavailable.

## Output
The cleaned dataset is saved at:

output/cleaned_cafe_sales.csv

## Technologies Used
- Python
- NumPy
- Pandas

## Project Structure
```text
data_cleaning/
├── data_cleaning.py
├── dirty_cafe_sales.csv
├── README.md
└── output/
    └── cleaned_cafe_sales.csv
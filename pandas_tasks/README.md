# W1D2 – Pandas for Data Manipulation

## Overview
This project demonstrates Pandas operations using a student performance dataset containing 32 records.

## Dataset Columns
- `number_courses`: Number of courses opted for.
- `time_study`: Average study time.
- `Marks`: Student marks obtained.

## Operations Performed
1. Loaded CSV data into a Pandas DataFrame.
2. Inspected dataset shape, data types, first 10 records, descriptive statistics and missing values.
3. Filtered students scoring above 20 marks.
4. Grouped students by number of courses and calculated average marks.
5. Merged student records with course category information.
6. Created pivot tables to summarize average marks and study time.
7. Exported cleaned data to CSV and Parquet formats.
8. Compared exported file sizes.

## File Size Comparison

| Format | Size |
|---|---:|
| CSV | 534 bytes |
| Parquet | 2958 bytes |

CSV was smaller for this small dataset due to Parquet metadata overhead.

## Technologies Used
- Python
- Pandas
- NumPy
- PyArrow
- VS Code
- Git and GitHub

## Learning Outcomes
Practiced DataFrame operations, filtering, grouping, merging, pivot tables and data export formats.
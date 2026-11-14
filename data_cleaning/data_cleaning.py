import numpy as np
import pandas as pd
from pathlib import Path

# Get the folder where this Python file is located
BASE_DIR = Path(__file__).resolve().parent

# Load the CSV dataset
file_path = BASE_DIR / "dirty_cafe_sales.csv"
data = pd.read_csv(file_path)

print(data.shape)
print("------------------------")
print(data.head(5))
print("------------------------")
print(data.columns.tolist())
print("------------------------")
print(data.describe())
print("------------------------")




# Identify missing values in each column
print("\nMissing Values:")
print(data.isnull().sum())

print("------------------------")

# Identify invalid placeholder values
print("\nERROR and UNKNOWN Values:")

for column in data.columns:
    error_count = data[column].astype(str).str.upper().isin(
        ["ERROR", "UNKNOWN"]
    ).sum()

    if error_count > 0:
        print(f"{column}: {error_count}")



# Replace ERROR and UNKNOWN with NaN

data.replace(["ERROR","UNKNOWN"],np.nan,inplace=True)

print("------------------------")

print(data.isnull().sum())


# Convert numerical columns into numeric data types
numeric_columns = ["Quantity", "Price Per Unit", "Total Spent"]

for column in numeric_columns:
    data[column] = pd.to_numeric(data[column], errors="coerce")

# Convert Transaction Date into datetime format
data["Transaction Date"] = pd.to_datetime(
    data["Transaction Date"],
    errors="coerce"
)

# Display updated data types
print("\nUpdated Data Types:")
print(data.dtypes)



# Handle missing values

# Fill categorical columns with their most frequent value
categorical_columns = ["Item", "Payment Method", "Location"]

for column in categorical_columns:
    data[column] = data[column].fillna(data[column].mode()[0])

# Fill numerical columns with median values
numerical_columns = ["Quantity", "Price Per Unit"]

for column in numerical_columns:
    data[column] = data[column].fillna(data[column].median())

# Recalculate Total Spent where it is missing
missing_total = data["Total Spent"].isnull()

data.loc[missing_total, "Total Spent"] = (
    data.loc[missing_total, "Quantity"]
    * data.loc[missing_total, "Price Per Unit"]
)

# Check remaining missing values
print("\nMissing Values After Cleaning:")
print(data.isnull().sum())



# Check duplicate records

duplicate_count = data.duplicated().sum()

print("\nNumber of Duplicate Records:")
print(duplicate_count)

# Check duplicate Transaction IDs
duplicate_ids = data["Transaction ID"].duplicated().sum()

print("\nDuplicate Transaction IDs:")
print(duplicate_ids)



# Detect outliers using the IQR method

numerical_columns = ["Quantity", "Price Per Unit", "Total Spent"]

for column in numerical_columns:
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)

    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = data[
        (data[column] < lower_bound) |
        (data[column] > upper_bound)
    ]

    print(f"\nOutliers in {column}:")
    print("Lower Bound:", lower_bound)
    print("Upper Bound:", upper_bound)
    print("Outlier Count:", len(outliers))


# Inspect outlier records in Total Spent

Q1 = data["Total Spent"].quantile(0.25)
Q3 = data["Total Spent"].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

total_spent_outliers = data[
    (data["Total Spent"] < lower_bound) |
    (data["Total Spent"] > upper_bound)
]

print("\nFirst 10 Total Spent Outliers:")
print(total_spent_outliers[
    ["Transaction ID", "Item", "Quantity", "Price Per Unit", "Total Spent"]
].head(10))

print("\nHighest Total Spent:")
print(data["Total Spent"].max())



# Validate Total Spent calculations

data["Calculated Total"] = (
    data["Quantity"] * data["Price Per Unit"]
)

# Compare actual and calculated totals
data["Total Match"] = np.isclose(
    data["Total Spent"],
    data["Calculated Total"]
)

print("\nTotal Spent Validation:")
print(data["Total Match"].value_counts())

# Display mismatched transactions
mismatches = data[data["Total Match"] == False]

print("\nMismatched Transactions:")
print(mismatches[
    ["Transaction ID", "Quantity", "Price Per Unit",
     "Total Spent", "Calculated Total"]
].head(10))


# Correct inconsistent Total Spent values

data["Calculated Total"] = (
    data["Quantity"] * data["Price Per Unit"]
)

# Identify mismatched transactions
mismatch_mask = ~np.isclose(
    data["Total Spent"],
    data["Calculated Total"]
)

# Count mismatches before correction
print("\nMismatches Before Correction:")
print(mismatch_mask.sum())

# Replace incorrect totals with calculated totals
data.loc[mismatch_mask, "Total Spent"] = (
    data.loc[mismatch_mask, "Calculated Total"]
)

# Remove temporary validation column
data = data.drop(columns=["Calculated Total"])

# Validate corrected Total Spent values
validation = np.isclose(
    data["Total Spent"],
    data["Quantity"] * data["Price Per Unit"]
)

print("\nValidation After Correction:")
print(pd.Series(validation).value_counts())

# Remove temporary validation columns
data = data.drop(
    columns=["Total Match", "Calculated Total"],
    errors="ignore"
)



# Create output directory
output_dir = BASE_DIR / "output"
output_dir.mkdir(exist_ok=True)

# Export cleaned dataset
output_file = output_dir / "cleaned_cafe_sales.csv"

data.to_csv(output_file, index=False)

print("\nCleaned Dataset Exported Successfully!")
print("File Location:", output_file)

# Display final dataset information
print("\nFinal Dataset Shape:")
print(data.shape)

print("\nFinal Missing Values:")
print(data.isnull().sum())

print("\nFinal Data Types:")
print(data.dtypes)



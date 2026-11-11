import numpy as np
import pandas as pd

from pathlib import Path

# Get the current file directory
BASE_DIR = Path(__file__).resolve().parent

# Load CSV dataset
df = pd.read_csv(BASE_DIR / "student_data.csv")

print("Dataset:")
print(df.head())


courses=df["number_courses"].to_numpy()
study_time=df["time_study"].to_numpy()
marks=df["Marks"].to_numpy()

# Calculate Mean
print("\nMean:")
print("Courses:", np.mean(courses))
print("Study Time:", np.mean(study_time))
print("Marks:", np.mean(marks))

# Calculate Standard Deviation
print("\nStandard Deviation:")
print("Courses:", np.std(courses))
print("Study Time:", np.std(study_time))
print("Marks:", np.std(marks))

# Calculate Correlation
print("\nCorrelation Matrix:")
data = np.column_stack((courses, study_time, marks))
print(np.corrcoef(data, rowvar=False))
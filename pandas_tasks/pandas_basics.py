
import pandas as pd
from pathlib import Path


def load_data(path: Path) -> pd.DataFrame:
    """Load student data from a CSV file."""
    return pd.read_csv(path)


def human_size(bytes_: int) -> str:
    """Convert file size into a human-readable format."""
    size = float(bytes_)

    for unit in ["B", "KB", "MB", "GB"]:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024

    return f"{size:.2f} TB"


def main():
    """Perform Pandas data manipulation operations."""

    # Load the student dataset
    base_dir = Path(__file__).resolve().parent
    data_path = base_dir / "student_data.csv"

    data = load_data(data_path)

    # Task 1: Dataset exploration
    print("Dataset Shape:\n", data.shape)
    print("\nFirst 10 Rows:\n", data.head(10))
    print("\nColumn Data Types:\n", data.dtypes)
    print("\nStatistical Summary:\n", data.describe())
    print("\nMissing Values:\n", data.isnull().sum())

    # Data cleaning: Convert numeric columns and remove invalid rows
    numeric_cols = ["number_courses", "time_study", "Marks"]

    data[numeric_cols] = data[numeric_cols].apply(
        pd.to_numeric, errors="coerce"
    )

    data = data.dropna(subset=numeric_cols).copy()

    print("\nCleaned Dataset Shape:", data.shape)

    # Task 2: Filtering
    high_score_students = data[data["Marks"] > 20]

    print("\nStudents scoring more than 20 marks:")
    print(high_score_students)

    # Task 3: GroupBy
    average_marks = (
        data.groupby("number_courses")["Marks"]
        .mean()
        .sort_values(ascending=False)
    )

    print("\nAverage Marks by Number of Courses:")
    print(average_marks)

    # Task 4: Merge
    course_info = pd.DataFrame({
        "number_courses": [3, 4, 5, 6, 7, 8],
        "course_category": [
            "Low", "Low", "Medium", "Medium", "High", "High"
        ]
    })

    merged_data = pd.merge(
        data,
        course_info,
        on="number_courses",
        how="left"
    )

    print("\nMerged Student Data:")
    print(merged_data.head(10))

    # Task 5: Pivot Table
    pivot_data = pd.pivot_table(
        data,
        values=["Marks", "time_study"],
        index="number_courses",
        aggfunc="mean"
    )

    print("\nPivot Table:")
    print(pivot_data)

    # Task 6: Export cleaned data
    output_dir = base_dir / "output"
    output_dir.mkdir(exist_ok=True)

    csv_path = output_dir / "cleaned_student_data.csv"
    parquet_path = output_dir / "cleaned_student_data.parquet"

    data.to_csv(csv_path, index=False)
    data.to_parquet(parquet_path, index=False)

    # Compare file sizes
    csv_size = csv_path.stat().st_size
    parquet_size = parquet_path.stat().st_size

    print("\nFile Export Results:")
    print("CSV Size:", human_size(csv_size))
    print("Parquet Size:", human_size(parquet_size))

    print("\nData export completed successfully!")


if __name__ == "__main__":
    main()

import pandas as pd
import numpy as np


def assess_data_quality(df: pd.DataFrame) -> pd.DataFrame:
    """Calculates missingness and structural data types across features."""
    missing_count = df.isnull().sum()
    missing_pct = (df.isnull().sum() / len(df)) * 100
    data_types = df.dtypes

    quality_report = pd.DataFrame(
        {"Data_Type": data_types, "Missing_Count": missing_count, "Percentage_%": missing_pct}
    )
    return quality_report.sort_values(by="Percentage_%", ascending=False)


def handle_severity_outliers(
    df: pd.DataFrame, column: str, factor: float = 1.5
) -> pd.DataFrame:
    """Caps extreme claim values using the Interquartile Range (IQR) method

    to protect downstream pricing models from volatile distortions.
    """
    q1 = df[column].quantile(0.25)
    q3 = df[column].quantile(0.75)
    iqr = q3 - q1

    lower_bound = max(0, q1 - factor * iqr)
    upper_bound = q3 + factor * iqr

    # Apply capping
    df_cleaned = df.copy()
    df_cleaned[column] = np.clip(df_cleaned[column], lower_bound, upper_bound)
    return df_cleaned
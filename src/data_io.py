"""
data_io.py
----------
Utility functions for loading and preparing the London Bike Sharing dataset.
"""

from pathlib import Path

import pandas as pd

from src.schema import validate_bike_data


def load_bike_data(path: str | Path) -> pd.DataFrame:
    """
    Load and clean the London Bike dataset.
    """

    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    # 1. Load CSV
    df = pd.read_csv(path)

    # 2. Basic cleaning: lower-case + underscores
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("(", "")
        .str.replace(")", "")
    )

    # 3. Parse datetime columns
    datetime_cols = [c for c in df.columns if "time" in c or "date" in c]
    for col in datetime_cols:
        try:
            df[col] = pd.to_datetime(df[col])
        except Exception:
            pass

    # 4. Sort by datetime if exists
    if datetime_cols:
        df = df.sort_values(datetime_cols[0])

    # 5. Scale humidity if in % instead of 0–1
    if "hum" in df.columns and df["hum"].max() > 1:
        df["hum"] = df["hum"] / 100.0

    # 6. Drop duplicates
    df = df.drop_duplicates().reset_index(drop=True)

    # 7. Validate against schema
    df = validate_bike_data(df)

    return df

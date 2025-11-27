"""
schema.py
---------
Pandera schema (data contract) for the London bike sharing dataset.
"""

import pandas as pd
import pandera as pa
from pandera import Check, Column, DataFrameSchema

bike_schema = DataFrameSchema(
    {
        "timestamp": Column(pa.Timestamp, nullable=False),
        "cnt": Column(pa.Int64, Check.ge(0), nullable=False),
        "t1": Column(float, Check.between(-30, 50), nullable=False),
        "t2": Column(float, Check.between(-30, 50), nullable=False),
        "hum": Column(float, Check.between(0, 1), nullable=False),
        "wind_speed": Column(float, Check.ge(0), nullable=False),
        "weather_code": Column(float, nullable=False),
        "is_holiday": Column(float, Check.isin([0.0, 1.0]), nullable=False),
        "is_weekend": Column(float, Check.isin([0.0, 1.0]), nullable=False),
        "season": Column(float, Check.isin([0.0, 1.0, 2.0, 3.0]), nullable=False),
    },
    checks=[
        Check(lambda df: df["timestamp"].is_monotonic_increasing, element_wise=False),
    ],
    strict=False,
    name="bike_schema",
)


def validate_bike_data(df: pd.DataFrame) -> pd.DataFrame:
    """Validate the raw bike data and return the validated dataframe."""
    return bike_schema.validate(df)

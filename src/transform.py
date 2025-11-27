"""
transform.py
------------
Feature engineering for the London bike sharing dataset.
"""

from __future__ import annotations

import pandas as pd


def make_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create modeling/analysis features from the raw bike dataframe.

    Assumes `df` has been validated and contains at least:
    timestamp, cnt, t1, t2, hum, wind_speed, weather_code, is_holiday, is_weekend, season.
    """

    df = df.copy()

    # --- Time-based features ---
    df["hour"] = df["timestamp"].dt.hour
    df["weekday"] = df["timestamp"].dt.weekday  # 0=Mon
    df["month"] = df["timestamp"].dt.month
    df["year"] = df["timestamp"].dt.year
    df["dayofyear"] = df["timestamp"].dt.dayofyear

    # Keep weekend but make an explicit boolean/int version
    df["is_weekend_bool"] = df["is_weekend"].astype(int)

    # --- Binned / categorical versions ---
    # Temperature buckets: cold / mild / warm / hot
    df["temp_bin"] = pd.cut(
        df["t1"],
        bins=[-50, 0, 10, 20, 35, 100],
        labels=["freezing", "cold", "mild", "warm", "hot"],
    )

    # Rush hour flag (commuting times)
    df["is_rush_hour"] = df["hour"].isin([7, 8, 9, 16, 17, 18]).astype(int)

    # Working hours flag
    df["is_working_hour"] = df["hour"].between(8, 18).astype(int)

    # --- Rolling features (short history) ---
    # Sort just in case
    df = df.sort_values("timestamp")

    # Rolling mean of last 24 hours (window=24, since data is hourly)
    df["cnt_roll_mean_24h"] = df["cnt"].rolling(window=24, min_periods=1).mean()

    # Lag features: previous hour’s demand
    df["cnt_lag_1"] = df["cnt"].shift(1)
    df["cnt_lag_24"] = df["cnt"].shift(24)

    return df

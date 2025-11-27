from src.data_io import load_bike_data
from src.transform import make_features


def test_make_features_shapes_and_columns():
    df_raw = load_bike_data("data/raw/london_merged.csv")
    df_feat = make_features(df_raw)

    # same number of rows
    assert len(df_feat) == len(df_raw)

    # important new columns exist
    expected_cols = [
        "hour",
        "weekday",
        "month",
        "year",
        "dayofyear",
        "temp_bin",
        "is_rush_hour",
        "is_working_hour",
        "cnt_roll_mean_24h",
        "cnt_lag_1",
        "cnt_lag_24",
    ]
    for col in expected_cols:
        assert col in df_feat.columns

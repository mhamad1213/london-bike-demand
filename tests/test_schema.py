import pandas as pd

from src.schema import validate_bike_data


def test_validate_bike_data_smoke():
    # Minimal fake row that should pass
    df = pd.DataFrame(
        {
            "timestamp": ["2015-01-04 00:00:00"],
            "cnt": [0],
            "t1": [5.0],
            "t2": [5.0],
            "hum": [0.5],
            "wind_speed": [1.0],
            "weather_code": [1.0],
            "is_holiday": [0.0],
            "is_weekend": [0.0],
            "season": [0.0],
        }
    )
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    validated = validate_bike_data(df)
    assert not validated.empty

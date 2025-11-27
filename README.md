# London Bike Demand Analysis 🚴‍♂️

An end-to-end data analysis and forecasting project exploring how weather, seasonality, and temporal patterns influence hourly bike demand in London.  
Built with clean engineering practices, validated data pipelines, reproducible notebooks, and a baseline machine learning model.

---

## 📦 Project Structure

london-bike-demand/
│
├── data/               # Raw and processed datasets
├── notebooks/          # EDA + modeling notebooks
├── reports/            # Final report + exported figures
├── src/                # Source code (data loading, schemas, features)
│   ├── data_io.py
│   ├── schema.py
│   └── transform.py
│
├── tests/              # Tests for validation + feature engineering
├── venv/               # Virtual environment
├── requirements.txt
├── pyproject.toml
└── README.md
---

## 🎯 Project Goals

- Understand how hourly bike demand changes across:
  - time of day  
  - day of week  
  - season  
  - weather conditions  
- Build a reliable data pipeline with validation checks
- Engineer features for prediction (lags, rolling averages, time features)
- Train a baseline model to forecast hourly demand

---

## 🛠️ Tools & Technologies

- **Python**
- **Pandas, NumPy**
- **Matplotlib, Plotly**
- **Pandera** (data validation)
- **scikit-learn** (baseline model)
- **Jupyter Notebooks**
- **pytest** (testing)
- **Git + virtual environments**

---

## 🔍 Exploratory Data Analysis (EDA)

Key patterns identified:

- Strong **commuting peaks** at ~8 AM and ~5–6 PM on weekdays  
- Flatter demand on weekends with a midday peak  
- Highest demand in **summer**, lowest in **winter**  
- Temperature, humidity, and wind all have measurable effects on hourly usage  

Example visualisations are included in the final report.

---

## 🧩 Feature Engineering

Created features include:

- Time features: `hour`, `weekday`, `month`, `year`
- Behaviour features: `is_weekend_bool`, `is_rush_hour`, `is_working_hour`
- Weather transformations: temperature bins
- Time-series features:
  - `cnt_lag_1`, `cnt_lag_24`
  - `cnt_roll_mean_24h`

All feature generation lives in:  
`src/transform.py`

---

## 📊 Baseline Model

A **Random Forest Regressor** was trained using an 80/20 chronological split.

**Test Results:**
- **Mean Absolute Error (MAE):** ~95.85  
- **R²:** ~0.976  

Strong performance indicates predictable temporal and weather-driven patterns.

---

## 📜 Final Report

Full analysis, results, and visuals are available in:

👉 `reports/report.md`

---

## 🧪 Testing

Basic tests ensure:

- Schema validation works as expected  
- Feature engineering generates required columns  

Run tests:

```bash
pytest

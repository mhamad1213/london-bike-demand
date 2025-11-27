# London Bike Demand Analysis

## 1. Project Overview

The goal of this project was to understand how hourly bike demand is influenced by temporal patterns and weather conditions, and to build a baseline predictive model.

- **Dataset:** London Bike Sharing Dataset (Kaggle)
- **Time Range:** Jan 2015 – Jan 2017
- **Tools:** Python, Pandas, Matplotlib, Pandera, scikit-learn

---

## 2. Data Validation & Cleaning

Before the analysis was completed, a Pandera schema was used to validate the raw dataset to ensure the following:

- no negative counts
- humidity scaled properly (0–1)
- timestamps parsed correctly
- no duplicates
- sorted chronologically

This ensures the analysis and model rely on consistent, trustworthy data.

---

## 3. Exploratory Data Analysis (EDA)

### 3.1 Temporal Patterns

**Hourly patterns**  
- Clear commuting peaks at ~8 AM and ~5–6 PM on weekdays.  
- Weekends show flatter usage with a single midday peak.

**Daily/Weekday patterns**  
- Weekdays show strong rush-hour structure.  
- Weekends have higher leisure ridership.

**Monthly/Seasonal trends**  
- Summer months show the highest demand.  
- Winter months have significantly lower usage.

![Bike Over Time](figures/bike_over_time.png)

![Rentals Per Hour](figures/hourly_rentals.png)

![Average rentals Per Month](figures/rental_per_month.png)

---

## 4. Weather Effects

### 4.1 Temperature
- Demand increases steadily as temperature rises up to ~20°C.
- Usage plateaus or slightly declines above ~25°C.

### 4.2 Humidity & Wind
- Very high humidity correlates with slightly lower rentals.
- Stronger wind speeds also reduce demand.

### 4.3 Weather Codes
- Clear/partly cloudy days see much higher demand than rainy or foggy days.

![Temperature influence on bike hire](figures/temp_influence.png)


---

## 5. Feature Engineering

The following engineered features were created:

- `hour`, `weekday`, `month`, `year`
- `is_weekend_bool`, `is_rush_hour`, `is_working_hour`
- temperature bins (`temp_bin`)
- rolling averages (`cnt_roll_mean_24h`)
- lag features (`cnt_lag_1`, `cnt_lag_24`)

These improve model performance and reveal patterns in ridership behaviour.

---

## 6. Baseline Model

A simple **Random Forest Regressor** was trained on 80% of the chronological data.

**Performance on test set:**

- **MAE:** 95.85209315698677 
- **R²:** 0.9763574897288727 

These values indicate the model captures general demand patterns but has room to improve with more advanced time-series techniques.

**Top features:**  
Based on feature importance:

- `cnt_lag_1` (previous hour's demand)
- `cnt_lag_24` (same hour yesterday)
- `temperature`
- `hour`
- `month`
- `is_rush_hour`

---

## 7. Key Insights

- Bike demand strongly follows weekday commuting patterns.
- Temperature is one of the most influential weather variables.
- Lag features suggest strong short-term temporal dependency.
- Seasonal variations significantly affect ridership.
- Demand prediction is feasible using simple models + engineered features.

---

## 8. Limitations

- No event or holiday-specific data beyond simple flags.
- Weather granularity may not capture microclimate variation.
- More advanced forecasting (Prophet, SARIMA, LSTM) likely needed for deployment-level accuracy.

---

## 9. Next Steps

Future improvements could include:

- Adding external data (events, rainfall intensity, holidays).
- Deploying an interactive dashboard with Streamlit.
- Trying time-series models: SARIMA, XGBoost, Prophet.
- Hyperparameter tuning for model improvements.
- Cross-city comparisons or multi-city modelling.

---

## 10. Conclusion

This project demonstrates a complete, reproducible data pipeline and analytical workflow for understanding and predicting London’s hourly bike demand. The combination of validated data, engineered features, and interpretable modelling provides a solid foundation for further development and real-world deployment.

import pandas as pd
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

import numpy as np

BASE_DIR = Path(__file__).resolve().parent.parent

input_path = BASE_DIR / "Dataset" / "restaurant_dataset.csv"
output_path = BASE_DIR / "Predictive_Modelling" / "model_comparison.csv"

# Load actual dataset
df = pd.read_csv(input_path)

# Encode categorical columns
df["Has Table booking"] = df["Has Table booking"].map({"Yes": 1, "No": 0})
df["Has Online delivery"] = df["Has Online delivery"].map({"Yes": 1, "No": 0})

# Select features and target
features = [
    "Average Cost for two",
    "Price range",
    "Votes",
    "Has Table booking",
    "Has Online delivery"
]

X = df[features]
y = df["Aggregate rating"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scale features for Linear Regression
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Define models
models = {
    "Linear Regression": LinearRegression(),
    "Decision Tree": DecisionTreeRegressor(max_depth=5, random_state=42),
    "Random Forest": RandomForestRegressor(
        n_estimators=100, max_depth=8, random_state=42
    )
}

results = []

# Train and evaluate
for name, model in models.items():

    if name == "Linear Regression":
        model.fit(X_train_scaled, y_train)
        predictions = model.predict(X_test_scaled)
    else:
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)
    mse = mean_squared_error(y_test, predictions)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, predictions)

    results.append({
        "Model": name,
        "MAE": mae,
        "MSE": mse,
        "RMSE": rmse,
        "R2 Score": r2
    })

# Compare models
comparison = pd.DataFrame(results)
comparison = comparison.sort_values(by="R2 Score", ascending=False)

comparison.to_csv(output_path, index=False)

print("\nMODEL PERFORMANCE COMPARISON")
print(comparison.to_string(index=False))

print("\nPredictive Modelling Completed!")
print("Results saved:", output_path)

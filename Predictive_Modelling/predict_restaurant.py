
import pandas as pd
from pathlib import Path
from sklearn.ensemble import RandomForestRegressor

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
dataset_path = BASE_DIR / "Dataset" / "restaurant_dataset.csv"

# Load actual dataset
df = pd.read_csv(dataset_path)

# Encode categorical values
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

df = df.dropna(subset=features + ["Aggregate rating"])

X = df[features]
y = df["Aggregate rating"]

# Train Random Forest
model = RandomForestRegressor(
    n_estimators=100,
    max_depth=8,
    random_state=42
)

model.fit(X, y)

# User input
print("\n===== RESTAURANT RATING PREDICTOR =====")

try:
    booking = input(
        "Does the restaurant offer table booking? (Yes/No): "
    ).strip().capitalize()

    delivery = input(
        "Does the restaurant offer online delivery? (Yes/No): "
    ).strip().capitalize()

    price = int(input("Enter price range (1-4): "))
    cost = float(input("Enter average cost for two: "))
    votes = int(input("Enter number of votes: "))

    if booking not in ["Yes", "No"]:
        raise ValueError("Booking must be Yes or No.")

    if delivery not in ["Yes", "No"]:
        raise ValueError("Delivery must be Yes or No.")

    if price not in [1, 2, 3, 4]:
        raise ValueError("Price range must be between 1 and 4.")

    if cost < 0 or votes < 0:
        raise ValueError("Cost and votes cannot be negative.")

    new_restaurant = pd.DataFrame([{
        "Average Cost for two": cost,
        "Price range": price,
        "Votes": votes,
        "Has Table booking": 1 if booking == "Yes" else 0,
        "Has Online delivery": 1 if delivery == "Yes" else 0
    }])

    prediction = model.predict(new_restaurant)[0]

    print("\nPredicted Aggregate Rating:", round(prediction, 2))

except ValueError as e:
    print("\nInvalid input:", e)

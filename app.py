
from flask import Flask, request, jsonify, send_from_directory
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from pathlib import Path

# Project directory
BASE_DIR = Path(__file__).resolve().parent

# Flask application
app = Flask(
    __name__,
    static_folder=str(BASE_DIR / "Website"),
    static_url_path=""
)

# Load actual dataset
df = pd.read_csv(BASE_DIR / "Dataset" / "restaurant_dataset.csv")

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


# Homepage
@app.route("/")
def home():
    return send_from_directory(
        BASE_DIR / "Website",
        "index.html"
    )


# Prediction API
@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        booking = data.get("booking")
        delivery = data.get("delivery")
        price = int(data.get("price"))
        cost = float(data.get("cost"))
        votes = int(data.get("votes"))

        if booking not in ["Yes", "No"]:
            return jsonify({"error": "Invalid table booking value"}), 400

        if delivery not in ["Yes", "No"]:
            return jsonify({"error": "Invalid delivery value"}), 400

        if price not in [1, 2, 3, 4]:
            return jsonify({"error": "Price range must be between 1 and 4"}), 400

        if cost < 0 or votes < 0:
            return jsonify({"error": "Cost and votes cannot be negative"}), 400

        input_data = pd.DataFrame([{
            "Average Cost for two": cost,
            "Price range": price,
            "Votes": votes,
            "Has Table booking": 1 if booking == "Yes" else 0,
            "Has Online delivery": 1 if delivery == "Yes" else 0
        }])

        prediction = model.predict(input_data)[0]

        return jsonify({
            "prediction": round(float(prediction), 2)
        })

    except (ValueError, TypeError):
        return jsonify({"error": "Please provide valid input values"}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)

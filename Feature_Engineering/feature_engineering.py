
import pandas as pd
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent

input_path = BASE_DIR / "Dataset" / "restaurant_dataset.csv"

output_path = (
    BASE_DIR
    / "Feature_Engineering"
    / "engineered_restaurant_dataset.csv"
)

# Load actual restaurant dataset
df = pd.read_csv(input_path)

print("Original Dataset:")
print(df.head())

print("\nOriginal Dataset Shape:", df.shape)

# --------------------------------
# 1. Name Length
# --------------------------------

df["Name Length"] = df["Restaurant Name"].astype(str).str.len()

# --------------------------------
# 2. Address Length
# --------------------------------

df["Address Length"] = df["Address"].astype(str).str.len()

# --------------------------------
# 3. Cuisine Count
# --------------------------------

df["Cuisines"] = df["Cuisines"].fillna("Unknown")

df["Cuisine Count"] = df["Cuisines"].apply(
    lambda x: len(x.split(","))
)

# --------------------------------
# 4. Encode Categorical Variables
# --------------------------------

df["Table Booking Encoded"] = (
    df["Has Table booking"].map({"Yes": 1, "No": 0})
)

df["Online Delivery Encoded"] = (
    df["Has Online delivery"].map({"Yes": 1, "No": 0})
)

df["Delivering Now Encoded"] = (
    df["Is delivering now"].map({"Yes": 1, "No": 0})
)

df["Order Menu Encoded"] = (
    df["Switch to order menu"].map({"Yes": 1, "No": 0})
)

# --------------------------------
# 5. Price Category
# --------------------------------

price_mapping = {
    1: "Budget",
    2: "Moderate",
    3: "Premium",
    4: "Luxury"
}

df["Price Category"] = df["Price range"].map(price_mapping)

# --------------------------------
# 6. Save Engineered Dataset
# --------------------------------

df.to_csv(output_path, index=False)

print("\nEngineered Features:")
print(df[[
    "Restaurant Name",
    "Name Length",
    "Address Length",
    "Cuisine Count",
    "Table Booking Encoded",
    "Online Delivery Encoded",
    "Price Category"
]].head(10))

print("\nFinal Dataset Shape:", df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nFeature Engineering Completed Successfully!")
print("Saved to:", output_path)

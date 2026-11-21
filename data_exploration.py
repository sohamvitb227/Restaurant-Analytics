
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load Dataset
df = pd.read_csv("Dataset/restaurant_dataset.csv")

# 2. Explore Dataset
print("Dataset Shape:", df.shape)
print("Number of Rows:", df.shape[0])
print("Number of Columns:", df.shape[1])

# 3. Dataset Information
print("\nDataset Information:")
df.info()

# 4. Check Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# 5. Handle Missing Values
df["Cuisines"] = df["Cuisines"].fillna("Unknown")

print("\nMissing Values After Handling:")
print(df.isnull().sum())

# 6. Check and Convert Data Types
print("\nData Types Before Conversion:")
print(df.dtypes)

df["Aggregate rating"] = pd.to_numeric(
    df["Aggregate rating"], errors="coerce"
)

df["Average Cost for two"] = pd.to_numeric(
    df["Average Cost for two"], errors="coerce"
)

df["Votes"] = pd.to_numeric(
    df["Votes"], errors="coerce"
)

print("\nData Types After Conversion:")
print(df.dtypes)

# 7. Analyze Target Variable
print("\nAggregate Rating Distribution:")
rating_counts = df["Aggregate rating"].value_counts().sort_index()
print(rating_counts)

# 8. Target Variable Statistics
print("\nTarget Variable Statistics:")
print(df["Aggregate rating"].describe())

# 9. Calculate Rating Percentages
print("\nRating Distribution in Percentage:")
rating_percentages = (
    rating_counts / len(df) * 100
).round(2)

print(rating_percentages)

# 10. Visualize Aggregate Rating Distribution
plt.figure(figsize=(10, 5))

sns.histplot(
    df["Aggregate rating"],
    bins=20,
    kde=True
)

plt.title("Distribution of Aggregate Ratings")
plt.xlabel("Aggregate Rating")
plt.ylabel("Number of Restaurants")

plt.tight_layout()

# Save graph in project root
plt.savefig("aggregate_rating_distribution.png")

plt.show()

# 11. Save Cleaned Dataset
df.to_csv(
    "cleaned_restaurant_dataset.csv",
    index=False
)

print("\nData Exploration and Preprocessing Completed!")

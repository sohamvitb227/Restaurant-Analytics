
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

input_path = BASE_DIR / "Dataset" / "restaurant_dataset.csv"
output_dir = BASE_DIR / "Data_Visualization"

df = pd.read_csv(input_path)

# 1. Rating Distribution
plt.figure(figsize=(10, 6))
plt.hist(df["Aggregate rating"], bins=20, edgecolor="black")
plt.title("Restaurant Rating Distribution")
plt.xlabel("Aggregate Rating")
plt.ylabel("Number of Restaurants")
plt.tight_layout()
plt.savefig(output_dir / "rating_distribution_histogram.png")
plt.close()

# 2. Average Rating by Top 10 Cities
city_ratings = df.groupby("City")["Aggregate rating"].mean()
top_cities = city_ratings.sort_values(ascending=False).head(10)

plt.figure(figsize=(12, 6))
top_cities.plot(kind="bar")
plt.title("Top 10 Cities by Average Restaurant Rating")
plt.xlabel("City")
plt.ylabel("Average Rating")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(output_dir / "average_rating_by_city.png")
plt.close()

# 3. Price Range vs Average Rating
price_ratings = df.groupby("Price range")["Aggregate rating"].mean()

plt.figure(figsize=(8, 5))
price_ratings.plot(kind="bar")
plt.title("Price Range vs Average Restaurant Rating")
plt.xlabel("Price Range")
plt.ylabel("Average Rating")
plt.tight_layout()
plt.savefig(output_dir / "price_range_vs_rating.png")
plt.close()

# 4. Table Booking and Online Delivery
booking_rating = df.groupby("Has Table booking")["Aggregate rating"].mean()
delivery_rating = df.groupby("Has Online delivery")["Aggregate rating"].mean()

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

booking_rating.plot(kind="bar", ax=axes[0], title="Table Booking vs Rating")
delivery_rating.plot(kind="bar", ax=axes[1], title="Online Delivery vs Rating")

axes[0].set_ylabel("Average Rating")
axes[1].set_ylabel("Average Rating")

plt.tight_layout()
plt.savefig(output_dir / "booking_delivery_vs_rating.png")
plt.close()

# 5. Correlation Heatmap
numeric_columns = [
    "Average Cost for two",
    "Price range",
    "Aggregate rating",
    "Votes",
    "Longitude",
    "Latitude"
]

correlation = df[numeric_columns].corr()

plt.figure(figsize=(10, 7))
sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Restaurant Dataset Correlation Heatmap")
plt.tight_layout()
plt.savefig(output_dir / "correlation_heatmap.png")
plt.close()

print("\nDATA VISUALIZATION COMPLETED!")
print("Generated charts:")
print("1. Rating Distribution")
print("2. Average Rating by City")
print("3. Price Range vs Rating")
print("4. Booking and Delivery vs Rating")
print("5. Correlation Heatmap")

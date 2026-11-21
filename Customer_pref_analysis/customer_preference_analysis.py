
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent

input_path = BASE_DIR / "Dataset" / "restaurant_dataset.csv"
output_path = BASE_DIR / "Customer_pref_analysis" / "customer_preference_dataset.csv"

# Load actual dataset
df = pd.read_csv(input_path)

# Remove rows where cuisine information is missing
df = df.dropna(subset=["Cuisines"]).copy()

# Split multiple cuisines into separate rows
df["Cuisines"] = df["Cuisines"].str.split(",")
cuisine_df = df.explode("Cuisines")

# Clean cuisine names
cuisine_df["Cuisines"] = cuisine_df["Cuisines"].str.strip()

# Calculate customer preference statistics
analysis = cuisine_df.groupby("Cuisines").agg(
    Restaurant_Count=("Restaurant ID", "count"),
    Total_Votes=("Votes", "sum"),
    Average_Rating=("Aggregate rating", "mean")
).reset_index()

# Sort by total votes
analysis = analysis.sort_values(
    by="Total_Votes", ascending=False
)

# Save results
analysis.to_csv(output_path, index=False)

print("\nTOP 10 MOST POPULAR CUISINES")
print(analysis.head(10).to_string(index=False))

# Chart 1: Popular cuisines
top_cuisines = analysis.head(10)

plt.figure(figsize=(12, 6))
plt.bar(top_cuisines["Cuisines"], top_cuisines["Total_Votes"])
plt.title("Top 10 Most Popular Cuisines")
plt.xlabel("Cuisine")
plt.ylabel("Total Votes")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(BASE_DIR / "Customer_pref_analysis" / "popular_cuisines.png")
plt.close()

# Chart 2: Average ratings
top_rated = analysis.sort_values(
    by="Average_Rating", ascending=False
).head(10)

plt.figure(figsize=(12, 6))
plt.bar(top_rated["Cuisines"], top_rated["Average_Rating"])
plt.title("Top 10 Highest Rated Cuisines")
plt.xlabel("Cuisine")
plt.ylabel("Average Rating")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(BASE_DIR / "Customer_pref_analysis" / "cuisine_ratings.png")
plt.close()

print("\nAnalysis completed successfully!")
print("Dataset saved:", output_path)
print("Charts generated successfully!")

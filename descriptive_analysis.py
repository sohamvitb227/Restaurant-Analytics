
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load Dataset
df = pd.read_csv("Dataset/restaurant_dataset.csv")

# Handle missing cuisine values
df["Cuisines"] = df["Cuisines"].fillna("Unknown")

# 2. Basic Statistical Analysis
# Exclude ID and Country Code because they are identifiers/categories
numeric_columns = df.select_dtypes(include="number").columns.drop(
    ["Restaurant ID", "Country Code"]
)

print("BASIC STATISTICAL ANALYSIS")
print(df[numeric_columns].describe())

# Save statistical summary
df[numeric_columns].describe().to_csv(
    "descriptive_statistics.csv"
)

# 3. Country Code Distribution
print("\nCOUNTRY CODE DISTRIBUTION")
country_counts = df["Country Code"].value_counts()
print(country_counts)

country_counts.to_csv("country_distribution.csv")

# 4. City Distribution
print("\nTOP 10 CITIES WITH MOST RESTAURANTS")
city_counts = df["City"].value_counts()
top_cities = city_counts.head(10)
print(top_cities)

top_cities.to_csv("top_cities.csv")

# 5. Cuisine Distribution
# Split cuisines because one restaurant can offer multiple cuisines
cuisine_counts = (
    df["Cuisines"]
    .str.split(",")
    .explode()
    .str.strip()
    .value_counts()
)

print("\nTOP 10 CUISINES")
top_cuisines = cuisine_counts.head(10)
print(top_cuisines)

top_cuisines.to_csv("top_cuisines.csv")

# 6. Visualize Top 10 Cities
plt.figure(figsize=(12, 6))

sns.barplot(
    x=top_cities.values,
    y=top_cities.index
)

plt.title("Top 10 Cities by Number of Restaurants")
plt.xlabel("Number of Restaurants")
plt.ylabel("City")
plt.tight_layout()

plt.savefig("top_10_cities.png")
plt.show()

# 7. Visualize Top 10 Cuisines
plt.figure(figsize=(12, 6))

sns.barplot(
    x=top_cuisines.values,
    y=top_cuisines.index
)

plt.title("Top 10 Cuisines by Number of Restaurants")
plt.xlabel("Number of Restaurants")
plt.ylabel("Cuisine")
plt.tight_layout()

plt.savefig("top_10_cuisines.png")
plt.show()

# 8. Completion Message
print("\nDescriptive Analysis Completed!")

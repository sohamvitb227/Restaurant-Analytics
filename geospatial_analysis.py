
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium

from folium.plugins import FastMarkerCluster, HeatMap


# ==========================================
# 1. LOAD DATASET
# ==========================================

df = pd.read_csv("Dataset/restaurant_dataset.csv")

print("Dataset Loaded Successfully!")
print("Total Restaurants:", len(df))


# ==========================================
# 2. CLEAN GEOGRAPHICAL DATA
# ==========================================

df["Latitude"] = pd.to_numeric(df["Latitude"], errors="coerce")
df["Longitude"] = pd.to_numeric(df["Longitude"], errors="coerce")
df["Country Code"] = pd.to_numeric(df["Country Code"], errors="coerce")
df["Aggregate rating"] = pd.to_numeric(
    df["Aggregate rating"], errors="coerce"
)

geo_df = df.dropna(
    subset=["Latitude", "Longitude"]
).copy()

geo_df = geo_df[
    (geo_df["Latitude"].between(-90, 90)) &
    (geo_df["Longitude"].between(-180, 180))
]

print("\nRestaurants with valid coordinates:", len(geo_df))


# ==========================================
# 3. INTERACTIVE RESTAURANT LOCATION MAP
# ==========================================

map_center = [
    geo_df["Latitude"].median(),
    geo_df["Longitude"].median()
]

restaurant_map = folium.Map(
    location=map_center,
    zoom_start=5,
    tiles="OpenStreetMap"
)

locations = geo_df[
    ["Latitude", "Longitude"]
].values.tolist()

FastMarkerCluster(locations).add_to(restaurant_map)

restaurant_map.save("restaurant_locations_map.html")

print("\nInteractive restaurant location map saved!")


# ==========================================
# 4. INDIA MAP WITH STATE BOUNDARIES
#    AND RESTAURANT DENSITY HEATMAP
# ==========================================

# Country Code 1 represents India

india_df = geo_df[
    geo_df["Country Code"] == 1
].copy()

# Create map using OpenStreetMap
india_map = folium.Map(
    location=[22.5, 82.0],
    zoom_start=5,
    tiles="OpenStreetMap"
)

# Prepare restaurant coordinates
heat_data = india_df[
    ["Latitude", "Longitude"]
].values.tolist()

# Add restaurant density heatmap
HeatMap(
    heat_data,
    radius=15,
    blur=20,
    min_opacity=0.4
).add_to(india_map)

# Add Indian state boundaries from GeoJSON
folium.GeoJson(
    "Dataset/india-regions.geojson",
    name="Indian State Boundaries",
    style_function=lambda feature: {
        "color": "black",
        "weight": 1.5,
        "fillOpacity": 0
    }
).add_to(india_map)

# Add layer control
folium.LayerControl().add_to(india_map)

# Save map
india_map.save("restaurant_density_heatmap.html")

print("\nIndia density heatmap with state boundaries saved!")


# ==========================================
# 5. TOP 10 CITIES BY RESTAURANT COUNT
# ==========================================

print("\nTOP 10 CITIES BY RESTAURANT COUNT")

city_counts = df["City"].value_counts().head(10)

print(city_counts)

plt.figure(figsize=(12, 6))

sns.barplot(
    x=city_counts.values,
    y=city_counts.index
)

plt.title("Top 10 Cities by Restaurant Count")
plt.xlabel("Number of Restaurants")
plt.ylabel("City")

plt.tight_layout()
plt.savefig("geospatial_city_distribution.png")
plt.show()


# ==========================================
# 6. COUNTRY-WISE RESTAURANT DISTRIBUTION
# ==========================================

print("\nCOUNTRY-WISE RESTAURANT DISTRIBUTION")

country_counts = df["Country Code"].value_counts()

print(country_counts)

country_counts.to_csv(
    "geospatial_country_distribution.csv"
)


# ==========================================
# 7. GEOGRAPHICAL SCATTER PLOT
# ==========================================

plt.figure(figsize=(12, 7))

scatter = plt.scatter(
    india_df["Longitude"],
    india_df["Latitude"],
    c=india_df["Aggregate rating"],
    cmap="viridis",
    alpha=0.6,
    s=15
)

plt.colorbar(
    scatter,
    label="Aggregate Rating"
)

plt.title("Restaurant Locations Across India")
plt.xlabel("Longitude")
plt.ylabel("Latitude")

plt.tight_layout()
plt.savefig("restaurant_geographical_distribution.png")
plt.show()


# ==========================================
# 8. LOCATION AND RATING CORRELATION
# ==========================================

# Exclude restaurants with rating 0
rated_df = india_df[
    india_df["Aggregate rating"] > 0
].copy()

print("\nPEARSON CORRELATION")

correlation = rated_df[
    ["Latitude", "Longitude", "Aggregate rating"]
].corr(method="pearson")

print(correlation)

print("\nSPEARMAN CORRELATION")

spearman = rated_df[
    ["Latitude", "Longitude", "Aggregate rating"]
].corr(method="spearman")

print(spearman)

correlation.to_csv(
    "location_rating_correlation.csv"
)


# ==========================================
# 9. AVERAGE RATING BY CITY
# ==========================================

city_analysis = (
    rated_df.groupby("City")
    .agg(
        Restaurant_Count=("Aggregate rating", "count"),
        Average_Rating=("Aggregate rating", "mean")
    )
    .sort_values(
        "Restaurant_Count",
        ascending=False
    )
)

print("\nCITY-WISE AVERAGE RATINGS")

print(city_analysis.head(10).round(2))

city_analysis.to_csv(
    "city_rating_analysis.csv"
)


# ==========================================
# 10. VISUALIZE AVERAGE RATING BY CITY
# ==========================================

top_city_ratings = city_analysis.head(10).sort_values(
    "Average_Rating",
    ascending=False
)

plt.figure(figsize=(12, 6))

sns.barplot(
    data=top_city_ratings.reset_index(),
    x="Average_Rating",
    y="City"
)

plt.title("Average Restaurant Rating by Top 10 Cities")
plt.xlabel("Average Rating")
plt.ylabel("City")

plt.tight_layout()

plt.savefig("average_rating_by_city_geospatial.png")
plt.show()


# ==========================================
# 11. COMPLETION
# ==========================================

print("\n====================================")
print("GEOSPATIAL ANALYSIS COMPLETED!")
print("====================================")

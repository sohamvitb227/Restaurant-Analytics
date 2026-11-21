# 🍽️ Restaurant Analytics Dashboard

An end-to-end **Restaurant Data Analysis and Machine Learning Project** that explores restaurant trends, customer preferences, geographical distribution, and rating patterns. The project also includes an interactive web dashboard with a restaurant rating prediction feature.

Developed as part of the **Cognifyz Technologies Internship**.

---

## 📌 Project Overview

The Restaurant Analytics Dashboard uses Python, data analysis, visualization, and machine learning techniques to extract meaningful insights from restaurant data.

The project focuses on understanding:

- Restaurant distribution across cities and countries.
- Popular cuisines and customer preferences.
- Restaurant ratings and pricing patterns.
- Relationship between restaurant features and aggregate ratings.
- Geographical concentration of restaurants.
- Predicting restaurant ratings using machine learning models.

## ✨ Key Features

### 1. Data Exploration
- Dataset structure and statistical analysis.
- Missing value detection and handling.
- Aggregate rating distribution.
- Identification of important numerical and categorical features.

### 2. Descriptive Analysis
- Country-wise restaurant distribution.
- Top 10 cities by restaurant count.
- Most popular cuisines.
- Statistical summaries of numerical columns.

### 3. Data Visualization
- Restaurant rating distribution.
- Average ratings across cities.
- Price range versus restaurant ratings.
- Table booking and online delivery analysis.
- Correlation heatmap.

### 4. Geospatial Analysis
- Interactive restaurant location map.
- India restaurant density heatmap.
- State boundary visualization.
- City-wise restaurant distribution.
- Analysis of geographical coordinates and restaurant ratings.

### 5. Customer Preference Analysis
- Identification of popular cuisines.
- Cuisine-wise restaurant counts.
- Average ratings by cuisine.
- Customer voting pattern analysis.

### 6. Feature Engineering
- Restaurant name and address length.
- Cuisine count.
- Handling missing cuisine values.
- Encoding categorical features.
- Price range categorization.

### 7. Predictive Modelling
Implemented and compared three machine learning algorithms:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor

Model performance is evaluated using:
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

The Random Forest model achieved the best performance among the three models on the evaluated test split.

### 8. Interactive Web Dashboard
- Restaurant analytics dashboard built using Flask.
- Visual representation of analytical findings.
- Interactive restaurant rating prediction.
- User input for price range, cost, votes, table booking and online delivery.

---

## 🛠️ Technologies Used

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Data Analysis | Pandas, NumPy |
| Data Visualization | Matplotlib, Seaborn |
| Geospatial Visualization | Folium |
| Machine Learning | Scikit-learn |
| Web Framework | Flask |
| Frontend | HTML, CSS, JavaScript |
| Development Environment | VS Code |

## 📂 Project Structure

```text
Restaurant_Analysis/
│
├── Dataset/
│   ├── restaurant_dataset.csv
│   └── india-regions.geojson
│
├── Data_Visualization/
│   ├── data_visualization.py
│   └── visualization charts
│
├── Customer_pref_analysis/
│   ├── customer_preference_analysis.py
│   ├── customer_preference_dataset.csv
│   └── visualization charts
│
├── Feature_Engineering/
│   ├── feature_engineering.py
│   └── engineered_restaurant_dataset.csv
│
├── Predictive_Modelling/
│   ├── predictive_model.py
│   ├── predict_restaurant.py
│   └── model_comparison.csv
│
├── Website/
│   ├── index.html
│   └── charts/
│
├── app.py
├── data_exploration.py
├── descriptive_analysis.py
├── geospatial_analysis.py
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/Restaurant-Analytics.git
```

### 2. Navigate to the Project Directory

```bash
cd Restaurant-Analytics
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install pandas numpy matplotlib seaborn scikit-learn flask folium
```

### 5. Run the Analysis Scripts

```bash
python data_exploration.py
python descriptive_analysis.py
python geospatial_analysis.py
```

Other analysis scripts are available in their respective folders.

### 6. Launch the Web Dashboard

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

### 7. View the Geospatial Heatmap

After running the geospatial analysis:

```bash
python -m http.server 8000
```

Open:

```text
http://localhost:8000/restaurant_density_heatmap.html
```

---

## 📊 Machine Learning Model Comparison

The following results were obtained from the evaluated test dataset:

| Model | MAE | RMSE | R² Score |
|---|---:|---:|---:|
| Linear Regression | 1.0751 | 1.2948 | 0.2634 |
| Decision Tree | 0.2277 | 0.3505 | 0.9460 |
| Random Forest | 0.2149 | 0.3307 | 0.9519 |

**Best performing model:** Random Forest Regressor.

*Note: These are results from the current train-test evaluation. Performance on unseen real-world data may differ.*

## 🔍 Key Analytical Observations

- New Delhi has the highest restaurant count in the dataset.
- North Indian cuisine is the most frequently represented cuisine.
- The dataset contains restaurants from multiple countries.
- Restaurant ratings vary across cities, cuisines and price ranges.
- Restaurant density is concentrated in particular geographical regions.
- Random Forest performed better than the other evaluated models on the test split.

## 🚀 Future Improvements

- Deploy the dashboard online.
- Add interactive filters for cities, cuisines and price ranges.
- Improve model generalization through further feature selection and validation.
- Integrate more advanced geospatial visualizations.
- Add interactive charts and downloadable analytical reports.

## 👨‍💻 Author

**Soham Das**

B.Tech – Computer Science and Engineering (Core)

VIT Bhopal University

---

⭐ If you find this project interesting, feel free to explore the repository!

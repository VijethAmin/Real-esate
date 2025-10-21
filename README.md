# 🏡 Bengaluru House Price Prediction - ML Web App

## 🌟 Overview

This project aims to predict house prices in Bengaluru using machine learning, based on features like area (sqft), number of bedrooms, bathrooms, and location. The final solution is deployed as a web app using Flask.

---

## 📊 Dataset Used

* **Name:** Bengaluru House Data
* **Source:** [Kaggle](https://www.kaggle.com/datasets/amitabhajoy/bengaluru-house-price-data)
* **Entries:** \~13,320
* **Main Features:** `location`, `size`, `total_sqft`, `bath`, `price`

---

## ⚖️ Tools & Technologies

| Category         | Tools/Libraries                                          |
| ---------------- | -------------------------------------------------------- |
| Language         | Python                                                   |
| Data Handling    | Pandas, NumPy                                            |
| Visualization    | Matplotlib, Seaborn                                      |
| Machine Learning | Scikit-learn (Linear Regression, Random Forest), XGBoost |
| Model Saving     | Joblib                                                   |
| Web Framework    | Flask                                                    |
| Frontend         | HTML, Bootstrap (optional)                               |

---

## 🪜 Data Preprocessing Steps

1. **Dropped unnecessary columns:** `area_type`, `availability`, `society`, `balcony`
2. **Cleaned missing values**
3. **Converted total\_sqft** (e.g., "2100-2850" → average)
4. **Created derived features:**

   * `bhk` from `size`
   * `price_per_sqft`
5. **Removed outliers:**

   * Properties with `total_sqft/bhk < 300`
   * Price per sqft outliers (location-wise)
   * Inconsistent BHK pricing within same location
6. **One-hot encoded** the `location` feature (rare ones grouped under 'other')

---

## 🤖 Model Comparison

| Model             | R² Score   | MAE (Lakhs) | RMSE (Lakhs) |
| ----------------- | ---------- | ----------- | ------------ |
| Linear Regression | **0.8646** | 19.24       | **40.02**    |
| Random Forest     | 0.8128     | **17.03**   | 47.05        |
| XGBoost           | 0.7694     | 19.15       | 52.22        |

### ✅ Final Model: **Linear Regression**

* Best R² score
* Simpler and generalizes well
* Less overfitting vs tree models

---

## 💻 Web Application (Flask)

### Features:

* User inputs: total_sqft, bath, bhk, and location via form
* Model input vector created dynamically with one-hot encoding
* Predictions are displayed in UI
* Errors and negative predictions handled safely

### Files:

* `app.py`: Flask backend logic
* `index.html`: Frontend form (with dropdown for locations)
* `bengaluru_price_model.pkl`: Trained model file
* `model_columns.pkl`: Columns used for input encoding

---

## 🚀 Deployment Flow

1. User fills form on web page
2. Flask receives and processes input
3. Trained model makes prediction
4. Price is returned and shown

---

## 💡 Key Highlights

* End-to-end ML pipeline: data cleaning → training → deployment
* Cleaned and engineered structured data for better accuracy
* Model safely handles unknown or missing input cases
* Linear regression outperformed complex models due to robust preprocessing

---

## 🚀 Future Improvements

* Add features like `furnishing_status`, `availability`
* Perform hyperparameter tuning with `GridSearchCV`
* Experiment with LightGBM, CatBoost
* Deploy using Render/Streamlit/Heroku

---
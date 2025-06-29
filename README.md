# 🔥 Algerian Forest Fire Prediction with Flask + ML Pipeline

Predict the burned area of Algerian forest fires using a machine learning model powered by a **Scikit-learn pipeline** (StandardScaler → LinearRegression) and served through a lightweight **Flask API**.

---

## 📁 Project Overview

This project focuses on deploying a machine learning regression model trained on the **Algerian Forest Fire dataset**. It uses:

- 🔄 **Scikit-learn Pipeline**: `StandardScaler` → `LinearRegression`
- ⚙️ **Flask API** to serve predictions
- 🧪 Simple input via JSON for model testing
- 📊 Based on the real Algerian forest fires dataset

---

## 📦 Dataset Summary

> The Algerian Forest Fire Dataset includes 244 records (122 for each of two regions: Bejaia and Sidi Bel-Abbes) with meteorological and fire-related features.

**Features include:**
- Temperature
- RH (Relative Humidity)
- Ws (Wind Speed)
- Rain
- FFMC, DMC, DC, ISI (Fire weather indices)
- Classes: Fire or Not (for classification) — not used here for regression
-region : Bejaia Region Dataset(denotes by 0) and  Sidi-Bel Abbes Region Dataset(denoted by 1)

📌 Target variable: **Area** (burned area in hectares)

---

## 🧠 Model Pipeline

```text
[Input Features] ─▶ StandardScaler ─▶ LinearRegression ─▶ [Predicted Burned Area]

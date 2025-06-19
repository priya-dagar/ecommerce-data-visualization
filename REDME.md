# 📊 E-Commerce Retail Sales - Exploratory Data Analysis (EDA)

Welcome to the Exploratory Data Analysis project on a real-world e-commerce dataset. This project demonstrates how to transform raw transactional data into meaningful business insights through data cleaning, visualization, and storytelling using Python.

---

## 📁 Dataset Information

- **Source**: UCI Machine Learning Repository / Kaggle (Online Retail Dataset)
- **Records**: ~500,000 rows
- **Fields**:
  - `InvoiceNo`: Transaction ID
  - `StockCode`: Product ID
  - `Description`: Product description
  - `Quantity`: Items purchased
  - `InvoiceDate`: Timestamp of transaction
  - `UnitPrice`: Price per item
  - `CustomerID`: Unique customer identifier
  - `Country`: Country of customer

---

## 🎯 Objective

The goal of this project is to explore the sales data and answer business-relevant questions such as:
- Which products generate the most revenue?
- Are there seasonal patterns in customer purchasing behavior?
- What is the relationship between product price and demand?
- Which countries contribute most to sales?
- Are there any anomalies or outliers in pricing or transactions?

---

## 🛠️ Tech Stack & Tools

- **Language**: Python
- **Libraries**: 
  - `pandas` – data manipulation
  - `matplotlib`, `seaborn` – data visualization
- **IDE**: Jupyter Notebook

---

## 📂 Project Structure

ecommerce-data-visualization/
├── data/
│ └── data.csv # Raw dataset
├── notebooks/
│ └── eda_report.ipynb # Full analysis notebook with commentary
├── visuals/
│ └── *.png # Saved charts and plots
├── src/
│ ├── data_cleaning.py # Script for loading & cleaning data
│ └── visualization_helpers.py# Modular plotting functions
├── requirements.txt # Python dependencies
└── README.md # This file


---

## 📊 Key Visualizations

- 📦 **Top 10 Products by Revenue**
- 🌍 **Top 10 Countries by Sales**
- 📈 **Monthly Sales Trends**
- 💸 **Unit Price vs Quantity (Demand)**
- ⚠️ **Outlier Detection via Boxplot**

Each visual is saved inside the `/visuals` folder and embedded in the notebook.

---

## 📌 Insights Summary

| Insight | Business Action |
|--------|-----------------|
| 🚀 Top-selling products identified | Focus on bundling and upselling |
| 📅 Holiday peaks in Nov–Dec | Stock up before peak seasons |
| 🌍 UK dominates revenue | Explore expansion to top other countries |
| 🧾 Outliers in price or volume | Review bulk transactions or errors |
| 🎯 Low-priced products sell more | Consider tiered pricing strategies |

---

## 🚀 How to Run

1. Clone this repo:
   ```bash
   git clone https://github.com/priya-dagar/ecommerce-data-visualization.git
   cd ecommerce-data-visualization

2. Install dependencies:

pip install -r requirements.txt

3. Launch Jupyter Notebook:

jupyter notebook notebooks/eda_report.ipynb

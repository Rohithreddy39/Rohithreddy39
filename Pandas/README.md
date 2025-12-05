# 📊 Sales Analytics Project (Python + Pandas)

This project performs a complete **end-to-end data analysis** of a simulated sales dataset using **Pandas**, **NumPy**, and **Matplotlib/Seaborn**.  
It demonstrates data cleaning, feature engineering, time-series analysis, pivot tables, and business insights — a real-world analytics workflow used by Data Analysts and BI teams.

---

## 🚀 Project Objectives

- Generate a realistic sales dataset  
- Clean and validate data  
- Engineer business features (profit, revenue categories, etc.)  
- Perform exploratory data analysis (EDA)  
- Analyze revenue, profit, and product performance  
- Build pivot tables and heatmaps  
- Visualize trends  
- Export cleaned and summarized results  

---

## 🛠️ Technologies Used

- **Python 3**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **Seaborn**
- **Jupyter Notebook / VS Code**

---

## 📁 Dataset Description

The dataset contains 300 rows of sales transactions from  
**Jan 2024 – Mar 2024**, including:

| Column        | Description |
|--------------|-------------|
| Date          | Transaction date |
| Region        | North, South, East, West |
| Product       | Laptop, Phone, Tablet, Headphones, Camera |
| Units_Sold    | Quantity sold |
| Unit_Price    | Price per unit |
| Category      | Electronics / Accessories |
| Revenue       | Units_Sold × Unit_Price |
| Profit        | (Unit Price − Cost) × Units Sold |
| Profit_Margin | Profit as % of Revenue |
| Month_Year    | Period for time-series |
| Week          | ISO Week |

---

## 🧹 Data Cleaning

- Removed duplicates  
- Validated datatypes  
- Checked for outliers  
- Ensured revenue formula consistency  
- Normalized text formats  
- Added time-based columns (Year, Month, Weekday, Month_Year)

---

## 🧮 Feature Engineering

- Profit  
- Profit Margin (%)  
- Revenue Category (Low / Medium / High)  
- Price Category (Low / Mid / High)  
- High Sales Day flag  
- Month-Year grouping  

---

## 📊 Key Business Insights

### **Regional Performance**
- Identified best and worst performing regions based on total revenue.

### **Product Performance**
- Ranked products by total revenue and units sold.

### **Category Profitability**
- Electronics vs Accessories margin comparison.

### **Monthly Trends**
- Month-over-month sales trend analysis.

### **Weekly Insights**
- Weekly revenue peaks indicating seasonal or campaign-driven behavior.

---

## 📈 Visualizations Included

- Revenue by Region  
- Revenue by Product  
- Profit by Category  
- Monthly Revenue Trend  
- Heatmap (Region × Product)  
- Units Sold Histogram  
- Revenue Boxplot by Category  

---

## 💾 Exports

Generated files:

- `sales_analytics_cleaned.csv`  
- `sales_analytics_cleaned.xlsx`  
- `sales_analytics_report.xlsx`  

---

## 🧩 How to Run This Project

```bash
pip install pandas numpy matplotlib seaborn
python sales_analytics_project.py
```

---

## ⭐ Future Enhancements

- Forecasting (Prophet / ARIMA)
- Tableau dashboard
- Streamlit deployment

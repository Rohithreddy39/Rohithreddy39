📊 Sales Analytics Project (Python + Pandas)

This project performs a complete end-to-end data analysis of a simulated sales dataset using Pandas, NumPy, and Matplotlib/Seaborn.
It demonstrates data cleaning, feature engineering, time-series analysis, pivot tables, and business insights — a real-world analytics workflow used by Data Analysts and BI teams.

🚀 Project Objectives

1.Generate a realistic sales dataset
2.Clean and validate data
3.Engineer business features (profit, revenue categories, etc.)
4.Perform exploratory data analysis (EDA)
5.Analyze revenue, profit, and product performance
6.Build pivot tables and heatmaps
7.Visualize trends
8.Export cleaned and summarized results

🛠️ Technologies Used

-->Python 3
-->Pandas
-->NumPy
-->Matplotlib
-->Seaborn
-->Jupyter Notebook / VS Code

📁 Dataset Description

The dataset contains 300 rows of sales transactions from
Jan 2024 – Mar 2024, including:

Column	Description
Date	Transaction date
Region	North, South, East, West
Product	Laptop, Phone, Tablet, Headphones, Camera
Units_Sold	Quantity sold
Unit_Price	Price per unit
Category	Electronics / Accessories
Revenue	Units_Sold × Unit_Price
Profit	(Unit Price − Cost) × Units Sold
Profit_Margin	Profit as % of Revenue
Month_Year	Period for time-series
Week	ISO Week

🧹 Data Cleaning

Removed duplicates

Validated datatypes

Checked for outliers

Ensured revenue formula consistency

Normalized text formats

Added time-based columns (Year, Month, Weekday, Month_Year)

🧮 Feature Engineering

Profit

Profit Margin (%)

Revenue Category (Low / Medium / High)

Price Category (Low / Mid / High)

High Sales Day flag

Month-Year grouping

📊 Key Business Insights
1️⃣ Regional Performance

The highest-revenue region: (replace with your result)

The lowest-revenue region: (replace)

Indicates strongest market presence in ___.

2️⃣ Product Performance

Best-selling product: (replace)

Weakest-selling product: (replace)

Electronics dominate overall revenue.

3️⃣ Category Profitability

Electronics contributed (x%) of total profit.

Accessories show lower but stable margins.

4️⃣ Monthly Trends

Highest revenue month: (replace)

Sales trend: increasing / decreasing / stable.

5️⃣ Weekly Insights

Top-performing week number: (replace)

Suggests periodic demand peaks.

📈 Visualizations

Charts generated:

Revenue by Region

Revenue by Product

Profit by Category

Monthly Revenue Trend (Line Plot)

Revenue Heatmap (Region × Product)

Units Sold Histogram

Category Revenue Boxplot

💾 Exports

Generated:

sales_analytics_cleaned.csv

sales_analytics_cleaned.xlsx

sales_analytics_report.xlsx

🧩 How to Run This Project
pip install pandas numpy matplotlib seaborn
python sales_analytics_project.py

⭐ Future Enhancements

Add forecasting (Prophet / ARIMA)

Build Tableau dashboard

Deploy as a Streamlit app

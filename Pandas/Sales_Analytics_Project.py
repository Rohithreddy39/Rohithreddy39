import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


#1.Data Creation (300)
np.random.seed(10)

dates=pd.date_range(start='2024-01-01', end='2024-03-31',freq='D')
regions=['North','South','East','West']
products=['Laptop','Tablet','Phone','Headphones','Camera']

categories={
    'Laptop':'Electronics',
    'Tablet': 'Electronics',
    'Phone': 'Electronics',
    'Headphones': 'Accessories',
    'Camera': 'Electronics'
}

data={
    'Date':np.random.choice(dates,300),
    'Region':np.random.choice(regions,300),
    'Product':np.random.choice(products,300),
    'Units_Sold':np.random.randint(1,20,300),
    'Unit_Price':np.random.randint(100,1500,300)
}

df=pd.DataFrame(data)
df['Category']=df['Product'].map(categories)
df['Revenue']=df['Units_Sold']*df['Unit_Price']


######################################

#2.Data Exploration(EDA)

#view first and last rows
print(df.head())
print(df.tail())

#view Dataset shape
print(df.shape)

#Column info(datatypes,null counts)
print(df.info())

#summary statistics for numeric columns
print(df.describe())

#checking missing values
print(df.isna().sum())

#unique values in each column
print(df['Region'].unique())
print(df['Product'].unique())
print(df['Category'].unique())

#check duplicates
print(df.duplicated().sum())

####################################
print("####################################")

#3.Data Cleaning & Validation

#Validate Datatypes
print(df[df['Units_Sold'] <= 0])
print(df[df['Unit_Price'] <= 0])


#Check for outliers
#we are looking for extremely high or low revenue.
print(df[['Units_Sold','Unit_Price','Revenue']].describe())

#check for categorical Consistency
print(df.groupby('Category')['Product'].unique())

#Add a sanity check: Revenue formula
print(df['Units_Sold']*df['Unit_Price']==df['Revenue'])


#Normalize text columns
df['Region']=df['Region'].str.title()
df['Product']=df['Product'].str.title()
df['Category']=df['Category'].str.title()

#Add useful time columns
df['Year']=df['Date'].dt.year
df['Month']=df['Date'].dt.month
df['MonthName']=df['Date'].dt.month_name()
df['Week']=df['Date'].dt.isocalendar().week
df['Day']=df['Date'].dt.day



print("####################################")
print("####################################")

#4.Feature Engineering

#create profit(Assume 60% cost price)
df['Cost']=df['Unit_Price']*0.60
df['Profit']=(df['Unit_Price']-df['Cost'])*df['Units_Sold']

#profit margin
df['Profit_Margin']=(df['Profit']/df['Revenue'])*100

#Revenue Category(Binning)
df['Revenue_Category']=pd.cut(df['Revenue'],bins=[0,4000,10000,float('inf')],labels=['Low','Medium','High'])

#High Sales Day Flag
df['High_Sales_day']=np.where(df['Revenue']>df['Revenue'].median(),'Yes','No')

#Unit Price Category
df['Price_Category']=pd.cut(df['Unit_Price'],bins=[0,500,1000,2000],labels=['Low Price','Mid Price','High Price'])


#Month-Year Column
df['Month_Year']=df['Date'].dt.to_period('M').astype(str)


#Weekday Name
df['Weekday']=df['Date'].dt.day_name()

print(df.head())


print("####################################")
print("####################################")


#5 — SALES ANALYSIS & BUSINESS INSIGHTS

#total Revenue by Region
revenue_by_region=df.groupby('Region')['Revenue'].sum()
print(revenue_by_region)
#total revenue by Product
revenue_by_product=df.groupby('Product')['Revenue'].sum()
print(revenue_by_product)

#Total Profit by Category
profit_by_caegory=df.groupby('Category')['Profit'].sum()
print(profit_by_caegory)

#Average Units sold by Product
avg_units_sold=df.groupby('Product')['Units_Sold'].mean()
print(avg_units_sold)

#Top 5 Highest Revenue Transactions
top5 = df.nlargest(5, 'Revenue')
print(top5)

#Monthly Revenue (Time-Series)
monthly_revenue = df.groupby('Month_Year')['Revenue'].sum()
print(monthly_revenue)

#Daily Average Revenue
daily_avg = df.groupby('Date')['Revenue'].mean()
print(daily_avg)

#Pivot Table: Revenue by Region × Product
pivot_region_product=df.pivot_table(values='Revenue',index='Region',columns='Product',aggfunc='sum',fill_value=0)
print(pivot_region_product)

#Pivot Table: Profit by Category × Region
pivot_profit = df.pivot_table(
    values='Profit',
    index='Category',
    columns='Region',
    aggfunc='sum',
    fill_value=0
)
print(pivot_profit)

#Best Performing Region (highest revenue)
best_region = df.groupby('Region')['Revenue'].sum().idxmax()
print("Best region:", best_region)

#Worst Performing Product (least revenue)
worst_product = df.groupby('Product')['Revenue'].sum().idxmin()
print("Worst product:", worst_product)

#Which Week Has Highest Revenue?
weekly_revenue = df.groupby('Week')['Revenue'].sum()
best_week = weekly_revenue.idxmax()
print("Best week number:", best_week)
print("Weekly revenue:", weekly_revenue[best_week])



#7 — VISUALIZATIONS (Matplotlib)

#Revenue by Region (Bar Chart)
revenue_by_region = df.groupby('Region')['Revenue'].sum()

plt.figure(figsize=(8,5))
plt.bar(revenue_by_region.index, revenue_by_region.values, color='skyblue')
plt.title("Total Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.show()

#Revenue by Product (Bar Chart)
revenue_by_product = df.groupby('Product')['Revenue'].sum()

plt.figure(figsize=(8,5))
plt.bar(revenue_by_product.index, revenue_by_product.values, color='orange')
plt.title("Total Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.show()

#Monthly Revenue Trend (Line Plot)
monthly_revenue = df.groupby('Month_Year')['Revenue'].sum()

plt.figure(figsize=(9,5))
plt.plot(monthly_revenue.index, monthly_revenue.values, marker='o')
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.grid(True)
plt.show()

#Profit by Category (Bar Chart)
profit_by_category = df.groupby('Category')['Profit'].sum()

plt.figure(figsize=(8,5))
plt.bar(profit_by_category.index, profit_by_category.values, color='green')
plt.title("Total Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.show()

#Heatmap: Revenue by Region × Product (Pivot Table)
pivot_rp = df.pivot_table(
    values='Revenue',
    index='Region',
    columns='Product',
    aggfunc='sum',
    fill_value=0
)

plt.figure(figsize=(10,6))
sns.heatmap(pivot_rp, annot=True, fmt=".0f", cmap="Blues")
plt.title("Revenue Heatmap (Region × Product)")
plt.show()

#Units Sold Distribution (Histogram)
plt.figure(figsize=(8,5))
plt.hist(df['Units_Sold'], bins=15, color='purple')
plt.title("Distribution of Units Sold")
plt.xlabel("Units Sold")
plt.ylabel("Frequency")
plt.show()

#Boxplot: Revenue by Category
plt.figure(figsize=(8,5))
sns.boxplot(data=df, x='Category', y='Revenue')
plt.title("Revenue Distribution by Category")
plt.show()

#8 — EXPORT FINAL DATASET (CSV + EXCEL)
#Export to CSV (recommended)
df.to_csv("sales_analytics_cleaned.csv", index=False)

#Export to Excel (optional, but great for dashboards)
df.to_excel("sales_analytics_cleaned.xlsx", index=False)

#Export summary sheets in Excel (pro-level)
with pd.ExcelWriter("sales_analytics_report.xlsx") as writer:
    df.to_excel(writer, sheet_name="Cleaned Data", index=False)
    df.describe().to_excel(writer, sheet_name="Summary Stats")
    revenue_by_region.to_excel(writer, sheet_name="Revenue by Region")
    revenue_by_product.to_excel(writer, sheet_name="Revenue by Product")
    profit_by_category.to_excel(writer, sheet_name="Profit by Category")


# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'D:\\Internship\\Amazon Data Analytics\\Amazon Sales data.csv'
data = pd.read_csv(file_path)

# 1. Data Preprocessing
data['Order Date'] = pd.to_datetime(data['Order Date'])  # Convert 'Order Date' to datetime format
data['Year'] = data['Order Date'].dt.year               # Extract Year for year-wise analysis
data['Month'] = data['Order Date'].dt.month             # Extract Month for month-wise analysis
data['Year_Month'] = data['Order Date'].dt.to_period('M') # Extract Year-Month for yearly-month-wise analysis

# 2. Calculations

# Total Sales and Total Profit
total_sales = data['Total Revenue'].sum()
total_profit = data['Total Profit'].sum()

# Average Profit Margin
average_profit_margin = (total_profit / total_sales) * 100

# Average Unit Price
average_unit_price = data['Unit Price'].mean()

# Highest Sales by Order Priority
sales_by_priority = data.groupby('Order Priority')['Total Revenue'].sum()
highest_sales_priority = sales_by_priority.idxmax()

# Bestseller Item Type
sales_by_item_type = data.groupby('Item Type')['Total Revenue'].sum()
bestseller_item_type = sales_by_item_type.idxmax()

# Mode of Channel with Maximum Sales
sales_by_channel = data.groupby('Sales Channel')['Total Revenue'].sum()
max_sales_channel = sales_by_channel.idxmax()

# Yearly Total Sales
yearly_sales = data.groupby('Year')['Total Revenue'].sum()

# Sales Trend: Month-wise, Year-wise, and Yearly-Month-wise
monthly_sales = data.groupby('Month')['Total Revenue'].sum()
yearly_month_sales = data.groupby('Year_Month')['Total Revenue'].sum()

# Sales and Profit by Region
sales_by_region = data.groupby('Region')['Total Revenue'].sum()
profit_by_region = data.groupby('Region')['Total Profit'].sum()

# 3. Output Results

# Print Results for reference
print(f"Total Sales: {total_sales}")
print(f"Total Profit: {total_profit}")
print(f"Average Profit Margin: {average_profit_margin:.2f}%")
print(f"Average Unit Price: {average_unit_price:.2f}")
print(f"Order Priority with Highest Sales: {highest_sales_priority}")
print(f"Bestseller Item Type: {bestseller_item_type}")
print(f"Sales Channel with Maximum Sales: {max_sales_channel}")
print("Yearly Sales:")
print(yearly_sales)
print("Sales by Region:")
print(sales_by_region)
print("Profit by Region:")
print(profit_by_region)
print("Monthly Sales Trend:")
print(monthly_sales)
print("Yearly-Month Sales Trend:")
print(yearly_month_sales)

# 4. Plotting

# Plot 1: Yearly Sales Trend
plt.figure(figsize=(10, 6))
yearly_sales.plot(kind='bar', color='skyblue')
plt.title('Yearly Sales Trend')
plt.xlabel('Year')
plt.ylabel('Total Sales ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('D:\\Internship\\sol1\\Yearly_Sales_Trend.png')
plt.show()

# Plot 2: Monthly Sales Trend (Aggregated across all years)
plt.figure(figsize=(10, 6))
monthly_sales.plot(kind='bar', color='orange')
plt.title('Monthly Sales Trend (Aggregated)')
plt.xlabel('Month')
plt.ylabel('Total Sales ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('D:\\Internship\\sol1\\Monthly_Sales_Trend.png')
plt.show()

# Plot 3: Yearly-Month Sales Trend
plt.figure(figsize=(10, 6))
yearly_month_sales.plot(kind='line', marker='o', color='green')
plt.title('Yearly-Month Sales Trend')
plt.xlabel('Year-Month')
plt.ylabel('Total Sales ($)')
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('D:\\Internship\\sol1\\Yearly_Month_Sales_Trend.png')
plt.show()

# 5. Detailed Visualizations

# Sales vs. Profit
plt.figure(figsize=(10, 6))
plt.bar(['Total Sales', 'Total Profit'], [total_sales, total_profit], color=['blue', 'green'])
plt.ylabel('Amount ($)')
plt.title('Total Sales vs. Total Profit')
plt.savefig('D:\\Internship\\sol1\\total_sales_vs_profit.png')
plt.show()

# Average Profit Margin
plt.figure(figsize=(6, 6))
plt.bar(['Average Profit Margin'], [average_profit_margin], color='purple')
plt.ylabel('Profit Margin (%)')
plt.title('Average Profit Margin')
plt.savefig('D:\\Internship\\sol1\\average_profit_margin.png')
plt.show()

# Average Unit Price
plt.figure(figsize=(6, 6))
plt.bar(['Average Unit Price'], [average_unit_price], color='orange')
plt.ylabel('Unit Price ($)')
plt.title('Average Unit Price')
plt.savefig('D:\\Internship\\sol1\\average_unit_price.png')
plt.show()

# Sales by Order Priority
plt.figure(figsize=(10, 6))
sales_by_priority.plot(kind='bar', color='teal')
plt.ylabel('Total Revenue ($)')
plt.title('Sales by Order Priority')
plt.savefig('D:\\Internship\\sol1\\sales_by_order_priority.png')
plt.show()

# Bestseller Item Type
plt.figure(figsize=(10, 6))
sales_by_item_type.plot(kind='bar', color='cyan')
plt.ylabel('Total Revenue ($)')
plt.title('Bestseller Item Type')
plt.savefig('D:\\Internship\\sol1\\bestseller_item_type.png')
plt.show()

# Maximum Sales Channel
plt.figure(figsize=(10, 6))
sales_by_channel.plot(kind='bar', color='magenta')
plt.ylabel('Total Revenue ($)')
plt.title('Sales Channel with Maximum Revenue')
plt.savefig('D:\\Internship\\sol1\\max_sales_channel.png')
plt.show()

# Yearly Total Sales
plt.figure(figsize=(12, 8))
yearly_sales.plot(kind='line', marker='o', color='red')
plt.ylabel('Total Sales ($)')
plt.title('Yearly Total Sales')
plt.savefig('D:\\Internship\\sol1\\yearly_total_sales.png')
plt.show()

# Sales by Region (Pie Chart)
plt.figure(figsize=(12, 8))
sales_by_region.plot(kind='pie', autopct='%1.1f%%', colors=plt.cm.Paired(range(len(sales_by_region))))
plt.title('Sales by Region')
plt.ylabel('')
plt.savefig('D:\\Internship\\sol1\\sales_by_region.png')
plt.show()

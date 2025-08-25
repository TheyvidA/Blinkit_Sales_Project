# Imports python libraries i need for this analysis
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Displays the data in the blinkit sales file
blinket_df = pd.read_csv('Blinkit_csv.csv')
pd.set_option('display.max_columns', 114)
pd.set_option('display.max_rows', 114)
print(blinket_df)

# Displays the top (5) data and the bottom (5) data in the blinkit sales file
print(blinket_df.head(5))
print(blinket_df.tail(5))

# Displays all the column names in the blinkit sales file
print(blinket_df.columns)

# Perform some Data Cleaning on the blinkit sales file
blinket_df['Item Fat Content'] = blinket_df['Item Fat Content'].replace({'LF':'Low Fat', 'low fat':'Low Fat', 'reg':'Regular'})
print(blinket_df['Item Fat Content'].unique())

# Check the total sales and the average sales
Total_sales = blinket_df['Sales'].sum()
print(Total_sales)
print(f"Total_Sales: ${Total_sales:,.0f}")

Avg_sales = blinket_df['Sales'].median()
print(Avg_sales)
print(f"Total_Sales: ${Avg_sales:,.0f}")

Item_Sold = blinket_df['Sales'].count()
print(Item_Sold)
print(f"Total_Sales: ${Item_Sold:,.0f}")

# Check the Average weight at the store
AvgWeight = blinket_df['Item Weight'].mean()
print(AvgWeight)
print(f"The Average Weight: {AvgWeight:,.0f}")

# Check the Average ratings for a customer
AvgRatings = blinket_df['Rating'].mean()
print(AvgRatings)
print(f"The Average Rating: {AvgRatings:,.0f}")

# Displays the pie chart in our Blinkit sales file
Sales_fat = blinket_df.groupby('Item Fat Content')['Sales'].sum()
plt.pie(Sales_fat, labels = Sales_fat.index,
        autopct = '%.1f%%',
        startangle = 90)
plt.title('Sales by Fat')
plt.axis('equal')
#plt.show()

# Displays the Bar chart for Total sales by item type

Sales_fat = blinket_df.groupby('Item Type')['Sales'].sum().sort_values(ascending=False)
plt.figure(figsize = (10, 6))
bars = plt.bar(Sales_fat.index, Sales_fat.values)
plt.xticks(rotation = -90)
plt.xlabel('Item Type')
plt.ylabel('Total Sales')
plt.title('Total_Sales By Item_Type')

for bar in bars:
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(),
             f'(bar.get_height():,.0f)', ha = 'center', va = 'bottom', fontsize=8)
plt.tight_layout()
plt.show()

# Displays the Stack Chart for the Fat content

Grouped = blinket_df.groupby(['Outlet Location Type', 'Item Fat Content'])['Sales'].sum().unstack()
Grouped = Grouped[['Regular', 'Low Fat']]
axis = Grouped.plot(kind = 'bar', figsize = (8, 5), title = 'Outlet Tier by Item Fat Content')
plt.xlabel('Outlet Location Tier')
plt.ylabel('Total Sales')
plt.legend(title = 'Item Fat Content')
plt.tight_layout()
plt.show()

# Displays the Pie Chart of Sales by outlet Size
Sales_BySize = blinket_df.groupby('Outlet Size')['Sales'].sum()
plt.figure(figsize=(4, 4))
plt.pie(Sales_BySize, labels = Sales_BySize.index, autopct = '%1.f%%', startangle = 90)
plt.title('Sales by Fat')
plt.tight_layout()
plt.show()
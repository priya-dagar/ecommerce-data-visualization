"""
📈 Visualization Functions for EDA
"""

import matplotlib.pyplot as plt
import seaborn as sns

def plot_top_products(df, save_path="visuals/sales_by_top_products.png"):
    top_products = df.groupby('Description')['TotalPrice'].sum().nlargest(10)
    top_products.plot(kind='bar', figsize=(10,6), title='Top 10 Products by Sales', color='skyblue')
    plt.ylabel("Total Sales")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()

def plot_monthly_sales(df, save_path="visuals/monthly_sales_trend.png"):
    monthly_sales = df.groupby('Month')['TotalPrice'].sum()
    monthly_sales.plot(kind='line', marker='o', figsize=(10,6), title='Monthly Sales Trend', color='green')
    plt.xlabel("Month")
    plt.ylabel("Sales Amount")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()

def plot_sales_by_country(df, save_path="visuals/sales_by_country.png"):
    country_sales = df.groupby('Country')['TotalPrice'].sum().nlargest(10)
    country_sales.plot(kind='bar', figsize=(10,6), title='Top 10 Countries by Sales', color='orange')
    plt.ylabel("Total Sales")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()

def plot_unitprice_vs_quantity(df, save_path="visuals/unitprice_vs_quantity.png"):
    plt.figure(figsize=(10,6))
    sns.scatterplot(data=df[df['UnitPrice'] < 100], x='UnitPrice', y='Quantity', alpha=0.6)
    plt.title("Unit Price vs Quantity")
    plt.xlabel("Unit Price")
    plt.ylabel("Quantity")
    plt.xlim(0, 100)
    plt.ylim(0, 100)
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()

def plot_boxplot_totalprice(df, save_path="visuals/boxplot_totalprice.png"):
    plt.figure(figsize=(10,6))
    sns.boxplot(x=df['TotalPrice'])
    plt.title("Outliers in Total Price")
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()

"""
📦 Data Cleaning Script for E-Commerce Dataset
"""

import pandas as pd

def load_data(path):
    """
    Load e-commerce transaction data from CSV.
    """
    df = pd.read_csv(path, encoding='ISO-8859-1')
    return df


def clean_data(df):
    """
    Clean and preprocess the dataset:
    - Convert 'InvoiceDate' to datetime
    - Create 'Month' and 'Year' columns
    - Create 'TotalPrice' column = Quantity * UnitPrice
    - Handle missing values (drop or fill)
    """
    df = df.copy()
    
    # Convert InvoiceDate to datetime
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    
    # Extract month and year
    df['Month'] = df['InvoiceDate'].dt.month
    df['Year'] = df['InvoiceDate'].dt.year
    
    # Create total price per transaction line
    df['TotalPrice'] = df['Quantity'] * df['UnitPrice']
    
    # Optional: drop rows with missing CustomerID
    df.dropna(subset=['CustomerID'], inplace=True)
    
    return df

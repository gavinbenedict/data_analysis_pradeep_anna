import pandas as pd
import sys
print(sys.executable)

def load_data(file_path):
    if file_path.endswith('.csv'):
        return pd.read_csv(file_path)
    elif file_path.endswith('.xlsx'):
        return pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file format. Use .csv or .xlsx.")

def summarize_columns(df):
    print("\nSummary statistics for each column:")
    print(df.describe(include='all'))

def high_value_customers(df):
    clv = df.groupby('customer_id')['retail_price'].sum().sort_values(ascending=False)
    print("\nTop 10 customers by lifetime value and their spending:")
    print(clv.head(10))
    return clv

def product_reviews_by_segment(df):
    avg_reviews = df.groupby(['product_name'])['review_star'].mean().sort_values(ascending=False)
    print("\nAverage product review by product:")
    print(avg_reviews)
    return avg_reviews

def marketing_channel_effectiveness(df):
    prof = df.groupby('referring_channel')['retail_price'].sum().sort_values(ascending=False)
    print("\nTotal revenue by referring channel:")
    print(prof)
    return prof

def mainstream_vs_niche(df):
    if 'product_name' in df.columns:
        premium_mask = df['product_name'].str.contains("Pro", case=False, na=False)
        premium_customers = df[premium_mask].groupby('customer_id')['retail_price'].sum()
        mainstream_customers = df[~premium_mask].groupby('customer_id')['retail_price'].sum()
        print(f"\nTotal spent by premium customers: {premium_customers.sum():.2f}")
        print(f"Total spent by mainstream customers: {mainstream_customers.sum():.2f}")
    else:
        print("\nColumn 'product_name' not found for premium/mainstream split.")

def product_penetration(df):
    if 'product_name' in df.columns:
        mainstream_mask = df['product_name'].str.contains("Go", case=False, na=False)
        mainstream_pct = mainstream_mask.sum() / len(df) * 100
        print(f"\nMainstream ('Go') products as a % of all sales: {mainstream_pct:.1f}%")
    else:
        print("\nColumn 'product_name' not found for niche/mainstream analysis.")

def analyze_dataset(file_path):
    df = load_data(file_path)
    summarize_columns(df)
    high_value_customers(df)
    product_reviews_by_segment(df)
    marketing_channel_effectiveness(df)
    mainstream_vs_niche(df)
    product_penetration(df)

analyze_dataset("/Users/gabeee/Data_analysis/dataa.csv")

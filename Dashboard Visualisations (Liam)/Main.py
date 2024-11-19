import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('data.csv')

# Convert 'Date' to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Function to plot total spending by category
def plot_spending_by_category(df):
    category_spending = df.groupby('Category')['Amount'].sum().sort_values(ascending=False)
    
    # Plot bar chart
    plt.figure(figsize=(10, 6))
    category_spending.plot(kind='bar', color='skyblue')
    plt.title('Total Spending by Category')
    plt.xlabel('Category')
    plt.ylabel('Amount ($)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Function to plot spending over time
def plot_spending_over_time(df):
    df.set_index('Date', inplace=True)
    daily_spending = df.resample('D')['Amount'].sum()
    
    # Plot line chart
    plt.figure(figsize=(10, 6))
    daily_spending.plot(kind='line', color='green')
    plt.title('Daily Spending Over Time')
    plt.xlabel('Date')
    plt.ylabel('Amount ($)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Function to plot spending distribution by category as a pie chart
def plot_spending_pie_chart(df):
    category_spending = df.groupby('Category')['Amount'].sum()
    
    # Plot pie chart
    plt.figure(figsize=(8, 8))
    category_spending.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=sns.color_palette("Set3", len(category_spending)))
    plt.title('Spending Distribution by Category')
    plt.ylabel('')
    plt.tight_layout()
    plt.show()

# Call functions to generate the graphs
plot_spending_by_category(df)
plot_spending_over_time(df)
plot_spending_pie_chart(df)

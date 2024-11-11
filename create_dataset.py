import pandas as pd
import numpy as np

# Generate a date range
date_range = pd.date_range(start='2024-01-01', periods=100, freq='D')

# Generate random sales and profit data
np.random.seed(0)  # For reproducibility
sales = np.random.randint(100, 1000, size=100)  # Random sales between 100 and 1000
profit = np.random.randint(10, 300, size=100)   # Random profit between 10 and 300

# Generate random categories
categories = ['Electronics', 'Clothing', 'Furniture', 'Toys', 'Groceries']
category_choices = np.random.choice(categories, size=100)

# Create a DataFrame
data = pd.DataFrame({
    'Date': date_range,
    'Sales': sales,
    'Profit': profit,
    'Category': category_choices
})

# Save the DataFrame to a CSV file
file_path = 'custom_dataset.csv'
data.to_csv(file_path, index=False)

print(f"Dataset saved as {file_path}")

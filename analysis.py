import pandas as pd

# Load the Iris dataset (replace with your own dataset if necessary)
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
df = pd.read_csv(url, names=column_names)

# Display the first few rows of the dataset
print(df.head())

# Explore the structure of the dataset
print("\nData Types:\n", df.dtypes)
print("\nMissing Values:\n", df.isnull().sum())

# Clean the dataset by filling or dropping missing values (if any)
# If there are any missing values, you can either fill them or drop them
df = df.fillna(df.mean())  # Fill missing values with the mean (if any)
# df = df.dropna()  # Alternatively, drop rows with missing values

# Basic statistics of the numerical columns
print("\nBasic Statistics:\n", df.describe())

# Perform groupings on the 'species' column and compute the mean of numerical columns
grouped = df.groupby('species').mean()
print("\nGrouped Data (Mean of Numerical Columns per Species):\n", grouped)

# Identify patterns or interesting findings from the analysis
# Example: Compare the sepal length for each species
print("\nSepal Length by Species:\n", grouped['sepal_length'])

import matplotlib.pyplot as plt
import seaborn as sns

# Set the style for better visuals
sns.set(style='whitegrid')

# Line Chart: Trend over time (if you have a time series, replace with actual data)
# For demonstration, let's assume we have a 'date' column and use 'sepal_length' over time.
# For this example, we'll simulate a time series.
df['date'] = pd.date_range(start='2020-01-01', periods=len(df), freq='D')  # Simulate dates
plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['sepal_length'], label='Sepal Length')
plt.title('Sepal Length Over Time')
plt.xlabel('Date')
plt.ylabel('Sepal Length (cm)')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Bar Chart: Comparison of numerical values across categories (average sepal length per species)
plt.figure(figsize=(10, 6))
sns.barplot(x='species', y='sepal_length', data=df)
plt.title('Average Sepal Length per Species')
plt.xlabel('Species')
plt.ylabel('Average Sepal Length (cm)')
plt.show()

# Histogram: Distribution of sepal lengths
plt.figure(figsize=(10, 6))
sns.histplot(df['sepal_length'], kde=True, bins=20)
plt.title('Distribution of Sepal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.show()

# Scatter Plot: Relationship between sepal length and petal length
plt.figure(figsize=(10, 6))
sns.scatterplot(x='sepal_length', y='petal_length', data=df, hue='species')
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species')
plt.show()

try:
    df = pd.read_csv('path_to_your_file.csv')  # Replace with your actual file path
except FileNotFoundError:
    print("File not found. Please check the file path.")
except pd.errors.ParserError:
    print("Error parsing the CSV file. Please check the file format.")

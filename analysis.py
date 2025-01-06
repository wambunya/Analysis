import pandas as pd

# Load the Iris dataset from sklearn for demonstration purposes
from sklearn.datasets import load_iris

# Convert the iris dataset to a pandas DataFrame
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target_names[iris.target]

# If you are using your own CSV, use:
# df = pd.read_csv('your_dataset.csv')

# Display the first few rows of the dataset
print(df.head())

# Check data types and missing values
print(df.info())

# Check for missing values
print(df.isnull().sum())

# Fill missing values with the mean of the column
df = df.fillna(df.mean())

# Or, if you want to drop rows with missing values
# df = df.dropna()

# Basic statistics of numerical columns
print(df.describe())

# Grouping by 'species' and calculating mean of numerical columns
grouped = df.groupby('species').mean()
print(grouped)

import matplotlib.pyplot as plt
import seaborn as sns

# 1. Line chart showing trends over time (Assuming you have a time-related column, but for now, we'll use an index)
# Example: Trend of Sepal Length (replace with a time-related column in your dataset)
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['sepal length (cm)'], label='Sepal Length')
plt.title('Sepal Length Over Time')
plt.xlabel('Index')
plt.ylabel('Sepal Length (cm)')
plt.legend()
plt.show()

# 2. Bar chart showing comparison of numerical value across categories (average petal length per species)
plt.figure(figsize=(10, 6))
sns.barplot(x='species', y='petal length (cm)', data=df)
plt.title('Average Petal Length per Species')
plt.xlabel('Species')
plt.ylabel('Average Petal Length (cm)')
plt.show()

# 3. Histogram of a numerical column (distribution of Sepal Width)
plt.figure(figsize=(10, 6))
sns.histplot(df['sepal width (cm)'], bins=15, kde=True)
plt.title('Distribution of Sepal Width')
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Frequency')
plt.show()

# 4. Scatter plot showing the relationship between two numerical columns (e.g., Sepal Length vs. Petal Length)
plt.figure(figsize=(10, 6))
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', data=df, hue='species')
plt.title('Sepal Length vs. Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species')
plt.show()


try:
    # Load dataset
    df = pd.read_csv('your_dataset.csv')  # Adjust for your dataset path
    
    # Inspect first few rows
    print(df.head())

except FileNotFoundError:
    print("Error: The file was not found. Please check the file path.")
except pd.errors.EmptyDataError:
    print("Error: The file is empty.")
except Exception as e:
    print(f"An error occurred: {e}")

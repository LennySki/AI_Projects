import pandas as pd

# URL of the dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
# Column names for the dataset
columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']


# Load the dataset into a pandas DataFrame
iris_data = pd.read_csv(url, names=columns)

# Print the first few rows of the DataFrame
print(iris_data.head())

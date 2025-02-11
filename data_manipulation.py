import pandas as pd

# Sample data creation
data = {
	'Name': ['John', 'Anna', 'Peter', 'Linda'],
	'Age': [28, 22, 34, 42],
	'City': ['New York', 'Paris', 'Berlin', 'London']
}

# Create DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print("Original DataFrame:")
print(df)

# Add a new column
df['Age Next Year'] = df['Age'] + 1

# Display the updated DataFrame
print("\nUpdated DataFrame with 'Age Next Year':")
print(df)

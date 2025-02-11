import pandas as pd

data = {
	'Age': [28, 22, 34, 42],
	'Name': ['John', 'Anna', 'Peter', 'Linda']
}

df = pd.DataFrame(data)

# Print the entire DataFrame to see your initial data
print("Original DataFrame:")
print(df)

# Filter to show only rows where Age is greater than 30
filtered_df = df[df['Age'] > 30]

# Print the filtered DataFrame
print("\Filtered DataFrame (Age > 30):")
print(filtered_df)

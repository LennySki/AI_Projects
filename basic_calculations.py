import pandas as pd

# Creating the DataFrame
data = {
	'Numbers': [1, 2, 3, 4, 5],
	'Square': [n**2 for n in range(1, 6)]
}
df = pd.DataFrame(data)

# Displaying the DataFrame
print(df)

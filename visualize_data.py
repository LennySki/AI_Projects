import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
	'Age' : [28, 22, 34, 42],
	'Name': ['John', 'Anna', 'Peter', 'Linda']
}
df = pd.DataFrame(data)

# Creating a bar chart
plt.figure(figsize=(8, 4))
plt.bar(df['Name'], df['Age'], color='blue')
plt.xlabel('Name')
plt.ylabel('Age')
plt.title('Age of Individuals')
plt.show()



import pandas as pd

# Load data
df = pd.read_csv("dataset.csv")
print(df.columns)

# 1. Average duration (convert milliseconds to minutes)
avg_duration = df ["duration_ms"].mean() / 60000
print(f"Average song duration: {avg_duration:.2f} minutes")

# 2. Artist with most tracks
top_artist = df["artists"].value_counts().idxmax()
print(f"Top artist: {top_artist}")

# 3. Correlation
correlation = df[["danceability", "energy"]].corr().iloc[0,1]
print(f"Correlation: {correlation:.2f}")

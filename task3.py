import pandas as pd
import numpy as np
df = pd.read_csv("data/trends_clean.csv")

print("Loaded data:", df.shape)
print("\nFirst 5 rows:")
print(df.head())
print("\nAverage score:", df["score"].mean())
print("Average comments:", df["num_comments"].mean())
scores = df["score"].to_numpy()

print("\n--- NumPy Stats ---")
print("Mean score:", np.mean(scores))
print("Median score:", np.median(scores))
print("Std deviation:", np.std(scores))
print("Max score:", np.max(scores))
print("Min score:", np.min(scores))
category = df["category"].value_counts().idxmax()
count = df["category"].value_counts().max()

print(f"\nMost stories in: {category} ({count} stories)")
row = df.loc[df["num_comments"].idxmax()]
print("\nMost commented story:", row["title"])
print("Comments:", row["num_comments"])

average_score = df["score"].mean()

df["engagement"] = df["num_comments"] / (df["score"] + 1)
df["is_popular"] = df["score"] > average_score


df.to_csv("data/trends_analysed.csv", index=False)

print("\nSaved to data/trends_analysed.csv")
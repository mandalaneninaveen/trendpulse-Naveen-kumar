import pandas as pd
import glob
file = glob.glob("data/trends_*.json")[0]
df = pd.read_json(file)

print("Loaded:", len(df))
df = df.drop_duplicates("post_id")
df = df.dropna(subset=["post_id", "title", "score"])
df["score"] = pd.to_numeric(df["score"])
df["num_comments"] = pd.to_numeric(df["num_comments"]).fillna(0).astype(int)
df["score"] = df["score"].astype(int)
df["title"] = df["title"].str.strip()
df = df[df["score"] >= 5]

print("After cleaning:", len(df))
df.to_csv("data/trends_clean.csv", index=False)

print("Saved", len(df), "rows to data/trends_clean.csv")
print("\nStories per category:")
print(df["category"].value_counts())
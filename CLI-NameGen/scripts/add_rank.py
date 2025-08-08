import json
import pandas as pd

#load Oxford Words
with open("C:\\Users\\m2mcgonigle\\dev\\CLI-NameGen\\filtered_oxford_words.json", "r", encoding="utf-8") as f:
    oxford_words = json.load(f)

#Load COCA Excel File
df = pd.read_excel("C:\\Users\\m2mcgonigle\\dev\\CLI-NameGen\\data\\""COCA-wordFrequency.xlsx")

df = df.rename(columns={
    "lemma" : "word",
    "PoS" : "pos"
})


#Clean and Prep COCA data
df["word"] = df["word"].str.lower()
df["pos"] = df["pos"].str.lower()
df = df[df["pos"].isin(["n","j","r"])]

pos_priority = {"j":0, "n":1, "r": 2}
df["pos_rank"] = df["pos"].map(pos_priority).fillna(999)

#Sort and Remove duplicate words, Keeping best PoS rank
df = df.sort_values(by=["word", "pos_rank", "rank"])
df = df.drop_duplicates(subset=["word"], keep=("first"))

#Create [word:rank] Dict
rank_lookup = {row["word"]: int(row["rank"]) for _, row in df.iterrows()}

#Attach Usage_Rank to Oxford Word List
matched = 0
for word in oxford_words:
    key = word["word"].lower()
    rank = rank_lookup.get(key)
    if rank is not None:
        word["usage_rank"] = rank
        matched += 1
    else:
        word["usage_rank"] = None

with open("C:\\Users\\m2mcgonigle\\dev\\CLI-NameGen\\data\\oxford_words_with_rank.json", "w", encoding="utf-8") as f:
    json.dump(oxford_words, f, indent=2)

print(f"Matched {matched} / {len(oxford_words)} Words to COCA")
print("saved: data/oxford_words_with_rank.json")
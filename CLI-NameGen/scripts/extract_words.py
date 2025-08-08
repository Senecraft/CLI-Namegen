import json 

with open("C:\\Users\\m2mcgonigle\\dev\\CLI-NameGen\\data\\Oxford5000full-word.json", "r", encoding="utf-8") as f:
    raw_data = json.load(f)

allowed_types = ["adjective", "noun"]

filtered = []
for entry in raw_data:
    value = entry.get("value", {})
    word_type = value.get("type", "").lower()
    if word_type in allowed_types:
        filtered.append({
            "word": value.get("word"),
            "pos" : word_type,
        })

print(f"total words kept: {len(filtered)}")

nouns = [w for w in filtered if w["pos"] == "noun"]
adjectives = [w for w in filtered if w["pos"] == "adjective"]

print(f"Nouns: {len(nouns)}")
print(f"Adjectives: {len(adjectives)}")

with open("filtered_oxford_words.json", "w", encoding="utf-8") as f:
    json.dump(filtered, f, indent=2)
from .word import Word
import json

with open("C:\\Users\\m2mcgonigle\\dev\\CLI-NameGen\\data\\oxford_words_with_rank.json", "r", encoding="utf-8") as f:
    raw_words = json.load(f)

word_objects = [
    Word(
        name=entry["word"],
        word_type=entry["pos"],
        usage_rank=int(entry.get("usage_rank")) if entry.get("usage_rank") is not None else None,
        #superlative=None #fill in later
    )
    for entry in raw_words
]

word_bank = {
    "noun": [],
    "adjective" : []
}

for word in word_objects:
    if word.word_type in word_bank:
        word_bank[word.word_type].append(word)

def load_word_bank():
    return word_bank      
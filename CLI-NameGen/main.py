import argparse
import random
from namegen.wordbank import load_word_bank
from namegen.generator import generate_base

bank = load_word_bank()
nouns = bank.get("noun", [])
adjs = bank.get("adjective", [])



name = generate_base(adjs, nouns, random,)


print(name)

#print(word_objects[:5])
#print(sum(1 for w in word_objects if w.usage_rank is None), "missing ranks")
#for word in word_objects:
#    if word.usage_rank is None:
#        print(word.name)
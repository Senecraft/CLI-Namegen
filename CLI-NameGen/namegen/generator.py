import random
from typing import Sequence, Callable, Optional
from .word import Word

#helpers
def _weight_from_rank(rank: Optional[int], alpha: float = 0.7) -> float:
    if rank is None:
        return 0.0001
    return (1.0/(rank ** alpha))

def _choose_weighted(words: Sequence[Word], rng: random.Random) -> Word:
    weights = [_weight_from_rank(w.usage_rank) for w in words]
    return rng.choices(words, weights=weights, k=1)[0]

def _cap(s: str) -> str:
    return s[:1].upper() + s[1:]

#API

def generate_base(adjs: Sequence[Word], nouns: Sequence[Word], rng: Optional[random.Random] = None,
                  joiner: str = "") -> str:
    rng = rng or random
    adj = _choose_weighted(adjs,rng)
    noun = _choose_weighted(nouns,rng)
    return f"{_cap(adj.name)}{joiner}{_cap(noun.name)}" if joiner == "" else f"{_cap(adj.name)}{joiner}{_cap(noun.name)}"
class Word:
    def __init__(self, name, word_type, usage_rank=None, superlative=None):
        self.name = name
        self.word_type = word_type
        self.usage_rank= usage_rank
        self.superlative = superlative


    def has_superlative(self):
        return self.superlative is not None
    
    def get_superlative(self):
        return self.superlative if self.superlative else self.name
    
    def __repr__(self):
        return self.name
    

        pass

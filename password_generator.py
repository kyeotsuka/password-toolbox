import string, secrets
from typing import List

def load_word_list(filepath: str) -> list[str]:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            # This line splits each line and takes only the word part
            words = [line.split('\t')[1].strip() for line in f]
            return words
    except FileNotFoundError:
        print(f"Error: Word list not found at '{filepath}'.")
        return []

class Generator:
    def __init__(self, length, use_upper=True, use_lower=True, use_numbers=True, use_symbols=True): 
        # this is stopping my function from working as it is requiring specific attributes, may you move it specifically to your function?
        self.length = length
        self.use_upper = use_upper
        self.use_lower = use_lower
        self.use_numbers = use_numbers
        self.use_symbols = use_symbols
        self.word_list = load_word_list("/eff_large_wordlist.txt")
        
    def generate_password(self):
        pool = ""
        if self.use_upper:
            pool += string.ascii_uppercase
        if self.use_lower:
            pool += string.ascii_lowercase
        if self.use_numbers:
            pool += string.digits
        if self.use_symbols:
            pool += string.punctuation
        
        if not pool:
            raise ValueError("No character sets selected.")
        
        return "".join(secrets.choice(pool) for _ in range(self.length))

    def generate_passphrase(self, num_words: int, separator: str = " ") -> str:
        """
        Generates a secure passphrase from the loaded word list.
        """
        if num_words < 3:
            raise ValueError(f"Number of words must be at least 3, but was {num_words}.")

        if not self.word_list:
            return "Error: Word list is not available."

        words = [secrets.choice(self.word_list) for _ in range(num_words)]
        
        return separator.join(words)
            

# below are for testing purposes
gen1 = Generator(15, use_upper=True, use_lower=True, use_numbers=True, use_symbols=True)
print(gen1.generate_password())
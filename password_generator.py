import string, secrets
from password import Password

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
    def __init__(self): 
        self.length = 0
        self.use_upper = True
        self.use_lower = True
        self.use_numbers = True
        self.use_symbols = True
        self.word_list = load_word_list("eff_large_wordlist.txt")
        
    def generate_password(self, length: int) -> Password:
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
        
        return Password("".join(secrets.choice(pool) for _ in range(length)))

    def generate_passphrase(self, num_words: int, separator: str = " ") -> Password:
        """
        Generates a secure passphrase from the loaded word list.
        """
        if num_words < 3:
            raise ValueError("Number of words must be at least 3.")

        if not self.word_list:
            raise RuntimeError("Error: Word list is not available.")

        words = [secrets.choice(self.word_list) for _ in range(num_words)]
        
        return Password(separator.join(words))
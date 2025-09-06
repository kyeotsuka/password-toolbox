from collections import Counter
import string

class Password:
    """A class to represent and analyse a password's properties."""
    
    def __init__(self, pw_string: str) -> None:
        if not pw_string:
            raise ValueError("Password cannot be empty.")
        
        self.pw_string = pw_string
        self.length = len(pw_string)
        
        self.strength = "Untested"
        self.alphabet_count = 0
        self.lowercase_count = 0
        self.uppercase_count = 0
        self.number_count = 0
        self.symbol_count = 0
        self.space_count = 0
        
        self.analyse()
        
    def __str__(self) -> str:
        """Returns the properties of the password string."""
        
        # The width is determined by the longest label, "Lowercase" (9 chars).
        label_width = 9
        
        return (f"{'Length':>{label_width}}: {self.length}\n"
                f"{'Alphabet':>{label_width}}: {self.alphabet_count}\n"
                f"{'Lowercase':>{label_width}}: {self.lowercase_count}\n"
                f"{'Uppercase':>{label_width}}: {self.uppercase_count}\n"
                f"{'Number':>{label_width}}: {self.number_count}\n"
                f"{'Space':>{label_width}}: {self.space_count}\n"
                f"{'Symbol':>{label_width}}: {self.symbol_count}\n"
                f"{'Strength':>{label_width}}: {self.strength}\n")

    def analyse(self) -> None:
        """Analyses the properties of the password string."""
        counts = Counter(self.pw_string)
    
        # Reset counts to zero before analysing
        self.alphabet_count = 0
        self.lowercase_count = 0
        self.uppercase_count = 0
        self.number_count = 0
        self.space_count = 0
        self.symbol_count = 0

        for char, count in counts.items():
            if char.isalpha():
                self.alphabet_count += count
            if char.islower():
                self.lowercase_count += count
            elif char.isupper():
                self.uppercase_count += count
            elif char.isnumeric():
                self.number_count += count
            elif char.isspace():
                self.space_count += count
            elif char in string.punctuation:
                self.symbol_count += count
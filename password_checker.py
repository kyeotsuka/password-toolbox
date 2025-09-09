from password import Password

class Checker:
    def __init__(self, password: Password) -> None:
        self.password = password
        
    def __str__(self) -> str:
        """Returns a user-friendly string showing the checker's result."""
        return f"Strength Checker Result: The password strength is '{self.password.strength}'."
        
    def check_strength(self) -> None:
        # Handle passwords that are too short.
        if self.password.length < 8:
            self.password.strength = "Very Weak"
            return

        # The Passphrase Check.
        if self.password.length >= 11 and self.password.space_count >= 2:
            words = self.password.pw_string.split()
            unique_words = set(words)
            
            # Penalise passphrases with low word variety.
            if len(unique_words) < 3:
                self.password.strength = "Weak"
            else:
                self.password.strength = "Strong"
            return

        # For complex, non-passphrase passwords.
        types_count = 0
        if self.password.lowercase_count > 0: types_count += 1
        if self.password.uppercase_count > 0: types_count += 1
        if self.password.number_count > 0: types_count += 1
        if self.password.symbol_count > 0: types_count += 1

        if self.password.length >= 12:
            # Penalise long but monotonous passwords (i.e. "aaaaaaaaaaaaa").
            if self.password.unique_char_count <= 2:
                self.password.strength = "Weak"
            elif types_count >= 3:
                self.password.strength = "Strong"
            else:
                self.password.strength = "Medium"
            return
            
        # Check for passwords between 8 and 11 characters.
        if types_count >= 2:
            self.password.strength = "Medium"
        else:
            self.password.strength = "Weak"
        return
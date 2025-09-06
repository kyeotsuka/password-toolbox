from password import Password

class Checker:
    def __init__(self, password: Password) -> None:
        self.password = password
        
    def __str__(self) -> str:
        """Returns a user-friendly string showing the checker's result."""
        return f"Checker Result: The password strength is '{self.password.strength}'."
        
    def check_strength(self) -> None:
        if self.password.length < 8:
            self.password.strength = "Very Weak"
            print("Password must be at least 8 characters long.\n")
            return
        elif self.password.length < 12:
            if self.password.symbol_count >= 1 and self.password.number_count >= 1 and self.password.uppercase_count >= 1:
                self.password.strength = "Medium"
            else:
                self.password.strength = "Weak"
            return
        elif self.password.length >= 12:
            self.password.strength = "Strong"
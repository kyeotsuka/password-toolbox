# import httpx 
from password import Password

class Checker:
    def __init__(self, password: Password) -> None:
        self.password = password
        
    def check_strength_old(self) -> None:
        # add a comment of password being too short to a list that holds criteria comments (too short, no numbers, etc.)
        
        if self.password.length < 8:
            self.password.strength = "Very Weak - must be at least 8 characters."
            return

        score = self.password.length

        for i in range(self.password.number_count): score += 1
        for i in range(self.password.uppercase_count): score += 1
        for i in range(self.password.number_count): score += 1
        for i in range(self.password.symbol_count): score += 1

        # Subtract penalty points
        if self.password.alphabet_count == self.password.length:
            score -= 10
        if self.password.number_count == self.password.length:
            score -= 10

        # Determine the final verdict based on the score
        if score >= 50:
            self.password.strength = "Very Strong"
        elif score >= 40:
            self.password.strength = "Strong"
        elif score >= 30:
            self.password.strength = "Medium"
        else:
            self.password.strength = "Weak"
            
    def check_strengh_modern(self) -> None:
        pass       
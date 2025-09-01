class Password:
    """The password's properties."""
    def __init__(self, pw_string) -> None:
        self.pw_string = pw_string
        self.length = len(pw_string)
        self.strength = 0
        self.has_lCase = False
        self.has_uCase = False
        self.has_numbers = False
        self.has_symbol = False
    
    def checkCase(self):
        for char in self.pw_string:
            if char.islower(): self.has_lCase = True
            elif char.isupper(): self.has_uCase = True
            if self.has_lCase and self.has_uCase: break
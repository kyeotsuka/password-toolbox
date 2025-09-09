from password import Password
from password_generator import Generator
from password_checker import Checker

def main():
    # 1. Create the generator tool
    generator = Generator()

    # 2. Use the tool to create a Password object and save it
    my_password = generator.generate_password(7)
    
    print("--- 1. Generated Password (Strength Untested) ---")
    print(my_password)

    # 3. Create a checker and give it the password to analyse
    checker = Checker(my_password)
    
    # 4. Run the strength check
    checker.check_strength()
    
    print("--- 2. Password After Being Checked ---")
    # The original my_password object has now been updated by the checker
    print(my_password)
    
    # You can also print the checker itself to see its result
    print("--- 3. Checker's Direct Output ---")
    print(checker)

if __name__ == '__main__':
    main()
    
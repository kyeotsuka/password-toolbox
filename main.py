from password import Password
from password_generator import Generator
from password_checker import Checker

def main():
    generated_password = Generator()
    my_password = Password(generated_password.generate_password(15))
    print(generated_password)
    checker = Checker(my_password)
    print(my_password)
    print(checker)  

# run main by default
if __name__ == '__main__': main()
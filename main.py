from password import Password
from password_checker import Checker

def main():
    my_password = Password("testD!/243")
    checker = Checker(my_password)
    print(my_password)
    print(checker)  

# run main by default
if __name__ == '__main__': main()
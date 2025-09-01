from Password import Password

def main():
    passwordTest = Password("test")
    test = passwordTest.checkCase()
    print(test)
    
    
# run main by default
if __name__ == '__main__': main()
import random
import string

def password_generate(len, complexity):
    lc = string.ascii_lowercase
    uc = string.ascii_uppercase
    d = string.digits
    s = string.punctuation

    Password = lc + uc + d
    if complexity == 'strong':
        Password += s
    elif complexity == 'medium':
        Password = Password
    elif complexity == 'weak':
        Password = lc+uc
    elif complexity == 'very weak':
        Password = lc

    password = ''.join(random.choice(Password) for i in range(len))
    return password

def Length():
    while True:
        try:
            len = int(input("Enter the required length for your password: "))
            if len <= 0:
                print("Length should be a positive number.")
            else:
                return len
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def Complexity():
    while True:
        complexity = input("Enter the desired complexity (strong, medium, weak, very weak): ").lower()
        if complexity in ['strong', 'medium', 'weak', 'very weak']:
            return complexity
        else:
            print("Invalid complexity level. Please choose from (strong, medium, weak, very weak).")

def main():
    len = Length()
    complexity = Complexity()
    password = password_generate(len, complexity)
    print(f"Generated Password: {password}")
while True:
    main()
    password_again = input("Do you want another password? (yes/no): ").lower()
    if password_again == 'no' or password_again!='yes':
        break

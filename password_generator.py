# password generator
import random
import string

# List of all letters (lowercase + uppercase)
all_letters = list(string.ascii_letters)

# List of all digits
all_digits=list(string.digits)

# List of all punctuation symbols
symbols = list('!@#$%^&*()_+-=[]{}|;:\'",.<>?/~`')

print("WELCOME TO PASSWORD GENERATOR")
n_letter=int(input("How many number of LETTERS do you want in your password :  "))
n_digits=int(input("How many number of DIGITS do you want in your password :  "))
n_symbols=int(input("How many number of SYMBOLS do you want in your password :  "))
password_list=[]
for i in range(1,n_letter+1):
    char=random.choice(all_letters)
    password_list+=char
for i in range(1,n_digits+1):
    char=random.choice(all_digits)
    password_list+=char
for i in range(1,n_symbols+1):
    char=random.choice(symbols)
    password_list+=char

random.shuffle(password_list)

password=''
for i in password_list:
    password += i

print("Password Generated : ",password)
# 8 commits

# Never output brackets or braces

# Use .strip()

# Use functions whenever you can (eg. a function to encrypt, a function to decrypt, a function to format the string)

# Functions can either output directly or return the string to where it was called (eg. your formatting function could call for decrypting and then it gets returned to the formatting function so that it can be formatted nicely)

# Use variables, lists or dictionaries or tuples, string formatting, loops, if statements, functions

# Give feedback to user & info abt what it's doing

# Choose cipher to use for program

# Ask user whether they want to decrypt/encrypt a message
def greet():
    d_or_e = input("\nHello! Hope you're having a great day <3\n\nWould you like to [e]ncrypt or [d]ecrypt?\n\n> ")
    og_string = input(f"\nThanks! Now please enter a string.\n\n> ")
    if d_or_e == 'e':
        encrypt()
    if d_or_e == 'd':
        decrypt()

# Accept string that program will either encrypt/decrypt

# Call function to encrypt/decrypt

# Create 2 functions that'll accept parameters in the form of list/dictionary that will contain string to be encrypted/decrypted. One will encrypt, other will decrypt using chosen cipher technique. This should involve loops & if statements
def encrypt():
    print("waa")

def decrypt():
    print("uieafife")

# Present final encrypted/decrypted string to user

# User must be able to copy output & run through program again to perfectly encrypt/decrypt multiple times without mistakes - test this

# Call functions
greet()
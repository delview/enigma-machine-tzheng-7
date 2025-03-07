# Create morse code list
morse_code = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

char_to_index = {char: idx for idx, char in enumerate(alphabet)}

# Create empty list to store og string
og_string = []

# Create empty list to store encrypted/decrypted string
changed_string = []

# 8 commits

# Use .strip()

# Use functions whenever you can (eg. a function to encrypt, a function to decrypt, a function to format the string)

# Functions can either output directly or return the string to where it was called (eg. your formatting function could call for decrypting and then it gets returned to the formatting function so that it can be formatted nicely)

# Use variables, lists or dictionaries or tuples, string formatting, loops, if statements, functions

# Ask user whether they want to decrypt/encrypt a message
def greet():
    '''
    Greets user, asks user for choice of encryption/decryption, & asks user for string they want to encrypt/decrypt
    '''
    d_or_e = input("\nHello! Hope you're having a great day <3\n\nWould you like to [e]ncrypt or [d]ecrypt?\n\n> ") # Greets user & asks user for choice of encryption/decryption
    og_string.append(input(f"\nThanks! Now please enter a string.\n\n> ").upper()) # Asks user for string they want to encrypt/decrypt
    if d_or_e == 'e': # If user's choice is to encrypt
        encrypt(og_string) # Call function to encrypt
    elif d_or_e == 'd': # If user's choice is to decrypt
        decrypt() # Call function to decrypt
    else:
        print("\nInvalid input...")
        greet()

# Create 2 functions that'll accept parameters in the form of list/dictionary that will contain string to be encrypted/decrypted. One will encrypt, other will decrypt using chosen cipher technique. This should involve loops & if statements
def encrypt(og_string):
    '''
    Encrypts user's string
    '''
    for char in og_string[0]:
        if char in char_to_index:
            index = char_to_index[char]  # Get index of character
            changed_string.append(morse_code[index])
            print(encrypt(og_string))
        else:
            changed_string.append('')
            print("\n")
        print(" ".join(changed_string))

def decrypt():
    '''
    Decrypts user's string
    '''
    print("uieafife")

# Present final encrypted/decrypted string to user

# User must be able to copy output & run through program again to perfectly encrypt/decrypt multiple times without mistakes - test this

# Run program
greet()
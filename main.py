# Create morse code list
morse_code = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']

alphabet = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ]

char_to_morse = {char: morse for char, morse in zip(alphabet, morse_code)}

morse_to_char = {morse: char for morse, char in zip(morse_code, alphabet)}

# Create empty list to store og string
og_string = []

# Create empty list to store encrypted/decrypted string
changed_string = []

# - 8 commits

# - Use .strip()

# - Use functions whenever you can (eg. a function to encrypt, a function to decrypt, a function to format the string)

# Functions can either output directly or return the string to where it was called (eg. your formatting function could call for decrypting and then it gets returned to the formatting function so that it can be formatted nicely)

# Use variables, lists or dictionaries or tuples, string formatting, loops, if statements, functions

# Ask user whether they want to decrypt/encrypt a message
def greet():
    '''
    Greets user, asks user for choice of encryption/decryption, & asks user for string they want to encrypt/decrypt
    '''
    d_or_e = input("\nWould you like to [e]ncrypt or [d]ecrypt?\n\n> ") # Greets user & asks user for choice of encryption/decryption
    if d_or_e == 'e': # If user's choice is to encrypt
        og_string = input(f"\nNow, please enter the message you would like to encrypt!\n\n> ").upper().strip() # Asks user for string they want to encrypt
        encrypt(og_string) # Call function to encrypt
    elif d_or_e == 'd': # If user's choice is to decrypt
        og_string = input(f"\nNow, please enter the message you would like to decrypt!\n\n> ").strip().split() # Asks user for string they want to decrypt
        decrypt(og_string) # Call function to decrypt
    else: # If user's input's invalid
        print("\nOops, invalid input :c") # Give feedback
        greet() # Loop till user gives valid input

# Create 2 functions that'll accept parameters in the form of list/dictionary that will contain string to be encrypted/decrypted. One will encrypt, other will decrypt using chosen cipher technique. This should involve loops & if statements
def encrypt(og_string):
    '''
    Encrypts user's string & outputs it
    '''
    for char in og_string:
        if char in char_to_morse: # If char is letter
            changed_string.append(char_to_morse[char]) # Change to morse code according to idx
        else: # If char is punctuation
            changed_string.append('') # Ignore it
    print("\nEncrypted message:") # Display encrypted msg
    print(" ".join(changed_string)) # Present final encrypted/decrypted string to user
    print("\n")

def decrypt(og_string):
    '''
    Decrypts user's string
    '''
    for morse in og_string:
        if morse in morse_to_char: # If char is morse code
            changed_string.append(morse_to_char[morse]) # Change to alphabet according to idx
        else: # If char is punctuation
            changed_string.append('') # Ignore it
    print("\nEncrypted message:") # Display encrypted msg
    print(" ".join(changed_string)) # Present final encrypted/decrypted string to user
    print("\n")

# - User must be able to copy output & run through program again to perfectly encrypt/decrypt multiple times without mistakes - test this

# Run program
print("\nHello! Hope you're having a great day <3") # Greet user before calling functions so it's not looped if input is invalid
greet()
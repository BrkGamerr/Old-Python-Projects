alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# user picks what to do
def encrypt_or_decrypt(choice):

    if choice == "encode":
        encrypt(original_text=text, shift_amount=shift)
    elif choice == "decode":
        decrypt(original_text=text, shift_amount=shift)


# encrypts the message
def encrypt(original_text, shift_amount):

    encoded_text = ""  # a variable to contain the encoded text

    for _ in original_text:
        shifted_position = alphabet.index(_) + shift_amount
        shifted_position %= len(alphabet)  # to prevent an error when shifting after Z
        encoded_text += alphabet[shifted_position]

    print(encoded_text)


# decrypts the message
def decrypt(original_text, shift_amount):

    decoded_text = ""  # a variable to contain the decoded text

    for _ in original_text:
        shifted_position = alphabet.index(_) - shift_amount
        shifted_position %= len(alphabet)  # to prevent an error when shifting after Z
        decoded_text += alphabet[shifted_position]

    print(decoded_text)


# Main Code
while True:

    # user input
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()

    # checks if the user has made a typo in input
    if direction == "encode":
        pass
    elif direction == "decode":
        pass
    else:
        print("You've made a typo! Try again!")
        continue

    # user inputs
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))

    # calls a function
    encrypt_or_decrypt(direction)

    # asks if the user wants to go again
    repeat = input("Type 'yes' or 'no' if you would like to go again: ")

    if repeat == "yes":
        continue
    else:
        break

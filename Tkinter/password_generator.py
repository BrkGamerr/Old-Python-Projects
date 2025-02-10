import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    password = ""

    # generating random characters for the password
    for _ in range(6):
        random_letter = random.choice(letters)
        password += random_letter

    for _ in range(6):
        random_symbol = random.choice(symbols)
        password += random_symbol

    for _ in range(6):
        random_number = random.choice(numbers)
        password += random_number

    # shuffling the password
    temp_list = list(password)
    random.shuffle(temp_list)
    password = "".join(temp_list)

    return password

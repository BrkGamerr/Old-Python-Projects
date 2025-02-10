import random
from string import ascii_letters as letters
from string import digits as numbers
from string import punctuation as symbols


def generate_letters(amount) -> list:
    letters_list = random.choices(letters, k=amount)
    return letters_list


def generate_numbers(amount) -> list:
    numbers_list = random.choices(numbers, k=amount)
    return numbers_list


def generate_symbols(amount) -> list:
    symbols_list = random.choices(symbols, k=amount)
    return symbols_list


def generate_password(letters_amount, numbers_amount, symbols_amount) -> str:
    password = generate_letters(letters_amount) + generate_numbers(numbers_amount) + generate_symbols(symbols_amount)
    random.shuffle(password)
    password = "".join(password)
    return password


print(generate_password(6, 6, 6))

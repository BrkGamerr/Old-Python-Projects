from os import system


def addition(number_1, number_2):
    result = number_1 + number_2
    return result


def subtraction(number_1, number_2):
    result = number_1 - number_2
    return result


def multiplication(number_1, number_2):
    result = number_1 * number_2
    return result


def division(number_1, number_2):
    result = number_1 / number_2
    return result

operations = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division
}


def calculator():

    # asks the user for the first number
    user_number_1 = float(input("Enter the first number: "))

    # prints out all the operation symbols from operations dictionary
    for symbol in operations:
        print(symbol)

    cont = True

    while cont:

        # asks the user to choose operation symbol
        operation_symbol = input("Pick an operation: ")

        # asks the user for second number
        user_number_2 = float(input("Enter the next number: "))

        # does the calculation with provided inputs
        answer = operations[operation_symbol](user_number_1, user_number_2)

        print(f"\n{user_number_1} {operation_symbol} {user_number_2} = {answer}")

        # continue or no
        continue_calculator = input(f"\nType 'y' to continue calculating with {answer},"
                                    f" or type 'n' to start a new calculation:")

        if continue_calculator == 'y':
            user_number_1 = answer
        else:
            cont = False
            system("cls")  # clears the terminal
            calculator()

calculator()

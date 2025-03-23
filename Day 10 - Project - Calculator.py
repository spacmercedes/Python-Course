def add(n1, n2):
    return n1 + n2


def substract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide

}

# print(operations["*"](4,8))
def calculator():
    should_acumulate = True
    first_number = float(input("Give me the first number: "))

    while should_acumulate:

        for symbol in operations:
            print(symbol)
        chosen_operation = input("Give an operation: ")
        second_number = float(input("Give me the second number: "))

        answer = operations[chosen_operation](first_number,second_number)
        print(f"{first_number} {chosen_operation} {second_number} = {answer}")


        choice = input("Do you want to keep calculating with last result? ")

        if choice == "y":
            first_number = answer
        elif choice =="n":
            should_acumulate = False
            print("\n" * 20)
            calculator()


calculator()
# Add
def add(n1, n2):
    return n1 + n2

# Subs
def subs(n1, n2):
    return n1 - n2

# mult
def mult(n1, n2):
    return n1 * n2

# div
def div(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subs,
    "*": mult,
    "/": div
}

def calculator():
    num1 = int(input("What is the first number? "))
    for keys in operations:
        print(keys)
    want_continue = True

    while want_continue:
        user_operation = input("What operation wants to do? ")
        num2 = int(input("What is the next number? "))
        calculation_function = operations[user_operation]
        answer = calculation_function(num1, num2)

        print(f"{num1} {user_operation} {num2} = {answer}")

        if input(
                f"Type 'y' if you want to continue calculatin with {answer} or type 'n' to start a new calculation: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()


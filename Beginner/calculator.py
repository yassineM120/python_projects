from art import calculator_logo
def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2


operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
def calculator():
    print(calculator_logo+"\n")
    num1 = float(input("What's the first number?: "))
    num2 = float(input("What's the second number?: "))
    for operation in operations:
        print(operation)
    picked_operation = input("Pick an operation from the line above: ")
    answer = operations[picked_operation](num1, num2)
    print(f"{num1} {picked_operation} {num2} = {answer} \n")


    finished = False

    while not finished :
        user_answer = input(f"Type 'y' to continue calculating with {answer},or type 'n' to exit.: ")
        if user_answer == "n":
            finished = True
            calculator()
        else:
            num3 = float(input("What's the third number?: "))
            for operation in operations:
                print(operation)
            picked_operation = input("Pick an operation from the line above: ")
            answer2 = operations[picked_operation](answer, num3)
            answer = answer2
            print(f"{answer} {picked_operation} {num3} = {answer2} \n")

calculator()
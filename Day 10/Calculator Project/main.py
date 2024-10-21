def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

calc_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

n1 = int(input("Enter num1: "))
calc = input('What math: "+", "-", "*" or "/": ')
n2 = int(input("Enter num2: "))

next = ""
while next != "no":
    print(calc_dict[calc](n1,n2))
    next = input("again?")

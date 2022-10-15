# imported files
import art

logo = art.logo
print(logo)
#Functions
def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def divide(n1,n2):
    return n1 / n2

def multiply(n1,n2):
    return n1 * n2


operations = {
    "+" : add,
    "-" : subtract,
    "/" : divide,
    "*" : multiply
}

num1 = int(input("What is the first number?: "))
num2 = int(input("What is the second number?: "))

for symbols in operations:
    print(symbols)

user_symbol = input("Pick an operation from the line above: ")
# function that uses the dictionary to choose a operation function
calculation_function = operations[user_symbol]
answer = calculation_function(num1,num2)





print(f'{num1} {user_symbol} {num2} = {answer}')
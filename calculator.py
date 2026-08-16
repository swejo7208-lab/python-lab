def add(a,b):
    return a+b
def subract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
operations_dict={
    "+":add,
    "-":subract,
    "*":multiply,
    "/":divide
}

def calculator():
    number1=int(input("Enter first number:"))
    for symbol in operations_dict:
        print(symbol)
    continue_flag=True
    while continue_flag:
        op_symbol=input("Pick an operator:")
        number2=int(input("Enter second number:"))
        calculator_fun=operations_dict[op_symbol]
        output=calculator_fun(number1,number2)
        print(f"{number1} {op_symbol} {number2} is {output}")

        to_continue=input(f"Enter 'Y' to continue calculation with {output} or 'N' to start new calculation 'X' to  exit.").lower()
        if to_continue=='y':
            number1=output
        elif to_continue=='n':
            continue_flag=False
            calculator()
        else:
            continue_flag=False
            print("Bye")
calculator()
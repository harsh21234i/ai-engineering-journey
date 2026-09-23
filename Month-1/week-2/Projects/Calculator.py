def add(n1, n2):
    return n1 + n2
def multiply(n1,n2):
    return n1 * n2
def subtract(n1,n2):
    return n1 - n2
def divide(n1,n2):
    return n1 / n2


##Add those finctions into keys having . Key="+" "-" "*" "/"
operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}
##Use the dictionary operations to perform calculations
def calculator():
    should_accumalate=True
    while should_accumalate:
        num1=float(input("whats my first number?:"))
        for symbol in operations:
            print(symbol)
        operation_symbol=input("Pick an operation?:")
        num2=float(input("whats my second number?:"))
        answere=operations[operation_symbol](num1,num2)
        print(f"{num1} {operation_symbol} {num2}={answere}")

        choice=input(f"if you want to continue calculating with {answere} type'y' else type 'n' to start new calulation")

        if choice=="y":
            num1 =answere
        else:
            should_accumalate=False
            print("\n"*20)
            calculator()


calculator()
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1*n2

def divide(n1, n2):
    return n1/n2

operations_dict = {"+": add, 
                   "-": subtract, 
                   "*": multiply, 
                   "/": divide
                   }

working = True
saved_result = None

while working:
    if saved_result != None:
        n1 = saved_result
    else:
        n1 = float(input("What's the first number?: "))


    print("+ \n - \n * \n /")
    operator = input("Pick an operation: ")
    n2 = float(input("What's the next number?: "))

    result = operations_dict[operator](n1, n2)

    print(f"{n1} {operator} {n2} = {result}")
    decision = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()

    if decision == "y":
        saved_result = result
    else:
        saved_result = None
        
        
    


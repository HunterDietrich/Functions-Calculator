print("---Welcome to Calculator Program---")
print()
num1 = int(input("Provide a first number: "))
num2 = int(input("Provide a second number: "))
op = input("Provide an operator. Choos one: \n +, -, /, * \n")


def check_operator(op):
    global num1, num2
    if op == "+":
        #addition
        addition(num1, num2)
    elif op == "-":
        #subbtraction
        pass
    elif op == "/":
        #division
        pass
    elif op == "*":
        #multiplication
        pass
    else:
        print("hmm... that's not an operation")

def addition(n1, n2):
            print(f"Sum is: {n1 + n2}")

check_operator(op)


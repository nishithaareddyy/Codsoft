a = float(input("First number: "))
b = float(input("Second number: "))
op = input("Pick an operation (+, -, *, /): ")

if op == "+": print(f"Result: {a+b}")
elif op == "-": print(f"Result: {a-b}")
elif op == "*": print(f"Result: {a*b}")
elif op == "/": print(f"Result: {a/b}" if b else "Oops! Can't divide by zero.")
else: print("Hmm... I don't know that operation 🤔")
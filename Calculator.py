def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    # Mapping operations to functions
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }

    print("--- Python CLI Calculator ---")
    
    while True:
        try:
            num1 = float(input("\nEnter first number: "))
            op = input("Choose operation (+, -, *, /) or 'q' to quit: ").strip()
            
            if op.lower() == 'q':
                print("Exiting. Goodbye!")
                break

            if op not in operations:
                print("Invalid operator. Please try again.")
                continue

            num2 = float(input("Enter second number: "))

            # Execute the function based on user input
            result = operations[op](num1, num2)
            print(f"Result: {num1} {op} {num2} = {result}")
            
        except ValueError:
            print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    calculator()
    
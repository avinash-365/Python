print("--- Simple Calculator ---\n")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("\n1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = int(input("\nEnter your choice (1-4): "))

match choice:
    case 1:
        print(f"Result: {a} + {b} = {a + b}")
    
    case 2:
        print(f"Result: {a} - {b} = {a - b}")
        
    case 3:
        print(f"Result: {a} * {b} = {a * b}")
    
    case 4:
        if b != 0:
            print(f"Result: {a} / {b} = {a / b}")
        else:
            print("Error: Cannot divide by zero!")
    
    case _:
        print("Invalid choice! Please select between 1 and 4.")

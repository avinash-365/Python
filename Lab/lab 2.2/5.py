print("--- 🍔 Welcome to Our Food Plaza 🍕 ---")

print("\n1. Order a Sandwich")
print("2. Order a Pizza")
print("3. Order a Burger")

choice = int(input("\nEnter your choice (1-3): "))

match choice:
    case 1:
        print("\n--- Sandwich Menu ---")
        print("1. Veg Grilled Sandwich")
        print("2. Cheese Chutney Sandwich")
        subchoice = int(input("Select your Sandwich: "))
        
        match subchoice:
            case 1:
                print("Success: Ordered Veg Grilled Sandwich!")
            case 2:
                print("Success: Ordered Cheese Chutney Sandwich!")
            case _:
                print("Error: Invalid Sandwich selection!")

    case 2:
        print("\n--- Pizza Menu ---")
        print("1. Thin Crust Pizza")
        print("2. Cheese Burst Pizza")
        print("3. Fresh Dough Pizza")
        subchoice = int(input("Select your Pizza: "))

        match subchoice:
            case 1:
                print("Success: Ordered a Thin Crust Pizza!")
            case 2:
                print("Success: Ordered a Cheese Burst Pizza!")
            case 3:
                print("Success: Ordered a Fresh Dough Pizza!")
            case _:
                print("Error: Invalid Pizza selection!")
        
    case 3:
        print("\n--- Burger Menu ---")
        print("1. Aloo Tikki Burger")
        print("2. Paneer Supreme Burger")
        subchoice = int(input("Select your Burger: "))
        
        match subchoice:
            case 1:
                print("Success: Ordered Aloo Tikki Burger!")
            case 2:
                print("Success: Ordered Paneer Supreme Burger!")
            case _:
                print("Error: Invalid Burger selection!")
    
    case _:
        print("Error: Invalid Main Menu selection!")

print("\n--- Thank you for visiting! ---")

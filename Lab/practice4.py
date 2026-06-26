# print("Welcome to the Sales & Inventory Intelligence System")
# data_list = []

# # Global metrics tracking to prevent initialization crashes
# sum_li = 0
# avg = 0.0

# # Input System Data
# def input_data():
#     global data_list
#     user_input = input("\nEnter stock quantities for a 1D array (separated by spaces):\n").strip()
#     if user_input:
#         data_list = [int(i) for i in user_input.split(" ")]
#         print("\nData has been stored successfully!")
#     else:
#         print("\nNo data entered. List remains unchanged.")


# # Display Sales Summary (Built-in Functions)
# def display(data_list):
#     global avg, sum_li
#     if not data_list:
#         print("\nError: Inventory list is empty! Please input data first.")
#         return
        
#     print(f"\nTotal products tracked: {len(data_list)}")
#     print(f"Minimum stock item: {min(data_list)}")
#     print(f"Maximum stock item: {max(data_list)}")
#     sum_li = sum(data_list)
#     print(f"Sum of all inventory units: {sum_li}")
#     avg = sum_li / len(data_list)
#     print(f"Average inventory level: {avg:.2f}")


# # Calculate Target Growth Forecast (Recursion)
# def calculate_growth(value, steps):
#     if steps == 0:
#         return value
#     new_value = value * 1.26
#     return calculate_growth(new_value, steps - 1)


# # Filter Stock by Price Threshold (Lambda Function)
# def filter_v(n):
#     # Filter reads safely from global data_list
#     new_list = list(filter(lambda x: x >= n, data_list))
#     print(new_list)


# # Sort Inventory Records In-Place
# def sorting():
#     global data_list
#     if not data_list:
#         print("\nError: Inventory list is empty! Nothing to sort.")
#         return
#     data_list.sort()
#     print(f"Sorted Inventory Records: {data_list}")


# # Multiple Values Return
# def mul_val(avg, sum_li):
#     return avg, sum_li


# while True:
#     print('''
#         Main Menu:
#         1. Input System Data
#         2. Display Sales Summary (Built-in Functions)
#         3. Calculate Target Growth Forecast (Recursion)
#         4. Filter Stock by Price Threshold (Lambda Function)
#         5. Sort Inventory Records
#         6. Display Detailed Inventory Metrics (Return Multiple Values)
#         7. Exit Program''')

#     try:
#         choice = int(input("\nPlease enter your choice: "))
#     except ValueError:
#         print("Invalid input! Please enter a number between 1 and 7.")
#         continue

#     if choice == 1:
#         input_data()

#     elif choice == 2:
#         display(data_list)

#     elif choice == 3:
#         try:
#             start_val = float(input("\nEnter a starting value to calculate a 5-step geometric revenue projection: "))
#             projected_value = calculate_growth(start_val, 5)
#             print(f"Projected value after compounding is: {int(projected_value)}")
#         except ValueError:
#             print("Invalid input! Please enter a numerical value.")

#     elif choice == 4:
#         if not data_list:
#             print("\nError: Inventory list is empty! Please input data first.")
#             continue
#         try:
#             n = int(input("Enter a threshold value to filter out data below this value: "))
#             print(f"Filtered Data (values >= {n}): ", end="")
#             filter_v(n)
#         except ValueError:
#             print("Invalid input! Please enter a whole number.")

#     elif choice == 5:
#         sorting()

#     elif choice == 6:
#         if sum_li == 0 and avg == 0.0 and len(data_list) > 0:
#             sum_li = sum(data_list)
#             avg = sum_li / len(data_list)
            
#         calculated_avg, calculated_sum = mul_val(avg, sum_li)
#         print(f"\n--- Detailed Inventory Metrics ---")
#         print(f"Current Calculated Average: {calculated_avg:.2f}")
#         print(f"Current Calculated Sum: {calculated_sum}")

#     elif choice == 7:
#         print("\nThank you for using the Sales & Inventory Intelligence System. Goodbye!")
#         break
        
#     else:
#         print("Invalid Choice! Please select an option from 1 to 7.")

# -------------------------------------------------------------------------------------------------------------------------------------------------------------
investment=[]



# Log Investments
def Log_Investments():
    global investment
    investment=[int(i) for i in input("Enter investment amounts for your portfolio (separated by spaces):\n").split(" ")]
    print("\nData has been logged successfully!")

# Portfolio Statistics
def Portfolio_Statistics(investment):
    global sum_i,avg
    sum_i=sum(investment)
    avg= sum_i / len(investment)
    print(f"""--- Portfolio Statistics ---
Total number of investments:{len(investment)}
Minimum investment amount: {min(investment)}
Maximum investment amount: {max(investment)}
Total portfolio valuation: {sum_i}
Average investment size: {avg}""")
    
#  Compound Profit
def Compound_Profit(amount , periods=6):
    if periods == 0:
        return amount
    else:
        new_amount=amount * (1 + 0.15)
        return Compound_Profit(new_amount,periods-1)
    
# Filter Micro-Investments - Lambda
def Micro_Investments(threshold):
    Filtered =list(filter(lambda amount:amount <= threshold,investment))
    print("Filtered Micro-Investments:",Filtered)

# sort
def sorting():
    global investment
    if not investment:
        print("\nError: Inventory list is empty! Nothing to sort.")
        return
    else:
        investment.sort(reverse=True)

# return value
def return_val(avg, sum_i):
    return avg, sum_i

print("Welcome to the Crypto Wallet & Investment Tracker")

while True:
    print('''
    Main Menu:
        1. Log Investments
        2. Portfolio Statistics
        3. Crypto Compound Profit (Recursion)
        4. Filter Micro-Investments (Lambda)
        5. Sort Portfolio
        6. Return Growth Summary
        7. Exit Program
''')
    
    choice=int(input("Please enter your choice: "))

    if choice == 1:
        Log_Investments()

    elif choice == 2:
        Portfolio_Statistics(investment)

    elif choice == 3:
        amount=int(input("Enter a starting investment amount to calculate 6-month compounded profit (15% monthly):"))
        new_amount= Compound_Profit(amount)
        print(f"Projected portfolio value after 6 months compounding is:{int(new_amount)}")
        Compound_Profit(amount)

    elif choice == 4:
        threshold=int(input("Enter a threshold value to filter out larger investments (amounts <= threshold):"))
        Micro_Investments(threshold)

    elif choice == 5:
        print("Portfolio sorted from highest to lowest valuation:",investment)
        sorting()

    elif choice == 6:
        if sum_i == 0 and avg == 0.0 and len(investment) > 0:
            sum_i = sum(investment)
            avg = sum_i / len(investment)
        
        cal_avg, cal_sum = return_val(avg, sum_i)
        print(f"\n--- Detailed Growth Summary ---")
        print(f"Current Portfolio Average: {cal_avg:.2f}")
        print(f"Current Total Invested: {cal_sum}")

    elif choice == 7:
            print("\nThank you for using the Crypto Wallet & Investment Tracker. Save and HODL! Goodbye!")
            break
            
    else:
        print("Invalid Choice! Please select an option from 1 to 7.")
data_input=[]

# input function
def user_input():
    global data_input
    data_input=[int(i) for i in input("\nEnter data for a 1D array (separated by spaces):\n").split()]

    print("\nData has been stored successfully!\n")

# buit-in function
def data_summary(data_input):
    print(f'''\nData Summary:
- Total Elements: {len(data_input)}
- Minimum Value: {min(data_input)}
- Maximum Value: {max(data_input)}
- Sum of all Value: {sum(data_input)}
- Average Value: {sum(data_input) / len(data_input):.2f}
''')
    
# Find Factorial (Recursion)
def factorial(number):
    if number <= 1:
        return 1
    else:
        return number * factorial(number - 1)

# filter data (lambda function)
def filter_data(threshold_value):
    new_list = list(filter(lambda x: x >= threshold_value, data_input))
    print(*new_list,sep=" ,")
    print()

# sorting data
def sort_data(data_input):
    global sorting,reverse_sorting
    sorting = sorted(data_input)
    reverse_sorting = sorted(data_input, reverse=True)

# return multiple value
def multiple_values(data_input):
    max_value=max(data_input)
    min_value=min(data_input)
    sum_value=sum(data_input)
    avg_value=sum(data_input) / len(data_input)

    return max_value,min_value,sum_value,avg_value 

# Exit Message
def Exit_message():
    print("\nThank you for using the data Analyzer and Transformer program. Goodbye !\n")


print("Welcome to the Data Analyzer and Transformer Program\n")

while True:
    print('''Main Menu:
    1. Input Data
    2. Display Data Summary (Built-in Functions)
    3. Calculate Factorial (Recursion)
    4. Filter Data by Threshold (Lambda Function)
    5. Sort Data
    6. Display Dataset Statistics (Return Multiple Values)
    7. Exit Program
''')
    choice=int(input("Please enter your choice: "))

    if choice ==  1:
        user_input()

    elif choice == 2:
        if not data_input:
            print("\nError: Please input data first using option 1!\n")
        else:
            data_summary(data_input)

    elif choice == 3:
        number = int(input("\nEnter number to Find of Factorial: "))
        if number < 0:
            print("\nFactorial is not defined for negative numbers!\n")
        else:
            print(f"\nFactorial of {number} is: {factorial(number)}\n")

    elif choice == 4:
        if not data_input:
            print("\nError: Please input data first using option 1!\n")
        else:
            threshold_value=int(input("\nEnter a threshold value to filter out data this value: "))
            print(f"\nFiltered data (Values >= {threshold_value}):")
            filter_data(threshold_value)

    elif choice == 5:
        if not data_input:
            print("\nError: Please input data first using option 1!\n")
            continue

        sort_data(data_input)
        print('''\nChoose sorting option:
1. Ascending
2. Descending''')
        
        sub_choice=int(input("\nEnter your choice:"))

        if sub_choice == 1:
            ascending_output = ", ".join(map(str, sorting))
            print("\nSorted data in Ascending order:\n",ascending_output)
            print()
        elif sub_choice == 2 :
            descending_output = ", ".join(map(str, reverse_sorting))
            print("\nSorted data in Descending order:\n",descending_output)
            print()
        else:
            print("\nInvaild choice !\n")
            
    elif choice == 6:
        if not data_input:
            print("\nError: Please input data first using option 1!\n")
        
        else:
            max_value,min_value,sum_value,avg_value = multiple_values(data_input)

            print(f'''\nDataset Statistics:
- Minimum value : {min_value}
- Maximum value: {max_value}
- Sum of all value: {sum_value}
- Average value: {avg_value:.2f}\n''')

    elif choice == 7:
        Exit_message()
        break

    else:
        print("Invaild Choice !")
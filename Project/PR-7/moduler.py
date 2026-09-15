import datetime 
import importlib

from modules import (
    # Datetime tools
    get_current_datetime,
    calculate_date_difference,
    format_custom_date,
    start_stopwatch,
    start_countdown,
    
    # Math tools
    fact,
    calculate_compound_interest,
    area_circle,
    area_rectangle,
    area_triangle,
    calculate_trig,
    
    # Random tools
    generate_random_number,
    generate_random_list,
    create_random_password,
    generate_random_otp,
    
    # UUID tool
    generate_unique_id,
    
    # File tools
    create_file,
    write_to_file,
    read_from_file,
    append_to_file
)

def main():
    print("="*35)
    print("Welcome to Multi-Utility Toolkit")
    print("="*35)

    while True:
        print('''Choose an option:
    1. Datetime and Time Opreations
    2. Mathematical Operations
    3. Random Data Generation
    4. Generate Unique Identifiers (UUID)
    5. File Operation (Custom Module)
    6. Explore Module Attributes (dir())
    7. Exit''')
        print("="*35)

        try:
            choice = int(input("Enter Your Choice :"))
        except ValueError:
            print("\nError: Please Enter Vaild Number !\n")
            continue

        if choice == 1:
            while True:
                print("="*35)
                print('''Datetime and Time Operations:

    1. Display current date and time
    2. Calculate difference between two dates/times
    3. Formate date into custom format
    4. stopwatch
    5. Countdown Timer
    6. Back to Main Menu''')
                print("="*35)

                try:
                    sub_choice = int(input("Enter Your Choice :"))
                except ValueError:
                    print("\nError: Please Enter Vaild Number !")
                    continue

                if sub_choice == 1:
                    print()
                    get_current_datetime()

                elif sub_choice == 2:
                    try:
                        user_input = input("\nEnter first Date (DD-MM-YYYY) Formate :")
                        date_obj = datetime.datetime.strptime(user_input,"%d-%m-%Y")
                            
                        user_input2 = input("Enter Second Date (DD-MM-YYYY) Formate :")
                        date_obj2 = datetime.datetime.strptime(user_input2,"%d-%m-%Y")

                        calculate_date_difference(date_obj2, date_obj)
                    except ValueError:
                        print("\nError: Invalid date format! Please use DD-MM-YYYY.")

                elif sub_choice == 3:
                    print("\n--- Date Selection ---")
                    print("1. Use Current Date & Time")
                    print("2. Enter Custom/Old Date")

                    try:
                        choice = int(input("Choose an option (1 or 2): "))
                    except ValueError:
                        print("\nError: Please Enter Vaild Number !")
                        continue

                    target_date = None
                    if choice == 1:
                        target_date = datetime.datetime.now()

                    elif choice == 2:
                        raw_date = input("Enter date (DD-MM-YYYY): ")
                        try:
                            target_date = datetime.datetime.strptime(raw_date, "%d-%m-%Y")
                        except ValueError:
                            print("\nError: Invalid date format! Please use DD-MM-YYYY.")
                            continue
                    else:
                        print("\nError: Invalid choice!")
                        continue

                    print("\nChoose Target Format:")
                    print("1. DD/MM/YYYY")
                    print("2. YYYY-MM-DD")
                    print("3. DD Month, YYYY (e.g. 10 September, 2026)")
                    print("4. DD-MM-YYYY HH:MM:SS")

                    try:
                        fmt_choice = int(input("Enter format choice (1-4): "))
                    except ValueError:
                        print("\nError: Please enter a valid number!")
                        continue

                    result = format_custom_date(target_date, fmt_choice)

                    if result:
                        print("\n" + "="*35)
                        print(f"Formatted Result: {result}")
                        print("="*35)

                    else:
                        print("\nError: Invalid format option selected!")

                elif sub_choice == 4:
                    start_stopwatch()

                elif sub_choice == 5:
                    try:
                        sec = int(input("\nEnter countdown time in seconds: "))
                        if sec > 0:
                            start_countdown(sec)
                        else:
                            print("\nError: Please enter a positive number!")
                    except ValueError:
                        print("\nError: Please enter a valid integer for seconds!")

                elif sub_choice == 6:
                    break

        elif choice == 2:
            while True:
                print("="*35)
                print('''Mathmatical Operations:
            
    1. Calculate Factorial
    2. Solve compound Interest
    3. Trigonometric Calculations
    4. Area of Geometric Shapes
    5. Back to Main Menu''')
                print("="*35)

                try:
                    sub_choice = int(input("Enter Your Choice :"))
                except ValueError:
                    print("\nError: Please Enter Vaild Number !")
                    continue

                if sub_choice == 1:
                    fact_num = int(input("\nEnter Number to Find of Factorial :"))

                    fact(fact_num)

                elif sub_choice == 2:
                    try:
                        p = float(input("Enter principal amount: "))
                        r = float(input("Enter rate of interest (in %): "))
                        t = float(input("Enter time (in years): "))

                        if p < 0 or r < 0 or t < 0:
                            print("\nError: Values cannot be negative!")
                            continue

                        total, interest_earned = calculate_compound_interest(p, r, t)

                        print("-" * 35)
                        print(f"Compound Interest: {total}")
                        print("-" * 35)

                    except ValueError:
                        print("\nError: Please enter valid numbers for calculation!")

                elif sub_choice == 3:
                    print("\n--- Trigonometric Functions ---")
                    print("1. Sine (sin)")
                    print("2. Cosine (cos)")
                    print("3. Tangent (tan)")
                    
                    try:
                        trig_choice = int(input("Select function (1-3): "))
                        if trig_choice not in [1, 2, 3]:
                            print("\nError: Please choose 1, 2, or 3!")
                            continue
                            
                        deg = float(input("Enter angle in degrees: "))
                        val = calculate_trig(deg, trig_choice)
                        
                        print("-" * 35)
                        if isinstance(val, str):
                            print(f"Result: {val}")
                        else:
                            print(f"Result: {round(val, 4)}")
                        print("-" * 35)
                    except ValueError:
                        print("\nError: Please enter a valid number!")

                elif sub_choice == 4:
                    print("\n--- Area of Geometric Shapes ---")
                    print("1. Circle")
                    print("2. Rectangle")
                    print("3. Triangle")
                    
                    try:
                        shape_choice = int(input("Select shape (1-3): "))
                        
                        if shape_choice == 1:
                            r = float(input("Enter radius: "))
                            if r < 0:
                                print("\nError: Radius cannot be negative!")
                                continue
                            ans = area_circle(r)
                            print(f"Area of Circle: {round(ans, 2)}")
                            
                        elif shape_choice == 2:
                            l = float(input("Enter length: "))
                            w = float(input("Enter width: "))
                            if l < 0 or w < 0:
                                print("\nError: Dimensions cannot be negative!")
                                continue
                            ans = area_rectangle(l, w)
                            print(f"Area of Rectangle: {round(ans, 2)}")
                            
                        elif shape_choice == 3:
                            b = float(input("Enter base: "))
                            h = float(input("Enter height: "))
                            if b < 0 or h < 0:
                                print("\nError: Dimensions cannot be negative!")
                                continue
                            ans = area_triangle(b, h)
                            print(f"Area of Triangle: {round(ans, 2)}")
                            
                        else:
                            print("\nError: Invalid shape choice!")
                    except ValueError:
                        print("\nError: Please enter valid numbers for calculation!")

                elif sub_choice == 5:
                    break

        elif choice == 3:
                while True:
                    print("="*35)
                    print('''Random Data Generation:
                
    1. Generate Random Number
    2. Generate Random List
    3. Create Random Password
    4. Generate Random OTP
    5. Back to Main Menu''')
                    print("="*35)
        
                    try:
                        sub_choice = int(input("Enter Your Choice :"))
                    except ValueError:
                        print("\nError: Please Enter Vaild Number !")
                        continue

                    if sub_choice == 1:
                        try:
                            start = int(input("Enter starting range: "))
                            end = int(input("Enter ending range: "))
                            if start > end:
                                print("\nError: Start range cannot be greater than End range!")
                                continue
                            num = generate_random_number(start, end)
                            print(f"\nGenerated Random Number: {num}")
                        except ValueError:
                            print("\nError: Please enter valid integers!")

                    elif sub_choice == 2:
                        try:
                            size = int(input("Enter number of elements for the list: "))
                            start = int(input("Enter minimum value: "))
                            end = int(input("Enter maximum value: "))
                            if start > end or size <= 0:
                                print("\nError: Please check the range and size values!")
                                continue
                            my_list = generate_random_list(size, start, end)
                            print(f"\nGenerated Random List: {my_list}")
                        except ValueError:
                            print("\nError: Please enter valid integers!")

                    elif sub_choice == 3:
                        try:
                            length = int(input("Enter password length: "))
                            if length < 4:
                                print("\nError: Password length should be at least 4 characters!")
                                continue
                            pwd = create_random_password(length)
                            print(f"\nGenerated Password: {pwd}")
                        except ValueError:
                            print("\nError: Please enter a valid number for length!")

                    elif sub_choice == 4:
                        try:
                            digits = int(input("Enter OTP length (e.g. 4 or 6): "))
                            if digits <= 0:
                                print("\nError: Length must be positive!")
                                continue
                            otp = generate_random_otp(digits)
                            print(f"\nGenerated OTP: {otp}")
                        except ValueError:
                            print("\nError: Please enter a valid number!")

                    elif sub_choice == 5:
                        break

                    else:
                        print("\nError: Invalid option selected!")

        elif choice == 4:
            print("Generate Unique Identifiers:")
            new_uuid = generate_unique_id()
            print(f"Generated UUID: {new_uuid}")
            print("=" * 35)

        elif choice == 5:
            while True:
                print("="*35)
                print('''File Operations:
    1. Create a new file
    2. Write to a file
    3. Read from a file
    4. Append to a file
    5. Back to Main Menu''')
                print("="*35)

                try:
                    sub_choice = int(input("Enter your choice: "))
                except ValueError:
                    print("\nError: Please enter a valid number!")
                    continue

                if sub_choice == 1:
                    filename = input("\nEnter file name: ")
                    create_file(filename)

                elif sub_choice == 2:
                    filename = input("\nEnter file name: ")
                    content = input("Enter data to write: ")
                    write_to_file(filename, content)

                elif sub_choice == 3:
                    filename = input("\nEnter file name: ")
                    read_from_file(filename)

                elif sub_choice == 4:
                    filename = input("\nEnter file name: ")
                    content = input("Enter data to append: ")
                    append_to_file(filename, content)

                elif sub_choice == 5:
                    break

                else:
                    print("\nError: Please choose a valid option (1-5)!")

        elif choice == 6:
            print("Explore Module Attributes:")
            mod_name = input("Enter module name to explore: ").strip()

            try:
                module_obj = importlib.import_module(mod_name)
                
                attributes = dir(module_obj)
                
                print(f"Available Attributes in {mod_name} module:")
                print(attributes)
                print("=" * 35)

            except ModuleNotFoundError:
                print(f"Error: Module '{mod_name}' not found! Please check the spelling.")
                print("=" * 35)

        elif choice == 7:
            print("=" * 35)
            print("Thank you for using the Multi-Utility Toolkit!")
            print("=" * 35)
            break

if __name__ == "__main__":
    main()
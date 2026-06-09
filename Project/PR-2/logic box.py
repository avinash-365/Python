print("Welcome to the Pattern Generator and Number Analyzer!")

while True:
    print("\nSelect an option:")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit\n")

    choice=int(input("Enter your choice:"))

    match choice:

        case 1:
            while True:
                print("\nWelcome to Pattern Menu!")
                print("Enter 1 for * pattern")
                print("Enter 2 for 1(num) pattern")
                print("Enter 3 for Main Menu")

                choice1=int(input("\nEnter your choice:"))

                if choice1==1:
                    row=int(input("\nEnter the number of rows for the pattern:"))
                    print("\nPattern of *:")
                    for i in range(1,row+1):
                        for j in range(1,i+1):
                            print("*",end=" ")
                        print()

                elif choice1==2:
                    row=int(input("\nEnter the number of rows for the pattern:"))
                    print("\nPattern of 1(num):")
                    for i in range(1,row+1):
                        for j in range(1,i+1):
                            print(i,end=" ")
                        print()

                elif choice1==3:
                    print("\nWelcome back to Main Menu!")
                    break
                
                else:
                    print("Enter Invaild value!")
        case 2:
            print("\nWelcome to Analyze Number!")
            sum=0
            start=int(input("\nEnter the start of the range:"))
            stop=int(input("Enter the end of the range:"))
    
            if start>stop:
                for i in range(start,stop-1,-1):
                    if i==0:
                        print(f"number {i} is neutral")
                    elif i%2==0:
                        print(f"Number {i} is Even")
                    else:
                        print(f"Number {i} is Odd")
                    sum=sum+i
                print(f"Sum of all numbers from {start} to {stop} is:",sum)

            else:
                for i in range(start,stop+1):
                    if i==0:
                        print(f"number {i} is neutral")
                    elif i%2==0:
                        print(f"Number {i} is Even")
                    else:
                        print(f"Number {i} is Odd")
                    sum=sum+i
                print(f"Sum of all numbers from {start} to {stop} is:",sum)

        case 3:
            print("Exiting the program. Goodbye!")
            break

        case _:
            print("Enter Invaild value!")
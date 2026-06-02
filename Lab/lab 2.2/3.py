print("Maximum number of 4 numbers\n")
A = int(input("Enter 1st num: "))
B = int(input("Enter 2nd num: "))
C = int(input("Enter 3rd num: "))
D = int(input("Enter 4th num: "))

if a > b:
    if a > c:
        if a > d:
            print(f"{A} is Maximum")
        else:
            print(f"{D} is Maximum")
    else:
        if c > d:
            print(f"{C} is Maximum")
        else:
            print(f"{D} is Maximum")
else:
    if b > c:
        if b > d:
            print(f"{B} is Maximum")
        else:
            print(f"{D} is Maximum")
    else:
        if c > d:
            print(f"{C} is Maximum")
        else:
            print(f"{D} is Maximum")
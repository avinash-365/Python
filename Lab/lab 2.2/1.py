print("Maximum number of 3 number\n")
a=int(input("Enter 1st num:"))
b=int(input("Enter 2nd num:"))
c=int(input("Enter 3rd num:"))

if a>b:
    if a>c:
        print(f"{a} Is Maximum number")
    else:
        print(f"{c} Is Maximum number")
else:
    if b>c:
        print(f"{b} Is Maximum number")
    else:
        print(f"{c} Is Maximum number")
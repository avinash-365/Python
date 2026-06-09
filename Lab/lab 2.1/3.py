print("Largest number of 3 number\n")
a=int(input("Enter 1 Num:"))
b=int(input("Enter 2 Num:"))
c=int(input("Enter 3 Num:"))

if a>b:
    if a>c:
        print(f"{a} is largest number")
    else:
        print(f"{c} is largest number")
else :
    if b>c:
        print(f"{b} is largest number")

    else:
        print(f"{c} is largest number")
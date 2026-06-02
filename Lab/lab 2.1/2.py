print("Age categorize program\n")
age=int(input("Enter Your Age:"))

if age<=12:
    print("Child")
elif age<=19 and age>=12:
    print("Teenager")
elif age<=59 and age>=19:
    print("Adult")
elif age>=60:
    print("Senior")
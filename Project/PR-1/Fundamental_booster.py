print("Welcome to the Interactive Personal Data Collector!\n")

name=input("Please enter your name:")
age=input("Please enter your age:")
height=input("Please enter your height in meters:")
fnum=int(input("Please enter your favourite number:"))

type(int(age))
type(float(height))

bithyear=2026 - age

print("\nThank you! Here is the information we collected:")

print("\nName:",name,"(Type:",type(name),", Memory Address:",id(name),")")
print("Age:",age,"(Type:",type(age),", Memory Address:",id(age),")")
print("Height:",height,"(Type:",type(height),", Memory Address:",id(height),")")
print("Favourite Number::",fnum,"(Type:",type(fnum),", Memory Address:",id(fnum),")")

print("\nYour birth year is approximately:",bithyear,"( based on your age of ",age,")")

print("\nThank you for using the Personal Data Collector. Goodbye!")
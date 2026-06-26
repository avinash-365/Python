print("Welcome Programmers !")

arr=[]

while True:

    print('''
Select an option:
    1. Create Array
    2. Find Sum of All Elements
    3. Find Largest Number
    4. Find Smallest Number
    5. Count Even and Odd Numbers
    6. Reverse the Array
    7. Check if an Element Exists
    8. Count Frequency of an Element
    9. Read Array
    10. Update Array
    11. Delete Array
    12. Exit 
''')
    choice=int(input("Enter Your Choice:"))

    if choice==1:
        n=int(input("\nHow many element do you enter:"))

        for i in range(n):
            a=int(input(f"Enter Element {i+1}:"))
            arr.append(a)
        print("\nArray Created Successfully !")

    elif choice==2:
        sum=0
        for i in arr:
            sum += i
        print("\nSum of all elements:",sum)

    elif choice==3:
        largest = arr[0]
        for num in arr:
            if num > largest:
                largest = num
        print("\nLargest num is :",largest)

    elif choice==4:
        smallest = arr[0]
        for num in arr:
            if num < smallest:
                smallest = num
        print("\nsmallest num is :",smallest)

    elif choice==5:
        even = 0
        odd = 0
        for i in arr:
            if i%2==0:
                even += 1
            else:
                odd += 1

        print(f"\nEven Number is :{even}")
        print(f"Odd Number is :{odd}")

    elif choice==6:
        print("\nReverse Array is:",arr[::-1])

    elif choice==7:
        element=int(input("Enter Element to be Find:"))
        for i in arr:
            if i == element:
                print(f"\n{element} is Exits in Array")
                break
        else:
            print(f"\n{element} does not exist in Array")
    
    elif choice==8:
        element=int(input("Enter Element to be Find:"))
        count=0

        for i in arr:
            if element == i:
                count += 1

        print(f"\n{element} appears {count} times")

    elif choice==9:
        for i in arr:
            print(f"\nArray is : {arr}")
            break

    elif choice==10:
        val = int(input("Enter value to search and update: "))
        found = False 

        for i in range(len(arr)):
            if arr[i] == val:
                val2 = int(input("Enter new value to update: "))
                arr[i] = val2 
                print("Array Updated Successfully!")
                found = True
                break 

        if not found:
            print("Value not Found in Array!")

        print("Updated Array:", arr)

    elif choice==11:
        val = int(input("Enter value to search and delete: "))
        found = False

        for i in range(len(arr)):
            if arr[i]==val:
                del arr[i]
                print("Array Eelement delete Successfully !")
                found=True
                break
        if not found:
            print("Value not Found in Array!")

        print("Updated Array:", arr)

    elif choice==12:
        print("Exit !")
        break

    else:
        print("\nInvaild Choice !")
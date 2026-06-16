print("Welcome to our student portal")

student = []

while True:
    print('''\nWelcome Student Menu:
    Enter 1 for add student
    Enter 2 for update student
    Enter 3 for read data of student
    Enter 4 to delete student data
    Enter 0 to Exit portal
    ''')

    choice = int(input("Enter Your choice: "))

    if choice == 1:
        st = {
            "id": len(student) + 1,
            "name": input("\nEnter Student Name: "),
            "age": int(input("Enter Student age: ")),
            "subject": set(input("Enter Subject separated with comma(,): ").split(","))
        }
        student.append(st)
        print("Student Added Successfully!")

    elif choice == 2:
        stdid = int(input("Enter id you want to update: "))
        found = False
        for st in student:
            if st["id"] == stdid:
                found = True
                st["name"] = input("\nEnter Student Name: ") 
                st["age"] = int(input("Enter Student age: ")) 
                st["subject"] = set(input("Enter Subject separated with comma(,): ").split(","))
                print("Student Updated Successfully!")
                break 
        if not found:
            print("Student Not Found!")

    elif choice == 3:
        for st in student:
            subjects = ", ".join(st["subject"])
            print(f"Id: {st['id']} | Name: {st['name']} | Subject: {subjects}")

    elif choice == 4:
        stdid = int(input("Enter id you want to delete: "))
        found = False
        for st in student:
            if st["id"] == stdid:
                found = True
                student.remove(st)
                print("Student deleted Successfully!")
                break
        if not found:
            print("Student Not Found!")

    elif choice == 0:
        print("Exited Successfully!")
        break

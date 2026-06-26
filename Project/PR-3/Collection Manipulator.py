print("Welcome to the Student Data Organizer!")
student=[]
id=101

while True:
    print('''\nSelect an option:
    1. Add Student
    2. Display All Students
    3. Update Student Information
    4. Delete Student
    5. Display Subjects Offered
    6. Exit''')

    choice=int(input("\nEnter your choice:"))

    if choice==1:
        print("\nEnter student details:")
        stu={
            "Id":id,
            "Name":input("Name:"),
            "Age":int(input("Age:")),
            "Grade":input("Grade:"),
            "DOB":input("Date Of Birth (YYYY-MM-DD):"),
            "Subject":set(input("Subjects (comma-separated):").split(","))
        }

        student.append(stu)
        print("\nStudent added successfully!")
        id += 1

    elif choice==2:
        print("\n--- Display All Students ---")
        for stu in student:
            print(f"ID:{stu["Id"]} | Name:{stu["Name"]} | Age:{stu["Age"]} | Grade:{stu["Grade"]} | Subject:{",".join(stu["Subject"])}")
    
    elif choice == 3:
        stuid = int(input("\nEnter the Student ID you want to update: "))
        found = False

        for stu in student:
            if stu["Id"] == stuid:
                found = True
                
                print("\nCurrent details:")
                print(f"ID: {stu['Id']} | Name: {stu['Name']} | Age: {stu['Age']} | Grade: {stu['Grade']} | Subjects: {', '.join(stu['Subject'])}")
                
                while True:
                    field_choice = input("\nWhich field do you want to update? (Name, Age, DOB, Grade, Subject): ").lower()

                    if field_choice == "name":
                        stu["Name"] = input("Update Name: ")
                        break
                    elif field_choice == "age":
                        stu["Age"] = int(input("Update Age: "))
                        break
                    elif field_choice == "grade":
                        stu["Grade"] = input("Update Grade: ")
                        break
                    elif field_choice == "dob":
                        stu["DOB"] = input("Update DOB: ")
                        break
                    elif field_choice == "subject":
                        stu["Subject"] = set(input("Subjects (comma-separated): ").split(","))
                        break
                    else:
                        print("Invalid option!")

                print("\nDetails updated successfully!")
                break 

        if found==False:
            print("Student ID not found!")
    
    elif choice == 4:
        stuid = int(input("\nEnter the Student ID you want to delete: "))
        found = False

        for stu in student:
            if stu["Id"] == stuid:
                found = True
                del student[student.index(stu)]
                print("\nDetails deleted successfully!")
                break  

        if found == False:
            print("\nStudent Not Found!")

    elif choice == 5:
        print("\n--- All Unique Subjects Offered Across All Students ---")
        all_subjects = set()
        
        for stu in student:
            all_subjects.update(stu["Subject"])
            
        if all_subjects:
            print("Unique Subjects Available:", ", ".join(all_subjects))
        else:
            print("No student records found to extract subjects!")

    elif choice==6:
        print("\nThank you for using the Student Data Organizer! Have a great day.")    
        break

    else:
        print("Please Enter Vaild Choice!")

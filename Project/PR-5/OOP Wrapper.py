class Employee:
    id_counter = 1000
    def __init__(self,employee_name,employee_age,employee_salary):
        self.__employee_id=Employee.id_counter
        self.employee_name=employee_name
        self.employee_age=employee_age
        self.employee_salary = employee_salary

        Employee.id_counter += 1

    @property
    def get_employee_id(self):
        return self.__employee_id

    @property
    def employee_salary(self):
        return self.__employee_salary

    @employee_salary.setter
    def employee_salary(self,new_salary):

        if new_salary >= 0:
            self.__employee_salary = new_salary

        else :
            print("\nError: Salary cannot be negative!")
            self.__employee_salary = 0

    def display_details(self):
        if type(self).__name__ == "Manager":
            print(f"\nManager id : {self.__employee_id} || Manager Name: {self.employee_name} || Manager Age: {self.employee_age} || Manager Salary: {self.__employee_salary}",end=" || ")

        elif type(self).__name__ == "Developer":
            print(f"\nDeveloper id : {self.__employee_id} || Developer Name: {self.employee_name} || Developer Age: {self.employee_age} || Developer Salary: {self.__employee_salary}",end=" || ")

        else:
            print(f"\nEmployee id : {self.__employee_id} || Employee Name: {self.employee_name} || Employee Age: {self.employee_age} || Employee Salary: {self.__employee_salary}")

    def __del__(self):
        print("Thank you")
        


class Manager(Employee):
    def __init__(self, employee_name, employee_age, employee_salary,manager_department):
        super().__init__(employee_name, employee_age, employee_salary)
        self.manager_department=manager_department

    def display_details(self): 
        super().display_details()
        print(f"Manager Department: {self.manager_department}")
    
    def __del__(self):
        pass
        

class Developer(Employee):
    def __init__(self, employee_name, employee_age, employee_salary,programming_language):
        super().__init__(employee_name, employee_age, employee_salary)
        self.programming_language = programming_language

    def display_details(self):
        super().display_details()
        print(f"Programing Language: {self.programming_language}")
    
    def __del__(self):
        pass

emp=[]
man=[]
dev=[]

print("\n---Python OOP Project: Employee Management System---")

while True:

    print("""\nChoose an operation:
1. Create an Employee / Manager / Developer
2. Show Details of Employee / Manager / Developer
3. Update a Employee / Manager / Developer
4. Delete a Employee / Manager / Developer
5. Exit""")
    
    choice=int(input("\nEnter your choice:"))
    
    if choice == 1:

        subChoice=int(input('''\nChoose an Create operation:
1. Create a Employee
2. Create a Manager
3. Create a Developer
                         
Enter your choice:'''))
        
        if subChoice == 1:
            employee_name=input("\nEnter Employee Name:")
            employee_age=int(input("Enter Employee Age:"))
            new_salary=int(input("Enter Employee Salary:"))

            empobj = Employee(employee_name,employee_age,new_salary)

            emp.append(empobj)

            print(f"\nEmployee Create with name: {employee_name} || Age: {employee_age} || Salary: {new_salary}.")

        elif subChoice == 2:
            manager_name=input("\nEnter Manager Name:")
            manager_age=int(input("Enter Manager Age:"))
            new_salary=int(input("Enter Manager Salary:"))
            manager_department=input("Enter Manager Department:")

            manobj = Manager(manager_name,manager_age,new_salary,manager_department)

            man.append(manobj)

            print(f"\nManager Create with name: {manager_name} || Age: {manager_age} || Salary: {new_salary} || Department: {manager_department}.")            

        elif subChoice == 3:
            developer_name=input("\nEnter Developer Name:")
            developer_age=int(input("Enter Developer Age:"))
            new_salary=int(input("Enter Developer Salary:"))
            Programming_language=input("Enter Developer Programing Language:")

            devobj = Developer(developer_name,developer_age,new_salary,Programming_language)

            dev.append(devobj)

            print(f"\nDeveloper Create with name: {developer_name} || Age: {developer_age} || Salary: {new_salary} || Programing Language: {Programming_language}.")            

        else:
            print("\nPlease Enter Valid Choice !")

    elif choice == 2:

        if len(emp) == 0 and len(man) == 0 and len(dev) == 0:
            print("\nNo data available! Please enter (create) data first.") 

        else:

            subChoice=int(input('''\nChoose an View operation:
1. View a Employee
2. View a Manager
3. View a Developer
                            
Enter your choice:'''))
            
            if subChoice == 1:
                if len(emp)==0:
                    print("\nNo data available for Employee!")
                else:
                    for emp_details in emp:
                        emp_details.display_details()

            elif subChoice == 2:
                if len(man)==0:
                    print("\nNo data available for Manager!")
                else:
                    for man_details in man:
                        man_details.display_details()

            elif subChoice == 3:
                if len(dev)==0:
                    print("\nNo data available for developer!")
                else:
                    for dev_details in dev:
                        dev_details.display_details()

            else:
                print("\nPlease Enter Valid Choice !")

    elif choice == 3:
        pass

    elif choice == 4:
        pass

    elif choice == 5:
        print("\nThank you for using the Employee Management System! Goodbye.\n")
        break

    else:
        print("\nPlease enter a valid choice!")
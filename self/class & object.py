# Person ---> Student
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age,roll_num,standard):
        super().__init__(name, age)
        self.roll_num = roll_num
        self.standard = standard

    def display(self):
        print(f"Student Details:\nName: {self.name}\nAge: {self.age}\nRoll numm: {self.roll_num}\nstandard: {self.standard}")

p1 = Student("Abc",15,177,10)
p1.display()

# Vehicle ---> Car

class Vehical:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

class Car(Vehical):
    def __init__(self, brand, model,fuel_type):
        super().__init__(brand, model)
        self.fuel_type = fuel_type

    def display(self):
        print(f"\n\nVehical Details:\nCar Brand: {self.brand}\nCar Model: {self.model}\nFuel Type: {self.fuel_type}")

c1 = Car("Totota","Fortuner","disel")
c1.display()

# Employee ---> Manager

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary,department):
        super().__init__(name, salary)
        self.department = department

    def display(self):
        print(f"\n\nEmployee Details:\nEmployee Name: {self.name}\nEmployee Salary: {self.salary}\nEmployee department: {self.department}")

e1 = Manager("Abc",150000,"AI-ML")
e1.display()

# BankAccount ----> SavingsAccount

class bankaccoount:
    def __init__(self,acc_no,h_name,balance):
        self.acc_no = acc_no
        self.h_name = h_name
        self.balance = balance

class savingaccount(bankaccoount):
    def __init__(self, acc_no, h_name, balance,interest_rate,interest):
        super().__init__(acc_no, h_name, balance)
        self.interest_rate = interest_rate
        self.interest = interest

    def display(self):
        print(f"\n\nBank Details:\nAccount No: {self.h_name}\nBalance: {self.balance}\ninterest rate: {self.interest_rate}\nninterest: {self.interest}")

b1=savingaccount(12547893,"Abc",25000,5.22,560)
b1.display()

#  Product -------> Electronics

class Product:

    def __init__(self, product_name, price):
        self.product_name=product_name
        self.price=price

class Electronics(Product):

    def __init__(self, product_name, price, brand, warranty):
        super().__init__(product_name,price)
        self.brand=brand
        self.warranty=warranty

    def display_data(self):
        print(f"\n\nProduct Details:\nProduct : {self.product_name}\nPrice : {self.price}\nBrand : {self.brand}\nWarranty : {self.warranty} years")

product1=Electronics("Mobile",25000,"ROG",3)
product1.display_data()
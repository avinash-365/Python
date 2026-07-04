# class FactoryBlueprint:

#     def __init__(self, name, model, registered_year):
#         self.name = name
#         self.model = model
#         self.registered_year = registered_year

# obj = FactoryBlueprint("toyota", 2026, 2026)
# obj2 = FactoryBlueprint("tata", 2023, 2025)

# print(obj.name, obj.model, obj.registered_year)
# print(obj2.name, obj2.model, obj2.registered_year)

#--------------------------------------1-------------------------------

# class Govrto:

#     def __init__(self,name,model,state="GJ"):
#         self.name=name
#         self.__model=model
#         self.state=state

#     def getdata(self):
#         print(f"Your car information:\n {self.name} \n {self.__model} \n {self.state}")

#     def __del__(self):
#         print("Done !")

# name=input("Enter name :")
# model=input("Enter Model:")
# state=input("Enter state:")

# if state.strip() != "":
#     obj = Govrto(name,model,state)
# else:
#     obj = Govrto(name,model)


# obj.getdata()

#----------------------------2----------------------------------
# class Bank:

#     def __init__(self,Bank_name,Bank_Branch,Bank_Acc=101,Bank_amount=10500):
#         self.Bank_name=Bank_name
#         self.__Bank_Acc=Bank_Acc
#         self.__Bank_amout=Bank_amount
#         self.Bank_Branch=Bank_Branch

#     def getdata(self):
#         print(f'''\nAccount Details:\nBank Name: {self.Bank_name}\nAccount Number: {self.__Bank_Acc}\nBalance: {self.__Bank_amout}\nBank Branch: {self.Bank_Branch}''')

#     def __del__(self):
#         print("Account details Fetch Successfully !")

# Bank_name=input("Enter Your Bank Name:")
# Bank_Branch=input("Enter Your Branch Name:")
# Bank_Acc=input("Enter Acc:")

# if len(Bank_Acc) >= 1:
#     obj=Bank(Bank_name,Bank_Branch,Bank_Acc)
# else:
#     obj=Bank(Bank_name,Bank_Branch)

# obj.getdata()
class LibraryItem:
    id_counter = 1000
    def __init__(self, title, publisher,price):
        self.__item_id= LibraryItem.id_counter
        self.title=title
        self.publisher=publisher
        self.set_price(price)

        LibraryItem.id_counter += 1

    def get_price(self):
        return  self.__price
    
    def get_item_id(self):
        return self.__item_id
    
    def set_price(self,new_price):
        if new_price >= 0:
            self.__price = new_price
        else :
            print("\nError: Price cannot be negative!")
            self.__price=0

    def display_details(self):
        print(f"\nId:{self.__item_id} || Book Title: {self.title} || Book Publisher: {self.publisher} || Book Price: {self.__price}", end=" || ")

    def __del__(self):
        pass

class Book(LibraryItem):
    def __init__(self, title, publisher, price,author,number_of_pages):
        super().__init__(title, publisher, price)
        self.author = author
        self.number_of_pages = number_of_pages

    def display_details(self):
        super().display_details()
        print(f"Author is : {self.author} || Book of num of Pages: {self.number_of_pages}\n")

    def __del__(self):
        pass

class Magazine(LibraryItem):
    def __init__(self, title, publisher, price,issue_month):
        super().__init__( title, publisher, price)
        self.issue_month = issue_month

    def display_details(self):
        super().display_details()
        print(f"Book Issue month: {self.issue_month}\n")

    def __del__(self):
        pass

lib=[]
book=[]
Magazin=[]

print("\n--- Library Management System ---\n")
while True:
    print('''Choose an operation:
1. Add a Book / Magazine
2. Show All Items
3. Update Items
4. Delete Items
5. Exit''')
    
    choice=int(input("\nEnter your choice:"))

    if choice == 1 :
        print('''\n- 1. Create Book
- 2. Crete Magazine''')
        
        subchoice=int(input("\nEnter Choice:"))
        if subchoice == 1:
            title=input("\nEnter Title:")
            publisher=input("Enter Publisher:")
            new_price=int(input("Enter Price:"))
            author=input("Enter Author:")
            number_of_pages=int(input("Enter Pages:"))

            bookobj=Book(title,publisher,new_price,author,number_of_pages)

            book.append(bookobj)

            print("\nBook successfully added!\n")

        elif subchoice == 2 :
            title=input("\nEnter Title:")
            publisher=input("Enter Publisher:")
            price=int(input("Enter Price:"))
            issue_month=int(input("Enter Issue Month:"))

            magobj=Magazine(title,publisher,price,issue_month)

            Magazin.append(magobj)

            print("\nMagazine successfully added!\n")  
        else:
            print("\nInvaild choice \n")     

    elif choice == 2:
        choice=int(input("\n1. View Magazine \n2. View Book\n3. All View\n\nEnter Choice:"))

        if choice == 2:
            for book_details in book:
                book_details.display_details()

        elif choice == 1:
            for mega_details in Magazin:
                mega_details.display_details()

        elif choice == 3:
            print("\n** Books **")
            for book_details in book:
                book_details.display_details()
                
            print("\n** Magazines **")
            for mega_details in Magazin:
                mega_details.display_details()

        else:
            print("\nInvaild choice!\n")

    elif choice == 3:
        update_choice = int(input("\n1. Update Book \n2. Update Magazine\n\nEnter Choice:"))

        if update_choice == 1:
            search_id = int(input("\nEnter Book ID: "))
            Found = False

            for iteam in book:
                if iteam.get_item_id() == search_id:
                    Found = True

                    new_title=input("\nEnter Title:")
                    new_publisher=input("Enter Publisher:")
                    new_new_price=int(input("Enter Price:"))
                    iteam.set_price(new_new_price)
                    new_author=input("Enter Author:")
                    new_number_of_pages=int(input("Enter Pages:"))

                    iteam.title = new_title
                    iteam.publisher = new_publisher
                    iteam.author = new_author
                    iteam.number_of_pages = new_number_of_pages

                    print("\nUpdated Successfully !\n")
                    break
            if Found == False:
                print("Error: Item ID not found!")

        elif update_choice == 2:
            search_id = int(input("\nEnter Book ID: "))
            Found = False

            for iteam in Magazin:
                if iteam.get_item_id() == search_id:
                    Found = True

                    new_title=input("\nEnter Title:")
                    new_publisher=input("Enter Publisher:")
                    new_price=int(input("Enter Price:"))
                    iteam.set_price(new_price)
                    new_issue_month=int(input("Enter Issue Month:"))

                    iteam.title = new_title
                    iteam.publisher = new_publisher
                    iteam.issue_month = new_issue_month

                    print("\nUpdated Successfully !\n")
                    break
            if Found == False:
                print("Error: Item ID not found!")

        else :
            print("Invaild Choice!")

        

    elif choice == 4:
        del_choice = int(input("\n1. Delete Book \n2. Delete Magazine\n\nEnter Choice: "))

        if del_choice == 1:
            search_id = int(input("Enter Book ID to delete: "))
            Found = False

            for item in book:
                if item.get_item_id() == search_id:
                    book.remove(item) 
                    Found = True
                    print("\nBook Deleted Successfully!\n")
                    break
            
            if Found == False:
                print("\nError: Item ID not found!\n")

        elif del_choice == 2:
            search_id = int(input("Enter Magazine ID to delete: "))
            Found = False
            for item in Magazin:
                if item.get_item_id() == search_id:
                    Magazin.remove(item)
                    Found = True
                    print("\nMagazine Deleted Successfully!\n")
                    break
            if Found == False:
                print("\nError: Item ID not found!\n")

    elif choice == 5:
        print("\nThank you for Visiting!\n")
        break

    else:
        print("\nInvaild choice!\n")
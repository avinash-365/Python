class JournalManager:
    def __init__(self):
        self.file = 'journal.txt'

    def add_entry(self):
        data = input("\nEnter your journal entry :\n")

        file_o = open(self.file,'a')
        file_o.write(data + '\n')
        file_o.close()

        print("\nEntry successfully added !\n")

    def view_entries(self):
        try:
            file_o = open(self.file,'r')
            content = file_o.read()

            if content == "":
                print("\nNo journal has been created yet; first, add a new entry.\n")
            else:
                print("\nYour Journal Entries:")
                print("-"*37)
                print(content)
            file_o.close()
        except FileNotFoundError:
            print("\nNo journal has been created yet; first, add a new entry.\n")

    def search_entries(self):
        search_data = input("\nEnter a word to search :")
        try:
            file_o = open(self.file,'r')
            found = False
            for line in file_o:
                if search_data in line:
                    found = True
                    print("\nMatching Enties:")
                    print("-"*38)
                    print(line)
            else:
                if not found:
                    print("\nNo matching entry was found.\n")
            file_o.close()
        except FileNotFoundError:
            print("\nThe journal file does not exist; create a new entry first.\n")

    def delete_entries(self):
        delete_file = input("\nAre you sure you want to delete all entries? (yes/no):").lower()

        try:
            if delete_file == "yes":
                file_o = open(self.file,'w')
                file_o.close()
                print("\nAll entries deleted successfully.\n")

        except FileNotFoundError:
                    print("The journal file does not exist; create a new entry first.")


journal = JournalManager()

print("-"*37)
print("Welcome to Personal Journal Manager!")
print("-"*37)

while True:
    try:
        choice = int(input('''Please select an option :
1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit

Enter Input: '''))
    except ValueError:
        print("\nEnter Valid Choice! (Please enter numbers only)\n")
        continue

    if choice == 1:
        journal.add_entry()

    elif choice == 2:
        journal.view_entries()

    elif choice == 3:
        journal.search_entries()

    elif choice == 4:
        journal.delete_entries()

    elif choice == 5:
        print("\nGoodbye!\n")
        break

    else:
        print("\nEnter Valid Choice!\n")
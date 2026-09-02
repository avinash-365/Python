# 📔 Personal Journal Manager

A simple **Object-Oriented Python** console application for managing personal journal entries.

This project is built to practice **Python OOP, File Handling, Exception Handling, Loops, Conditions, and String Operations** through a real-world mini project.

---

## 🚀 Features

* ➕ Add a New Journal Entry
* 📖 View All Journal Entries
* 🔍 Search Entries by Keyword
* 🗑️ Delete All Journal Entries
* ⚠️ Handle Missing Journal File
* ⚠️ Handle Invalid Menu Input
* 💾 Store entries permanently in a text file
* 🧱 Object-Oriented Programming structure

---

## 🛠️ Technologies Used

* **Python 3**
* **OOP (Object-Oriented Programming)**
* **File Handling**
* **Exception Handling**
* **String Operations**
* **Loops & Conditional Statements**

---

## 📂 Project Structure

```text
Personal-Journal-Manager/
│
├── journal_manager.py
├── journal.txt
└── README.md
```

> `journal.txt` is automatically created when the first journal entry is added.

---

## 📋 Menu

```text
-------------------------------------
Welcome to Personal Journal Manager!
-------------------------------------

Please select an option :

1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit
```

---

## ✨ How It Works

### 1️⃣ Add a New Entry

The user can enter a journal entry, which is stored inside `journal.txt`.

Example:

```text
Enter your journal entry :
Today I learned Python OOP.
```

The entry is saved automatically.

---

### 2️⃣ View All Entries

Displays all saved journal entries.

If the journal does not exist or contains no entries:

```text
No journal has been created yet; first, add a new entry.
```

---

### 3️⃣ Search for an Entry

The user can search for a specific word.

Example:

```text
Enter a word to search :Python
```

Matching entries are displayed.

---

### 4️⃣ Delete All Entries

The application asks for confirmation before deleting all journal entries.

```text
Are you sure you want to delete all entries? (yes/no):
```

If the user enters `yes`, all entries are removed.

---

### 5️⃣ Exit

Closes the application safely.

```text
Goodbye!
```

---

## 🧱 OOP Concept

The project uses a class called `JournalManager`.

```python
class JournalManager:
    def __init__(self):
        self.file = 'journal.txt'
```

The class contains methods for different journal operations:

```text
add_entry()
view_entries()
search_entries()
delete_entries()
```

This keeps the journal-related functionality organized inside one class.

---

## 📚 Python Concepts Practiced

| Concept            | Usage                             |
| ------------------ | --------------------------------- |
| Class              | `JournalManager`                  |
| Constructor        | `__init__()`                      |
| Object             | `journal = JournalManager()`      |
| Methods            | Journal operations                |
| File Handling      | Read / Write / Append             |
| `try-except`       | File & input errors               |
| `for` loop         | Searching entries                 |
| `if-else`          | Conditions                        |
| `while` loop       | Menu system                       |
| String Methods     | `.lower()`                        |
| User Input         | `input()`                         |
| Exception Handling | `ValueError`, `FileNotFoundError` |

---

## ▶️ How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Personal-Journal-Manager.git
```

### 2. Open the Project

```bash
cd Personal-Journal-Manager
```

### 3. Run the Program

```bash
python journal_manager.py
```

---

## 💡 Example

```text
-------------------------------------
Welcome to Personal Journal Manager!
-------------------------------------

Please select an option :
1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit

Enter Input: 1

Enter your journal entry :
Today I completed my Python OOP practice.

Entry successfully added!
```

---

## 🎯 Learning Objective

The main goal of this project is to strengthen Python programming fundamentals before moving toward more advanced concepts such as:

* Advanced OOP
* Data Structures
* NumPy
* Pandas
* Data Visualization
* Machine Learning
* Artificial Intelligence

---

## 🔮 Future Improvements

Possible future features:

* 📅 Add date and time to every entry
* ✏️ Edit an existing entry
* 🗑️ Delete a single entry
* 🔐 Password protection
* 📊 Journal statistics
* 🗂️ Categories for entries
* 💾 JSON/SQLite database storage
* 🎨 GUI version using Tkinter

---

## 👨‍💻 Author

**Avinash Vaghasiya**

Python & AI/ML Learner

---

## ⭐ Project Status

**Completed – Python OOP & File Handling Practice Project**

If you like this project, consider giving it a ⭐ on GitHub.
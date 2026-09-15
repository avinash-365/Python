# 🧰 Multi-Utility Toolkit

<p align="center">
  <b>A modular Python command-line toolkit for everyday utilities</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Project-Modular-success?style=for-the-badge" alt="Modular">
  <img src="https://img.shields.io/badge/Interface-CLI-orange?style=for-the-badge" alt="CLI">
  <img src="https://img.shields.io/badge/License-MIT-purple?style=for-the-badge" alt="License">
</p>

---

## 📌 About The Project

**Multi-Utility Toolkit** is a modular Python command-line application that brings several useful utilities into one simple menu-driven program.

The project is designed to practice and demonstrate:

- Python modules and packages
- Function creation and reuse
- `import` and `from ... import ...`
- `datetime` and `time`
- Mathematical calculations
- Random data generation
- UUID generation
- File handling
- Exception handling
- Input validation
- `importlib`
- `dir()` for module exploration
- Menu-driven CLI programming
- Code organization using custom modules

Instead of writing every feature inside one large Python file, the project separates functionality into smaller modules. This makes the application easier to understand, maintain, reuse, and extend.

---

## ✨ Features

### 🕒 1. Date & Time Operations

The toolkit provides several date and time utilities:

- Display the current date and time
- Calculate the difference between two dates
- Format dates into different formats
- Start a stopwatch
- Start a countdown timer

Example formats supported:

```text
DD/MM/YYYY
YYYY-MM-DD
DD Month, YYYY
DD-MM-YYYY HH:MM:SS
```

The date/time module uses Python's `datetime` and `time` libraries.

---

### 🧮 2. Mathematical Operations

The mathematical module provides:

- Factorial calculation
- Compound interest calculation
- Trigonometric calculations
- Circle area
- Rectangle area
- Triangle area

Supported trigonometric functions:

```text
1. Sine
2. Cosine
3. Tangent
```

The module uses Python's built-in `math` library.

---

### 🎲 3. Random Data Generation

The random module provides:

- Random number generation
- Random list generation
- Random password generation
- Random OTP generation

Password generation uses:

- Letters
- Numbers
- Special characters

---

### 🆔 4. UUID Generation

The toolkit can generate a unique identifier using Python's `uuid` module.

Example:

```text
Generated UUID:
7b8f0b8e-1a3e-4c5d-9b42-8f7c9d2e1234
```

Every generated UUID is intended to be unique.

---

### 📁 5. File Operations

The custom file module supports:

- Create a new file
- Write data to a file
- Read file content
- Append data to a file

The module also handles common file errors such as:

```text
File already exists
File not found
Other file-related errors
```

---

### 🔍 6. Module Attribute Explorer

The application includes a small learning-oriented feature using:

```python
dir()
```

The user can enter a module name, and the application imports it dynamically using:

```python
importlib.import_module()
```

Then it displays the available attributes of that module.

This feature is useful for understanding Python modules and introspection.

---

## 🗂️ Project Structure

```text
Multi-Utility-Toolkit/
│
├── moduler.py
│
├── modules/
│   ├── __init__.py
│   ├── date_time_ops.py
│   ├── math_ops.py
│   ├── random_ops.py
│   ├── uuid_ops.py
│   └── file_ops.py
│
└── README.md
```

> The exact folder name of the package can be changed as required by the project setup.

---

## 🧩 Module Overview

| Module | Purpose |
|---|---|
| `moduler.py` | Main application and menu system |
| `__init__.py` | Exports functions from custom modules |
| `date_time_ops.py` | Date, time, stopwatch and countdown utilities |
| `math_ops.py` | Mathematical and geometry utilities |
| `random_ops.py` | Random number, list, password and OTP utilities |
| `uuid_ops.py` | UUID generation |
| `file_ops.py` | File creation, writing, reading and appending |
| `README.md` | Project documentation |

---

## 🔗 Custom Module Imports

The main program imports reusable functions from the package.

For example:

```python
from modules import (
    get_current_datetime,
    calculate_date_difference,
    format_custom_date,
    start_stopwatch,
    start_countdown,
    fact,
    calculate_compound_interest,
    area_circle,
    area_rectangle,
    area_triangle,
    calculate_trig,
    generate_random_number,
    generate_random_list,
    create_random_password,
    generate_random_otp,
    generate_unique_id,
    create_file,
    write_to_file,
    read_from_file,
    append_to_file
)
```

This keeps the main application connected to smaller reusable modules instead of duplicating code.

---

# 🧠 Detailed Module Documentation

## 🕒 Date & Time Module

File:

```text
modules/date_time_ops.py
```

The date/time module contains five main functions.

### `get_current_datetime()`

Displays the current date and time.

Example:

```text
Current Date and Time: 2026-09-15 13:20:45
```

---

### `calculate_date_difference()`

Calculates the number of days between two dates.

Input format:

```text
DD-MM-YYYY
```

Example:

```text
Enter first Date (DD-MM-YYYY) Formate: 01-09-2026
Enter Second Date (DD-MM-YYYY) Formate: 15-09-2026

14 Days
```

The implementation uses Python `datetime` objects and calculates the absolute difference in days.

---

### `format_custom_date()`

Formats a supplied date according to the selected option.

| Option | Format | Example |
|---|---|---|
| 1 | DD/MM/YYYY | `15/09/2026` |
| 2 | YYYY-MM-DD | `2026-09-15` |
| 3 | DD Month, YYYY | `15 September, 2026` |
| 4 | DD-MM-YYYY HH:MM:SS | `15-09-2026 13:20:45` |

---

### `start_stopwatch()`

Starts timing when the user presses Enter and stops when Enter is pressed again.

Example:

```text
Press ENTER to START the stopwatch...
Stopwatch started! Running...

Press ENTER to STOP the stopwatch...

Elapsed Time: 5.42 seconds
```

---

### `start_countdown()`

Starts a countdown for a specified number of seconds.

Example:

```text
Countdown started for 5 seconds...
Time remaining: 5s
Time remaining: 4s
Time remaining: 3s
Time remaining: 2s
Time remaining: 1s

Time's up! Alert! Alert! ⏰
```

---

# 🧮 Mathematical Module

File:

```text
modules/math_ops.py
```

The math module contains reusable mathematical functions.

### `fact()`

Calculates factorial using Python's `math.factorial()`.

Example:

```text
Enter Number to Find of Factorial: 5

Factorial Num is: 120
```

---

### `calculate_compound_interest()`

Calculates compound interest using:

```text
A = P × (1 + R/100)^T
```

Where:

- `P` = Principal amount
- `R` = Rate of interest
- `T` = Time
- `A` = Total amount

The function returns:

```python
total_amount, interest
```

Example:

```text
Principal = 10000
Rate = 5
Time = 2

Compound Interest: 11025.0
```

---

### `calculate_trig()`

Converts degrees into radians and calculates:

```text
sin()
cos()
tan()
```

Example:

```text
Select function (1-3): 1
Enter angle in degrees: 30

Result: 0.5
```

The tangent function also checks angles where tangent is undefined.

---

### Geometry Functions

#### Circle

```python
area_circle(radius)
```

Formula:

```text
Area = π × r²
```

Example:

```text
Radius = 5
Area of Circle: 78.54
```

#### Rectangle

```python
area_rectangle(length, width)
```

Formula:

```text
Area = length × width
```

Example:

```text
Length = 10
Width = 5
Area of Rectangle: 50.0
```

#### Triangle

```python
area_triangle(base, height)
```

Formula:

```text
Area = 1/2 × base × height
```

Example:

```text
Base = 10
Height = 5
Area of Triangle: 25.0
```

---

# 🎲 Random Operations Module

File:

```text
modules/random_ops.py
```

### `generate_random_number()`

Generates a random integer within the selected range.

Example:

```text
Enter starting range: 1
Enter ending range: 100

Generated Random Number: 57
```

> The actual result changes because it is randomly generated.

---

### `generate_random_list()`

Creates a list containing randomly generated integers.

Example:

```text
Enter number of elements for the list: 5
Enter minimum value: 1
Enter maximum value: 50

Generated Random List: [12, 45, 7, 31, 19]
```

---

### `create_random_password()`

Creates a random password containing characters from:

```text
Letters
Numbers
! @ # $ % ^ & *
```

Example:

```text
Enter password length: 10

Generated Password: A7@kP2#x9Q
```

> Example output is only for demonstration. Actual generated passwords will vary.

---

### `generate_random_otp()`

Generates an OTP with the requested number of digits.

Example:

```text
Enter OTP length (e.g. 4 or 6): 6

Generated OTP: 583214
```

> The OTP is randomly generated and will be different on each execution.

---

# 🆔 UUID Module

File:

```text
modules/uuid_ops.py
```

The UUID module uses Python's `uuid.uuid4()` function.

Function:

```python
generate_unique_id()
```

Example:

```text
Generate Unique Identifiers:
Generated UUID: 7b8f0b8e-1a3e-4c5d-9b42-8f7c9d2e1234
```

---

# 📁 File Operations Module

File:

```text
modules/file_ops.py
```

### Create File

Function:

```python
create_file(filename)
```

Creates a new file using exclusive creation mode.

Example:

```text
Enter file name: notes.txt

File created successfully!
```

If the file already exists:

```text
Error: File 'notes.txt' already exists!
```

---

### Write to File

Function:

```python
write_to_file(filename, content)
```

Writes the supplied content into the file.

Example:

```text
Enter file name: notes.txt
Enter data to write: Hello Python

Data written successfully!
```

---

### Read File

Function:

```python
read_from_file(filename)
```

Reads and displays the complete file content.

Example:

```text
Enter file name: notes.txt

File Content:
Hello Python
```

If the file does not exist:

```text
Error: File 'notes.txt' not found!
```

---

### Append to File

Function:

```python
append_to_file(filename, content)
```

Adds new content to an existing file.

Example:

```text
Enter file name: notes.txt
Enter data to append: Learning modules

Data appended successfully!
```

---

# 🔎 Module Attribute Explorer

The main application includes an educational module exploration feature.

The user enters a module name:

```text
Enter module name to explore: math
```

The program dynamically imports the module:

```python
module_obj = importlib.import_module(mod_name)
```

Then:

```python
attributes = dir(module_obj)
```

The program displays the available attributes.

Example:

```text
Explore Module Attributes:
Enter module name to explore: math

Available Attributes in math module:
['__doc__', '__loader__', '__name__', '__package__',
 '__spec__', 'acos', 'acosh', 'asin', 'asinh', ...]
```

If the module is not available:

```text
Error: Module 'abc' not found! Please check the spelling.
```

---

# 🖥️ Main Menu

When the application starts, the user sees:

```text
===================================
Welcome to Multi-Utility Toolkit
===================================

Choose an option:
    1. Datetime and Time Operations
    2. Mathematical Operations
    3. Random Data Generation
    4. Generate Unique Identifiers (UUID)
    5. File Operation (Custom Module)
    6. Explore Module Attributes (dir())
    7. Exit
===================================
Enter Your Choice:
```

---

# 🧭 Application Flow

```text
                    ┌──────────────────────┐
                    │ Start Application    │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    Main Menu         │
                    └──────────┬───────────┘
                               │
          ┌────────────────────┼─────────────────────┐
          │                    │                     │
          ▼                    ▼                     ▼
   Date & Time             Mathematics          Random Data
          │                    │                     │
          ▼                    ▼                     ▼
    Select Utility       Select Utility        Select Utility
          │                    │                     │
          └────────────────────┼─────────────────────┘
                               │
          ┌────────────────────┼─────────────────────┐
          │                    │                     │
          ▼                    ▼                     ▼
        UUID             File Operations       Module Explorer
          │                    │                     │
          └────────────────────┼─────────────────────┘
                               │
                               ▼
                         Back to Menu
                               │
                               ▼
                             Exit
```

---

# 📸 Sample Outputs

## Date & Time

```text
===================================
Datetime and Time Operations:
===================================

1. Display current date and time
2. Calculate difference between two dates/times
3. Formate date into custom format
4. stopwatch
5. Countdown Timer
6. Back to Main Menu

Enter Your Choice: 1

Current Date and Time: 2026-09-15 13:20:45
```

---

## Factorial

```text
===================================
Mathmatical Operations:
===================================

1. Calculate Factorial
2. Solve compound Interest
3. Trigonometric Calculations
4. Area of Geometric Shapes
5. Back to Main Menu

Enter Your Choice: 1

Enter Number to Find of Factorial: 5

Factorial Num is: 120
```

---

## Random Number

```text
===================================
Random Data Generation:
===================================

1. Generate Random Number
2. Generate Random List
3. Create Random Password
4. Generate Random OTP
5. Back to Main Menu

Enter Your Choice: 1

Enter starting range: 1
Enter ending range: 100

Generated Random Number: 57
```

---

## UUID

```text
Generate Unique Identifiers:
Generated UUID: 7b8f0b8e-1a3e-4c5d-9b42-8f7c9d2e1234
===================================
```

---

## File Operation

```text
===================================
File Operations:
===================================

1. Create a new file
2. Write to a file
3. Read from a file
4. Append to a file
5. Back to Main Menu

Enter your choice: 1

Enter file name: notes.txt

File created successfully!
```

---

# 🛡️ Error Handling

The project includes input validation and exception handling.

Examples include:

### Invalid menu input

```text
Error: Please Enter Vaild Number !
```

### Invalid date

```text
Error: Invalid date format! Please use DD-MM-YYYY.
```

### Negative values

```text
Error: Values cannot be negative!
```

### Invalid countdown

```text
Error: Please enter a positive number!
```

### Invalid password length

```text
Error: Password length should be at least 4 characters!
```

### Missing file

```text
Error: File 'notes.txt' not found!
```

### Missing module

```text
Error: Module 'abc' not found! Please check the spelling.
```

These checks make the CLI application more user-friendly and prevent many common input errors.

---

# 🧱 Programming Concepts Used

This project is mainly focused on Python fundamentals and modular programming.

| Concept | Usage |
|---|---|
| Functions | Each utility is implemented as a function |
| Modules | Features are divided into separate files |
| Package | `__init__.py` exposes custom functions |
| Imports | Functions and libraries are imported where needed |
| `datetime` | Date and time calculations |
| `time` | Stopwatch and countdown |
| `math` | Mathematical operations |
| `random` | Random data generation |
| `string` | Password character sets |
| `uuid` | Unique identifier generation |
| File Handling | Create, write, read and append |
| Exception Handling | `try`, `except` |
| Input Validation | Checks invalid and negative input |
| `importlib` | Dynamic module importing |
| `dir()` | Module attribute exploration |
| Loops | Repeated menu interaction |
| Conditional Statements | Menu selection and validation |
| f-strings | Formatted output |

---

# 📦 Python Libraries Used

The project uses standard Python libraries, so no external package installation is required.

### `datetime`

Used for:

```python
datetime.datetime.now()
datetime.datetime.strptime()
```

### `time`

Used for:

```python
time.time()
time.sleep()
```

### `math`

Used for:

```python
math.factorial()
math.radians()
math.sin()
math.cos()
math.tan()
math.pi
```

### `random`

Used for:

```python
random.randint()
random.choice()
```

### `string`

Used for:

```python
string.ascii_letters
string.digits
```

### `uuid`

Used for:

```python
uuid.uuid4()
```

### `importlib`

Used for dynamic module loading:

```python
importlib.import_module()
```

---

# ⚙️ Requirements

Before running the project, make sure Python 3.x is installed.

Check Python version:

```bash
python --version
```

or:

```bash
python3 --version
```

No third-party packages are required.

---

# 🚀 Installation & Setup

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/Multi-Utility-Toolkit.git
```

Replace:

```text
your-username
```

with your GitHub username.

---

## 2. Open the Project

```bash
cd Multi-Utility-Toolkit
```

---

## 3. Check the Project Structure

Make sure the custom module package is available:

```text
moduler.py
modules/
├── __init__.py
├── date_time_ops.py
├── math_ops.py
├── random_ops.py
├── uuid_ops.py
└── file_ops.py
```

---

## 4. Run the Application

```bash
python moduler.py
```

---

# ▶️ How To Use

1. Run `moduler.py`.
2. Select an option from the main menu.
3. Select the required utility.
4. Enter the requested input.
5. View the generated result.
6. Use the back option to return to the previous menu.
7. Select Exit to close the application.

---

# 🔄 Example Complete Session

```text
===================================
Welcome to Multi-Utility Toolkit
===================================

Choose an option:
    1. Datetime and Time Operations
    2. Mathematical Operations
    3. Random Data Generation
    4. Generate Unique Identifiers (UUID)
    5. File Operation (Custom Module)
    6. Explore Module Attributes (dir())
    7. Exit
===================================

Enter Your Choice: 2

===================================
Mathmatical Operations:

1. Calculate Factorial
2. Solve compound Interest
3. Trigonometric Calculations
4. Area of Geometric Shapes
5. Back to Main Menu
===================================

Enter Your Choice: 1

Enter Number to Find of Factorial: 5

Factorial Num is: 120
```

---

# 🎯 Learning Objectives

This project helps strengthen practical understanding of:

- How Python modules work
- How packages are structured
- How functions can be reused
- How to organize a larger Python program
- How to work with standard libraries
- How to handle user input
- How to handle runtime errors
- How to work with files
- How dynamic imports work
- How `dir()` can be used for introspection
- How a CLI menu system can be designed

---

# 🌟 Why This Project?

A beginner Python program often places all code inside one file.

This project takes a more organized approach:

```text
One large program
       ↓
Separate responsibilities
       ↓
Reusable functions
       ↓
Custom modules
       ↓
Package
       ↓
Main application
```

This structure is a useful step toward writing cleaner and more maintainable Python applications.

---

# 📐 Design Approach

The application follows a simple modular design.

```text
                 Main Program
                 moduler.py
                      │
        ┌─────────────┼─────────────┐
        │             │             │
        ▼             ▼             ▼
   Date & Time      Math         Random
     Module         Module        Module
        │             │             │
        └─────────────┼─────────────┘
                      │
             ┌────────┴────────┐
             │                 │
             ▼                 ▼
          UUID Module       File Module
```

Each module focuses on a specific responsibility.

---

# 🧪 Testing Examples

The application can be manually tested with cases such as:

| Feature | Test Input | Expected Result |
|---|---|---|
| Current Date | `1` | Current date/time |
| Date Difference | Two valid dates | Difference in days |
| Date Format | `1-4` | Selected date format |
| Factorial | `5` | `120` |
| Compound Interest | `10000, 5, 2` | `11025.0` |
| Sine | `30°` | Approximately `0.5` |
| Circle | `r=5` | Approximately `78.54` |
| Random Number | `1-100` | Number in range |
| Random List | `5, 1-50` | 5 random values |
| Password | `10` | 10-character password |
| OTP | `6` | 6-digit OTP |
| UUID | No input | UUID string |
| Create File | `notes.txt` | File created |
| Read File | Existing file | File content |
| Module Explorer | `math` | Module attributes |

---

# ⚠️ Notes

- Random outputs are different on different executions.
- UUID values are different on different executions.
- Date/time output depends on the system clock.
- File operations work with files accessible from the application's current working directory.
- Date input should follow the expected `DD-MM-YYYY` format.
- The current implementation uses a command-line interface.
- No external Python packages are required.

---

# 🔮 Future Improvements

The current project can be extended with additional features.

Possible improvements:

- Add a graphical user interface using Tkinter
- Add more mathematical operations
- Add percentage and unit converters
- Add currency conversion
- Add temperature conversion
- Add length and weight conversion
- Add a BMI calculator
- Add a simple calculator
- Add more date utilities
- Add calendar generation
- Add stronger password generation
- Add password strength checking
- Add secure OTP generation
- Add JSON file operations
- Add CSV file operations
- Add file deletion and rename options
- Add logging
- Add automated tests
- Add configuration support
- Add a cleaner CLI interface
- Add colored terminal output
- Add command-line arguments
- Add documentation for every public function

---

# 🤝 Contributing

Contributions are welcome.

A simple contribution workflow:

```bash
git clone <repository-url>
cd Multi-Utility-Toolkit
```

Create a new branch:

```bash
git checkout -b feature/new-utility
```

Make your changes, test them, and commit:

```bash
git add .
git commit -m "Add new utility"
```

Push the branch:

```bash
git push origin feature/new-utility
```

Then create a Pull Request.

---

# 📄 License

This project is available for learning and development purposes.

If you add a specific open-source license to the repository, update this section accordingly.

---

# 👨‍💻 Author

**Avinash Vaghasiya**

Diploma in Computer Engineering Graduate  
AI & ML with Data Science Student

---

# ⭐ Project Highlights

```text
✓ Modular Python Architecture
✓ Custom Package
✓ Multiple Utility Modules
✓ Date & Time Tools
✓ Mathematical Tools
✓ Random Data Tools
✓ UUID Generator
✓ File Handling
✓ Exception Handling
✓ Input Validation
✓ Dynamic Module Import
✓ dir() Module Explorer
✓ Beginner-Friendly CLI
✓ Standard Python Libraries Only
```

---

# 📊 Feature Summary

```text
Date & Time
├── Current Date & Time
├── Date Difference
├── Custom Date Formatting
├── Stopwatch
└── Countdown

Mathematics
├── Factorial
├── Compound Interest
├── Sine
├── Cosine
├── Tangent
├── Circle Area
├── Rectangle Area
└── Triangle Area

Random Data
├── Random Number
├── Random List
├── Random Password
└── Random OTP

Other Utilities
├── UUID Generator
├── Create File
├── Write File
├── Read File
├── Append File
└── Module Attribute Explorer
```

---

# 🏁 Conclusion

**Multi-Utility Toolkit** is a practical Python project that combines multiple everyday utilities into one modular command-line application.

The project demonstrates how a Python application can be divided into reusable modules while keeping the main program focused on user interaction and menu management.

It is especially useful for practicing Python fundamentals, standard libraries, custom packages, exception handling, file operations, random data generation, and module introspection.

---

<p align="center">
  <b>Built with Python 🐍</b>
</p>

<p align="center">
  ⭐ If you find this project useful, consider giving the repository a star!
</p>

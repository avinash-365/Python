# Bank Management System

This is a console-based Bank Management System built with Python. It is designed to simulate real-world banking operations while demonstrating a strong understanding of core Object-Oriented Programming (OOP) principles. 

## Features

*   **Account Creation:** Open a Savings Account (includes an interest rate) or a Current Account (includes an overdraft limit).
*   **Core Banking:** Deposit, withdraw, and securely transfer money between different bank accounts.
*   **Transaction Statements:** View a detailed history of all transactions with real-time dates.
*   **Information Retrieval:** Look up comprehensive customer and account details using a unique 14-digit account number.
*   **Security & Validation:** Prevents negative deposits, blocks transfers to the same account, and enforces overdraft and balance limits.

## OOP Concepts Used

*   **Encapsulation:** Account balances are kept private and can only be modified through secure getter and setter methods.
*   **Inheritance:** The system uses hierarchical structures (e.g., a `customer` inherits from a `person`).
*   **Abstraction:** An abstract base `account` class acts as a strict blueprint for specific account types.
*   **Custom Exceptions:** Custom error handling ensures the program gracefully catches invalid amounts or insufficient funds without crashing.

## How to Run

1. Ensure you have Python 3 installed on your system.
2. Save the code to a file named `bank_system.py`.
3. Open your terminal or command prompt and run the command: `python bank_system.py` to interact with the main menu.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

class ExpenseTracker:

    def __init__(self):
        try:
            self.data = pd.read_csv("expenses.csv")
            
            self.data['Amount'] = self.data['Amount'].fillna(0.0)
            
            self.data['Category'] = self.data['Category'].fillna('Other')
            
            self.data['Description'] = self.data['Description'].fillna('No Description')
            
            self.data['Date'] = self.data['Date'].fillna('Unknown Date')

            self.data.to_csv("expenses.csv", index=False)

        except FileNotFoundError:
            self.data = pd.DataFrame(columns=['Date', 'Amount', 'Category', 'Description'])

    def add_expense(self, date, amount, category, description):
        valid_categories = ['Food', 'Transport', 'Utilities', 'Entertainment']

        if amount <= 0:
            print("\nError : Please enter valid positive amount.\n")

        elif category not in valid_categories:
            print(f"\nError : Invalid category. Please choose from {valid_categories}\n")

        else:
            self.data.loc[len(self.data)] = [date, amount, category, description]
            self.data.to_csv("expenses.csv", index=False)
            print("\nExpense added successfully!\n")

    def get_summary(self):
        if self.data.empty:
            print("\nNo expenses have been added yet.\n")
        else:
            total_expense = np.sum(self.data['Amount'])
            
            print("--- Spending Percentage by Category ---")
            category_totals = self.data.groupby('Category')['Amount'].sum()
            spending_percentage = (category_totals / total_expense) * 100
            print(spending_percentage.round(2).astype(str) + " %")
            print("=" * 36 + "\n")
            
            print("--- Monthly Average Spending ---")
            temp_df = self.data.copy()

            temp_df['Date'] = pd.to_datetime(temp_df['Date'], errors='coerce')
            temp_df['Month'] = temp_df['Date'].dt.to_period('M')
            monthly_avg = temp_df.groupby('Month')['Amount'].mean()
            print(monthly_avg.round(2))
            print("=" * 36 + "\n")

            print("--- Detailed Statistical Summary ---")
            print(self.data['Amount'].describe())
            print("=" * 36 + "\n")

    def filter_expenses(self, condition):
        if self.data.empty:
            print("\nNo expenses have been added yet.\n")
        else:
            filtered_data = self.data[self.data['Category'] == condition]
            
            if filtered_data.empty:
                print(f"\nNo expenses found for category: {condition}\n")
            else:
                print(f"\n--- Expenses for {condition} ---")
                print(filtered_data)
                print("-" * 30)

    def generate_report(self):
        if len(self.data) == 0:
            print("Not enough data for graphs.")
            return
            
        print("Loading Graphs...")
        
        cat_totals = self.data.groupby('Category')['Amount'].sum()
        date_totals = self.data.groupby('Date')['Amount'].sum()

        fig, ax = plt.subplots(2, 2, figsize=(12, 10))
        
        sns.barplot(x=cat_totals.index, y=cat_totals.values, ax=ax[0, 0], palette='Blues_r')
        ax[0, 0].set_title('Category Totals')
        ax[0, 0].set_ylabel('Amount')
        
        colors = sns.color_palette('pastel') 
        ax[0, 1].pie(cat_totals.values, labels=cat_totals.index, autopct='%1.1f%%', colors=colors)
        ax[0, 1].set_title('Spending Percentage')
        
        sns.lineplot(x=date_totals.index, y=date_totals.values, ax=ax[1, 0], marker='o', color='red')
        ax[1, 0].set_title('Daily Spending')
        ax[1, 0].tick_params(axis='x', rotation=45) 

        sns.histplot(self.data['Amount'], bins=10, ax=ax[1, 1], kde=True, color='green')
        ax[1, 1].set_title('Amount Frequency')
        ax[1, 1].set_xlabel('Amount')
        
        plt.tight_layout(pad=3.0)
        plt.savefig('chart.png')
        plt.show()

tracker = ExpenseTracker()

while True:
    print("="*30)
    print("   SMART EXPENSE TRACKER")
    print("="*30)
    print("1. Add New Expense")
    print("2. View Summary")
    print("3. Filter Expenses by Category")
    print("4. Generate Financial Report")
    print("5. Exit")
    
    choice = input("\nEnter your choice (1-5): ")
    
    if choice == '1':
        date = input("Enter Date (YYYY-MM-DD): ")
        try:
            datetime.datetime.strptime(date, "%Y-%m-%d")
            amount = float(input("Enter Amount: "))
            category = input("Enter Category (Food, Transport, Utilities, Entertainment): ").strip().capitalize()
            
            description = input("Enter Description: ").strip()
            if description == "":
                description = "No Description"
            
            tracker.add_expense(date, amount, category, description)
        except ValueError as e:
            print("\nError: Invalid Input! Make sure the Date is 'YYYY-MM-DD' and Amount is a number.\n")
            
    elif choice == '2':
        tracker.get_summary()
        
    elif choice == '3':
        condition = input("Enter category to filter (e.g., Food, Transport): ")
        tracker.filter_expenses(condition)
        
    elif choice == '4':
        tracker.generate_report()
        
    elif choice == '5':
        print("\nExiting Smart Expense Tracker. Goodbye!\n")
        break
        
    else:
        print("\nInvalid choice! Please enter a number between 1 and 5.\n")
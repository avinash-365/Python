import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class SaleDataAnalyzer:

    def __init__(self):
        self.df = None
        self.path = None
        self.figure = None

    def __del__(self):
        pass

    def load_data(self):

        try:
            self.path = input("\nEnter the path of the dataset (CSV file) :")
            self.df = pd.read_csv(self.path)
            print("\nDataset loaded Successfully!\n") 

        except FileNotFoundError:
            print("\nError: Please Enter Valid File!\n")

    def explore_data(self):

        if self.df is None:
            print("\nError: Please first load Data!\n")

        else:
            print("\n== Explore Data ==")
            print('''1. Display the first 5 rows
2. Display the last 5 rows
3. Display column names
4. Display data types
5. Display basic info''')
            
            try:
                choice = int(input("\nEnter Your Choice :"))

                if choice == 1:
                    print("\nFirst 5 Rows :")
                    print(self.df.head())
                    print()

                elif choice == 2:
                    print("\nLast 5 Rows :")
                    print(self.df.tail())
                    print()

                elif choice == 3:
                    print("\nColumn Names :")
                    print(list(self.df.columns))
                    print()

                elif choice == 4:
                    print("\nData Types :")
                    print(self.df.dtypes)
                    print()

                elif choice == 5:
                    print("\nBasic Info :")
                    print(self.df.info())
                    print()

                else:
                    print("\nError : Please Select number (1-5)\n")

            except ValueError:
                print("\nError : Please Enter Valid Number!\n")

    def data_operations(self):

        if self.df is None:
            print("\nError: Please first load Data!\n")

        else:
            print("\n== DataFrame Operation ==")

            try:
                col = input("\nEnter column name: ")
                print(self.df[col].agg(['sum','std','min','max']))
                print()

            except KeyError:
                print("\nError: Please Enter Valid column name\n")

    def clean_data(self):

        if self.df is None:
            print("\nError: Please first load Data!\n")

        else:
            print("\n== Handle Missing Data ==")
            print('''1. Display rows with missing values
2. Fill missing values with mean
3. Drop rows with missing values
4. Replace missing values with a specific value''')
            
            try:
                choice = int(input("\nEnter Your Choice :"))
                null_columns = list(self.df.columns[self.df.isnull().any()])
                
                if choice == 1:
                    print("\nRows with missing values :")
                    print(self.df.isnull().sum())
                    print()

                elif choice == 2:
                    if not null_columns:
                        print("\nNo missing values found in the dataset!\n")

                    else:
                        for col in null_columns:
                            if self.df[col].dtypes in ['int64','float64']:
                                self.df[col] = self.df[col].fillna(self.df[col].mean())
                        print("\nFill null Value Successful!\n")

                elif choice == 3:
                    if not null_columns:
                        print("\nNo missing values found in the dataset!\n")

                    else:
                        self.df.dropna(inplace=True)
                        print("\nRow Delete Successful!\n")

                elif choice == 4:                        
                    if not null_columns:
                        print("\nNo missing values found in the dataset!\n")

                    else:
                        for col in null_columns:
                            if self.df[col].dtypes in ['int64','float64']:
                                self.df[col] = self.df[col].fillna(int(input("\nEnter Specific Value :")))
                        print("\nFill null Value Successful!\n")

                else:
                    print("\nError : Please Select number (1-4)\n")

            except ValueError:
                print("\nError : Please Enter Valid Number!\n")

    def statistical_analysis(self):

        if self.df is None:
            print("\nError: Please first load Data!\n")
        
        else:
            summary_stats = self.df.describe()
            print("\n== Summary Statistics ==\n")
            print(summary_stats)
            print()

    def visualize_data(self):

        if self.df is None:
            print("\nError: Please first load Data!\n")
        
        else:
            print("\n== Data Visualization ==")
            print('''1. Bar Plot
2. Line Plot
3. Scatter Plot
4. Pie Chart
5. Histogram
6. Stack Plot''')
            try:
                choice = int(input("\nEnter Your Choice :"))

                if choice < 1 or choice > 6:
                    print("\nError : Please Select number (1-6)\n")

                else:
                    if choice in [1, 2, 3, 6]:
                        x_axis = input("\nEnter x-axis column name: ")
                        y_axis = input("\nEnter y-axis column name: ")
                        
                        if x_axis in self.df.columns and y_axis in self.df.columns:
                            if choice == 1:
                                print("\nGenerating Bar plot....\n")
                                plt.xlabel(x_axis)
                                plt.ylabel(y_axis)
                                plt.title(f"Bar Plot: {x_axis} vs {y_axis}")
                                sns.barplot(x=x_axis, y=y_axis, data=self.df)
                                self.figure = plt.gcf()
                                plt.show()
                                plt.close()
                                print("Bar plot displayed successfully!\n")

                            elif choice == 2:
                                print("\nGenerating Line plot....\n")
                                plt.xlabel(x_axis)
                                plt.ylabel(y_axis)
                                plt.title(f"Line Plot: {x_axis} vs {y_axis}")
                                sns.lineplot(x=x_axis, y=y_axis, data=self.df)
                                self.figure = plt.gcf()
                                plt.show()
                                plt.close()
                                print("Line plot displayed successfully!\n")

                            elif choice == 3:
                                print("\nGenerating Scatter plot....\n")
                                plt.xlabel(x_axis)
                                plt.ylabel(y_axis)
                                plt.title(f"Scatter Plot: {x_axis} vs {y_axis}")
                                sns.scatterplot(x=x_axis, y=y_axis, data=self.df)
                                self.figure = plt.gcf()
                                plt.show()
                                plt.close()
                                print("Scatter plot displayed successfully!\n")

                            elif choice == 6:
                                print("\nGenerating Stack plot....\n")
                                plt.xlabel(x_axis)
                                plt.ylabel(y_axis)
                                plt.title(f"Stack Plot: {x_axis} vs {y_axis}")
                                plt.stackplot(self.df[x_axis], self.df[y_axis])
                                self.figure = plt.gcf()
                                plt.show()
                                plt.close()
                                print("Stack plot displayed successfully!\n")

                        else:
                            print("\nError : Please Enter Valid Column name\n")
                            
                    elif choice in [4, 5]:
                        column = input("\nEnter column name for visualization: ")
                        if column in self.df.columns:
                            if choice == 4: 
                                print("\nGenerating Pie Chart....\n") 
                                data_counts = self.df[column].value_counts() 
                                plt.title(f"Pie Chart of {column}") 
                                plt.pie(data_counts, labels=data_counts.index, autopct='%1.1f%%') 
                                self.figure = plt.gcf()
                                plt.show()
                                plt.close() 
                                print("Pie Chart displayed successfully!\n") 

                            elif choice == 5: 
                                print("\nGenerating Histogram....\n") 
                                plt.title(f"Histogram of {column}") 
                                plt.xlabel(column) 
                                plt.ylabel("Frequency") 
                                sns.histplot(self.df[column], kde=True)
                                self.figure = plt.gcf()
                                plt.show()
                                plt.close() 
                                print("Histogram displayed successfully!\n") 

                        else:
                            print("\nError : Please Enter Valid Column name\n")
            except ValueError:
                print("\nError : Please Enter Valid Number!\n")
                
    def save_chart(self):
        if self.figure is None:
            print("\nError: No visualization found! Please generate a plot first.\n")
            return
            
        print("\n== Save Visualization ==")

        try:
            name = input("\nEnter file name to save the plot (e.g., linechart.png) :")
            self.figure.savefig(name)
            print(f"\nVisualization saved as {name} successfully!\n")

        except ValueError:
            print("\nInvalid file name or format! Please use a valid name like linechart.png")

    def main_data(self):
        while True:
            print("============ Data Analysis & Visualization Program ============")
            print('''Please select an option:
1. Load Dataset
2. Explore Data
3. Perform DataFrame operation
4. Handle Missing Data
5. Generate Descriptive Statistics
6. Data Visualization
7. Save Visualization
8. Exit''')
            print("="*63)
            try:
                choice = int(input("\nEnter Your Choice :"))

                if choice == 1:
                    self.load_data()

                elif choice == 2:
                    self.explore_data()

                elif choice == 3:
                    self.data_operations()

                elif choice == 4:
                    self.clean_data()

                elif choice == 5:
                    self.statistical_analysis()

                elif choice == 6:
                    self.visualize_data()

                elif choice == 7:
                    self.save_chart()

                elif choice == 8:
                    print("\nExiting the program. Goodbye!\n")
                    break

                else:
                    print("\nError : Please Select number (1-8)\n")

            except ValueError:
                print("\nError : Please Enter Valid Number!\n")
                
            except IndexError:
                print("\nError : Index out of range! Please select a valid option.\n")

sale_analyzr = SaleDataAnalyzer()
sale_analyzr.main_data()
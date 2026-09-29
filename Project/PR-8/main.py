from oop import analyzer


def main():
    analyzer.welcome_meassage()

    while True:

        analyzer.display_menu()

        try:

            choice = int(input("Enter your choice: "))

            # 1. CREATE NUMPY ARRAY
            if choice == 1:

                print("\n--- Create NumPy Array ---")
                print("1. Create 1D Array")
                print("2. Create 2D Array")
                print("3. Create 3D Array")

                sub_choice = int(input("\nEnter your choice: "))

                if sub_choice == 1:
                    analyzer.create_1d_array()

                elif sub_choice == 2:
                    analyzer.create_2d_array()

                elif sub_choice == 3:
                    analyzer.create_3d_array()

                else:
                    print("Invalid choice!")

            # 2. MATHEMATICAL OPERATIONS
            elif choice == 2:

                if not analyzer.has_array():
                    print("\nPlease create an array first!\n")
                    continue

                print("\n--- Mathematical Operations ---")
                print("1. Addition")
                print("2. Subtraction")
                print("3. Multiplication")
                print("4. Division")

                math_choice = int(input("\nEnter your choice: "))

                analyzer.create_second_array_of_math_op()

                if math_choice == 1:
                    analyzer.add()
                    
                elif math_choice == 2:
                    analyzer.sub()
                    
                elif math_choice == 3:
                    analyzer.mul()
                
                elif math_choice == 4:
                    analyzer.divi()
                
                else:
                    print("Invalid choice!")

            # 3. INDEXING / SLICING
            elif choice == 3:

                if not analyzer.has_array():
                    print("\nPlease create an array first!\n")
                    continue

                analyzer.operation_3()

            # 4. SEARCH / SORT / FILTER
            elif choice == 4:

                if not analyzer.has_array():
                    print("\nPlease create an array first!\n")
                    continue

                analyzer.search_sort_filter()

            # 5. STATISTICS
            elif choice == 5:

                if not analyzer.has_array():
                    print("\nPlease create an array first!")
                    continue

                analyzer.statistics()

            # 6. EXIT
            elif choice == 6:

                print("\nThank you for using NumPy Analyzer!")
                break

            else:
                print("\nInvalid choice!")
                print("Please enter a number between 1 and 7.\n")

        # VALUE ERROR
        except ValueError:

            print("\nPlease enter a valid number.\n")

        # GENERAL EXCEPTION
        except Exception as e:

            print(f"\nError: {e}")


# PROGRAM START
if __name__ == "__main__":
    main()
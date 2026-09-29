import numpy as np
from abc import ABC, abstractmethod


class NumpyAnalyzer(ABC):

    # Class variable
    object_count = 0
    app_name = "NumPy Analyzer"

    def __init__(self):
        # Private instance variable
        self.__arrays = []

        # Calling a class variable through the class
        NumpyAnalyzer.object_count += 1

    # PROPERTY / ENCAPSULATION
    @property
    def array(self):
        """Getter for private __arrays."""
        return self.__arrays

    @array.setter
    def array(self, value):
        """Setter for private __arrays."""
        if not isinstance(value, list):
            raise TypeError("Array storage must be a list.")

        self.__arrays = value
        

    @classmethod
    def get_object_count(cls):
        """Returns number of analyzer objects created."""
        return cls.object_count

    @staticmethod
    def welcome_meassage():
        print("=" * 40)
        print("Welcome to the NumPy Analyzer!")
        print("=" * 40)

    @staticmethod
    def display_menu():
        """Static method because it does not need self or cls."""
    
        print("""Choose an option:
1. Create a Numpy Array
2. Perform Mathematical Operations
3. Combine or Split Arrays / Indexing & Slicing
4. Search, Sort, or Filter Arrays
5. Compute Aggregates and Statistics
6. Exit
""")

    @abstractmethod
    def module_name(self):
        """
        Every child class must provide its own module name.
        This demonstrates abstraction.
        """
        pass

    # SPECIAL METHOD
    def __str__(self):
        return (
            f"{self.app_name} | "
            f"Stored Arrays: {len(self.__arrays)}"
        )

    # COMMON METHOD
    def has_array(self):
        """Check whether at least one array exists."""
        return len(self.__arrays) > 0


class CreateArray(NumpyAnalyzer):
    """Child class for creating 1D, 2D and 3D arrays."""

    def __init__(self):
        super().__init__()

    # Method overriding
    def module_name(self):
        return "Create Array Module"

    def create_1d_array(self):
        user_input = input(
            "\nEnter elements separated by spaces: "
        )

        user_list = [int(x) for x in user_input.split()]
        user_array = np.array(user_list)

        self.array.append(user_array)

        print("\nYour NumPy array:")
        print(user_array)
        print()

    def create_2d_array(self):
        rows = int(input("\nEnter the number of rows: "))
        cols = int(input("Enter the number of columns: "))

        total = rows * cols

        raw_input = input(
            f"\nEnter all {total} elements separated by spaces: "
        )

        flat_list = list(map(int, raw_input.split()))

        if len(flat_list) != total:
            print(
                f"\nError: You must enter exactly {total} numbers."
            )
            return

        user_2d_array = np.array(flat_list).reshape(rows, cols)

        self.array.append(user_2d_array)

        print("\nYour 2D NumPy Array:")
        print(user_2d_array)
        print()

    def create_3d_array(self):
        depth = int(input("\nEnter depth: "))
        rows = int(input("Enter rows: "))
        cols = int(input("Enter columns: "))

        total = depth * rows * cols

        raw_input = input(
            f"\nEnter all {total} elements separated by spaces: "
        )

        flat_list = list(map(int, raw_input.split()))

        if len(flat_list) != total:
            print(
                f"\nError: You must enter exactly {total} numbers."
            )
            return

        user_3d_array = np.array(flat_list).reshape(
            depth, rows, cols
        )

        self.array.append(user_3d_array)

        print("\nGenerated 3D Array:")
        print(user_3d_array)
        print()

class MathOperation(CreateArray):
    """Child class for mathematical operations."""

    def __init__(self):
        super().__init__()

    # Method overriding
    def module_name(self):
        return "Mathematical Operation Module"

    def create_second_array_of_math_op(self):
        if not self.has_array():
            print("\nPlease create array first\n")
            return False

        first_array = self.array[0]
        size = first_array.size
        shape = first_array.shape

        user_input = input(
            f"Enter the same-size array elements "
            f"({size} elements separated by space): "
        )

        val_list = [int(x) for x in user_input.split()]
        new_array = np.array(val_list)

        if new_array.size != size:
            print(
                f"\nError: You were supposed to provide exactly "
                f"{size} numbers, but you provided "
                f"{new_array.size} numbers."
            )
            return False

        new_array = new_array.reshape(shape)
        self.array.append(new_array)

        print("\nOriginal array:")
        print(first_array)

        print("\nSecond array:")
        print(new_array)

        return True

    def add(self):
        print("\nResult of Addition:")
        print(np.add(self.array[0], self.array[-1]))
        print()

    def sub(self):
        print("\nResult of Subtraction:")
        print(np.subtract(self.array[0], self.array[-1]))
        print()

    def mul(self):
        print("\nResult of Multiplication:")
        print(np.multiply(self.array[0], self.array[-1]))
        print()

    def divi(self):
        print("\nResult of Division:")
        print(np.divide(self.array[0], self.array[-1]))
        print()


class CombineSplitArray(MathOperation):
    """Child class for indexing and slicing."""

    def __init__(self):
        super().__init__()

    # Method overriding
    def module_name(self):
        return "Indexing and Slicing Module"

    def operation_3(self):
        if not self.has_array():
            print("\nPlease create array first\n")
            return

        print("""
Choose an operation:
1. Indexing
2. Slicing
3. Go Back
""")

        sub_choice = int(input("\nEnter Your Choice: "))

        if sub_choice == 3:
            print("\nGoing Back to main menu...\n")
            return

        current_array = self.array[-1]
        array_shape = current_array.ndim

        if sub_choice == 1:
            self.index_array(current_array, array_shape)

        elif sub_choice == 2:
            self.slice_array(current_array, array_shape)

        else:
            print("\nInvalid Sub-choice!\n")

    def index_array(self, current_array, array_shape):
        print(f"\nOriginal Array:\n{current_array}")

        if array_shape == 1:
            idx = int(
                input(
                    f"\nEnter index (0 to "
                    f"{len(current_array) - 1}): "
                )
            )

            print(
                f"\nElement at index {idx}: "
                f"{current_array[idx]}\n"
            )

        elif array_shape == 2:
            row_idx = int(
                input(
                    f"Enter row index "
                    f"(0 to {current_array.shape[0] - 1}): "
                )
            )

            col_idx = int(
                input(
                    f"Enter column index "
                    f"(0 to {current_array.shape[1] - 1}): "
                )
            )

            print(
                f"\nElement at [{row_idx}, {col_idx}]: "
                f"{current_array[row_idx, col_idx]}\n"
            )

        elif array_shape == 3:
            d_idx = int(
                input(
                    f"Enter depth/matrix index "
                    f"(0 to {current_array.shape[0] - 1}): "
                )
            )

            row_idx = int(
                input(
                    f"Enter row index "
                    f"(0 to {current_array.shape[1] - 1}): "
                )
            )

            col_idx = int(
                input(
                    f"Enter column index "
                    f"(0 to {current_array.shape[2] - 1}): "
                )
            )

            print(
                f"\nElement at [{d_idx}, {row_idx}, {col_idx}]: "
                f"{current_array[d_idx, row_idx, col_idx]}\n"
            )

    def slice_array(self, current_array, array_shape):
        print("\n--- Slicing Guide ---")
        print("For 1D array: 0:2")
        print("For 2D array: 0:2, 1:3")
        print("For 3D array: 0:1, 0:2, 1:3")

        if array_shape == 1:
            print("\nOriginal Array:\n", current_array)

            start = int(input("\nEnter your slice start range: "))
            stop = int(input("Enter your slice stop range: "))

            sliced_array = current_array[start:stop]

        elif array_shape == 2:
            print("\nOriginal Array:\n", current_array)
            print("\nSelect Slicing Option:")
            print("1. Select a submatrix")
            print("2. Select an entire column")
            print("3. Select an entire row")

            slice_choice = int(
                input("Enter your choice (1, 2, or 3): ")
            )

            if slice_choice == 1:
                row_start = int(input("\nEnter row start range: "))
                row_stop = int(input("Enter row stop range: "))
                col_start = int(input("Enter column start range: "))
                col_stop = int(input("Enter column stop range: "))

                sliced_array = current_array[
                    row_start:row_stop,
                    col_start:col_stop
                ]

            elif slice_choice == 2:
                col_index = int(
                    input("\nEnter column index: ")
                )

                sliced_array = current_array[:, col_index]

            elif slice_choice == 3:
                row_index = int(
                    input("\nEnter row index: ")
                )

                sliced_array = current_array[row_index, :]

            else:
                print("\nInvalid choice!")
                return

        elif array_shape == 3:
            print("\nOriginal Array:\n", current_array)
            print("\n--- Custom 3D Sub-cube Slicing ---")

            d_start = int(input("Enter depth start range: "))
            d_stop = int(input("Enter depth stop range: "))
            row_start = int(input("Enter row start range: "))
            row_stop = int(input("Enter row stop range: "))
            col_start = int(input("Enter column start range: "))
            col_stop = int(input("Enter column stop range: "))

            sliced_array = current_array[
                d_start:d_stop,
                row_start:row_stop,
                col_start:col_stop
            ]

        else:
            print("Unsupported array dimensions.")
            return

        print("\nSliced Array:")
        print(sliced_array)
        print()


class SearchSortFilter(CombineSplitArray):
    """Child class for searching, sorting and filtering."""

    def __init__(self):
        super().__init__()

    # Method overriding
    def module_name(self):
        return "Search, Sort and Filter Module"

    def search_sort_filter(self):
        if not self.has_array():
            print("\nPlease create array first\n")
            return

        current_array = self.array[-1]

        print(f"\nCurrent Array:\n{current_array}")

        print("""
Choose an operation:
1. Search Array
2. Sort Array
3. Filter Array
""")

        sub_choice = int(input("Enter Your Choice: "))

        if sub_choice == 1:
            val = int(
                input("Enter the value to search for: ")
            )

            result = np.where(current_array == val)

            if len(result[0]) > 0:
                print(
                    f"\nElement {val} found at indices: "
                    f"{result}\n"
                )
            else:
                print(
                    f"\nElement {val} not found in the array.\n"
                )

        elif sub_choice == 2:
            print("\nSorted Array:")
            print(np.sort(current_array, axis=None))
            print()

        elif sub_choice == 3:
            val = int(
                input(
                    "Enter the threshold value "
                    "(filter elements > value): "
                )
            )

            filtered_array = current_array[current_array > val]

            print(
                f"\nFiltered Elements "
                f"(Greater than {val}):"
            )
            print(filtered_array)
            print()

        else:
            print("\nInvalid Choice!")


class StatisticsAnalyzer(SearchSortFilter):
    """Final child class for statistics."""

    def __init__(self):
        super().__init__()

    # Method overriding
    def module_name(self):
        return "Statistics Module"

    def statistics(self):
        if not self.has_array():
            print("\nPlease create array first\n")
            return

        current_array = self.array[-1]

        print(f"\nCurrent Array:\n{current_array}")

        print("""
Choose a statistical operation:
1. Sum of all elements
2. Mean (Average)
3. Median
4. Maximum and Minimum values
5. Standard Deviation
""")

        sub_choice = int(input("\nEnter Your Choice: "))

        if sub_choice == 1:
            print(
                f"\nSum of Array: "
                f"{np.sum(current_array)}\n"
            )

        elif sub_choice == 2:
            print(
                f"\nMean of Array: "
                f"{np.mean(current_array)}\n"
            )

        elif sub_choice == 3:
            print(
                f"\nMedian of Array: "
                f"{np.median(current_array)}\n"
            )

        elif sub_choice == 4:
            print(
                f"\nMaximum Value: "
                f"{np.max(current_array)}"
            )

            print(
                f"Minimum Value: "
                f"{np.min(current_array)}\n"
            )

        elif sub_choice == 5:
            print(
                f"\nStandard Deviation: "
                f"{np.std(current_array)}\n"
            )

        else:
            print("\nInvalid Choice!")

# OBJECT CREATION
analyzer = StatisticsAnalyzer()

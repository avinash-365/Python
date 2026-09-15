def create_file(filename):
    try:
        with open(filename, "x") as f:
            pass
        print("File created successfully!")
    except FileExistsError:
        print(f"Error: File '{filename}' already exists!")
    except Exception as e:
        print(f"Error: {e}")

def write_to_file(filename, content):
    try:
        with open(filename, "w") as f:
            f.write(content)
        print("Data written successfully!")
    except Exception as e:
        print(f"Error: {e}")

def read_from_file(filename):
    try:
        with open(filename, "r") as f:
            data = f.read()
        print("File Content:")
        print(data)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
    except Exception as e:
        print(f"Error: {e}")

def append_to_file(filename, content):
    try:
        with open(filename, "a") as f:
            f.write("\n" + content)
        print("Data appended successfully!")
    except Exception as e:
        print(f"Error: {e}")
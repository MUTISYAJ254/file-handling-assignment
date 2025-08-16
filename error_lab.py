# error_lab.py
# Error Handling Lab 🧪

filename = input("Enter the filename you want to read: ")

try:
    with open(filename, "r") as file:
        content = file.read()
        print("\n✅ File content:\n")
        print(content)
except FileNotFoundError:
    print("\n❌ Error: The file does not exist.")
except PermissionError:
    print("\n❌ Error: You don’t have permission to read this file.")
except Exception as e:
    print(f"\n❌ An unexpected error occurred: {e}")


def main():
    # Step 1: Ask the user for a file name
    filename = input("Enter the filename you want to read: ")

    try:
        # Step 2: Try opening and reading the file
        with open(filename, "r") as file:
            content = file.read()

        # Step 3: Modify the content
        modified_content = content.upper()

        # Step 4: Save the modified text to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"✅ Success! A new file '{new_filename}' has been created.")

    except FileNotFoundError:
        print("❌ Error: That file does not exist. Please check the name and try again.")
    except PermissionError:
        print("❌ Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")


# Run the program
if __name__ == "__main__":
    main()
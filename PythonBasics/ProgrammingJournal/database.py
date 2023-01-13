entries = []

# generally we want to have separate files to interact with the user and work with a data store instead of mixing it here
def add_entry():
    entry_content = input("What have you learned today? ")
    entry_date = input("Enter the date: ")

    entries.append({"content": entry_content, "date": entry_date})

def view_entries():
    for entry in entries:
        print(f"{entry['date']}\n{entry['content']}\n\n")


# def add_notes():
#     notes = input("Enter your note : - ")
#     with open("my_notes.txt", "a") as file:
#         file.write(f"{notes}\n")

# def view_notes():
#     try:
#         with open("my_notes.txt", "r") as file:
#           for line in file:
#             print(line.strip())
#     except FileNotFoundError:
#        print("file does not exist")
  
# add_notes()
# view_notes()

def add_notes():
    notes = input("Enter your note : - ")
    with open("my_notes.txt", "a") as file:
        file.write(f"{notes}\n")

def view_notes():
    try:
        with open("my_notes.txt", "r") as file:
          for line in file:
            print(line.strip())
    except FileNotFoundError:
       print("file does not exist")  

# def clear_notes():
#    with open("my_notes.txt", "w") as file:
#       pass
#    print("All Notes Succesfully Deleted")

def Delete_Note():
   remaining_notes = []
   note_to_delete = input("Enter the note you want to Delete: ")

   with open("my_notes.txt", "r") as file:
    lines = file.readlines()
    
    for line in lines:
       if line.strip() != note_to_delete:
          remaining_notes.append(line)

    with open("my_notes.txt", "w") as file:
            file.writelines(remaining_notes)

def edit_note():
    updated_notes = []
    note_to_edit = input("Enter the note you want to edit: ")
    new_note = input("Enter the new note: ")
    with open("my_notes.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            if line.strip() == note_to_edit:
                updated_notes.append(new_note + "\n")
            else:
                updated_notes.append(line)
    with open("my_notes.txt", "w") as file:
        file.writelines(updated_notes)

while True:
   print("\n")
   print("1. Add Note")
   print("2. View Notes")
   print("3. Edit Note")
   print("4. Delete Note")
   print("5. Exit")

   choice = input("choose an option: ")
   print("\n")

   if choice == "1":
    add_notes()

   elif choice == "2":
       view_notes()

   elif choice == "3":
    edit_note()

   elif choice == "4":
    Delete_Note()

   elif choice == "5":
     print("program end")
     break
   else: 
    print("Invalid choice")



    
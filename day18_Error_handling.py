
try:

    with open("my_notes.txt", "r") as file:
        for line in file:
            print(line.strip())

except FileNotFoundError:
     print("file does not exist")
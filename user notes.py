note = input("Please input a note: ")
note2 = input("Please input another note: ")
note3 = input("Please enter a final note: ")

f = open("notes.txt", "x")
with open("notes.txt", "w") as f:
    f.write(note + "\n")
    f.write(note2 + "\n")
    f.write(note3 + "\n")
    f.close()
with open("notes.txt", "r") as f:
    print(f.read())
    f.close()
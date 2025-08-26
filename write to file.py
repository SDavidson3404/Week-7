f = open("hello.txt", "x")
with open("hello.txt", "w") as f:
    f.write("Hello, World!")
    f.close()
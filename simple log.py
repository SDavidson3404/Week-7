import datetime

datetime = str(datetime.datetime.now())

log1 = input("Please enter a message: ")
log2 = input("Please enter another message: ")
log3 = input("Please enter a third message: ")

f = open("log.txt", "w")
f.write(datetime + " " + log1 + "\n")
f.write(datetime + " " + log2 + "\n")
f.write(datetime + " " + log3 + "\n")
f.close()
f = open("log.txt", "r")
print(f.read())
f.close()


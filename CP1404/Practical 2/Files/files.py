
out_file = open("name.txt", "w")
name = input("What is your name?")
print(name, file=out_file)
out_file.close()

in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print("Your name is ", name)

in_file = open("numbers.txt", "r")
number1 = int(in_file.readline())
number2 = int(in_file.readline())
in_file.close()
total = number1 + number2
print(total)

in_file = open("numbers.txt", "r")
number1 = int(in_file.readline())
number2 = int(in_file.readline())
number3 = int(in_file.readline())
in_file.close()
total = number1 + number2 + number3
print(total)
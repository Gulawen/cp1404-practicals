for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 101, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

num = int(input("Please enter the number of the *"))
for i in range(num):
    print("*", end='')

num = int(input("Please enter the line for the *"))
for i in range(1, num+1):
    print("*" * i)
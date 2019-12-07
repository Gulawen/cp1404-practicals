numbers = [3, 1, 4, 1, 5, 9, 2]
numbers2 =[6, 5, 3]
num1 = numbers[0]
num2 = numbers[-1]
num3 = numbers[3]
num4 = numbers[:-1]
num5 = numbers[3:4]
num6 = numbers[4]
num7 = numbers[6]
numbers.append( 6 )
numbers.append(5)
numbers.append(3)
del numbers[0]
numbers.insert( 0, "ten")
del numbers[9]
numbers.insert(9,1)
num8 = numbers[2:]
for i in numbers:
    if i==9:
        print("True")
print(num1, num2, num3, num4)
print(num5, num6, num7, )
print(numbers)
print(numbers)
print(numbers)
print(num8)
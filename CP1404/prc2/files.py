
def main():
    name = input("please enter the your name")
    file = open('name.txt', 'w')
    file.write(name)
    file.close()
    file = open('name.txt', 'r')
    thin = file.read()
    print("Your name is"+ thin)
    file.close()
    file = open('number.txt', 'w')
    file.write("17\n42\n400")
    file.close()
    file = open('number.txt', 'r')
    num1 = file.readline()
    num2 = file.readline()
    num3 = int(num1) +int(num2)
    print(str(num3))
    file.close()
    file = open('number.txt', 'r')
    lines = file.readlines()
    sum = 0
    for line in lines:
        sum+=int(line)
    file.close
    print(sum)

main()


def main():
    finished = False
    finish = False
    while finished != True:
        value =int(input("enter a value to be cubed."))
        cube = value ** 3
        print(value, "cubed is", cube)
        while finish != True:
            choice = int(input("Cube another number? enter 0 to exit; enter 1 to continue."))
            if(choice==0):
                print("bye")
                finished = True
            elif("choice==1"):
                main()
            else:
                print("pls enter 1 or 0")
                finished != Fale
main()
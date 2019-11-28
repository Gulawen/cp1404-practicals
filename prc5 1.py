def main():
    finished = False

    while finished != True:
        value = int(input("Enter a value to be cubed."))
        cube = value ** 3
        print(str(value) + "cubed is" + str(cube))
        choice = input("Cube another number?")
        if choice== "No":
            finished = True
        else:
            finished = False

main()
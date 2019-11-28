from random import randint
def main():
    wp = randint(0,255)
    print("the level of the wind",int(wp))
    if wp < 0 or wp > 255:
        print("invalid")
        main()
    elif wp < 119:
        print("It is not yet a cyclone.")
    elif wp >= 119 and wp <= 153:
        print("it is level1.")
    elif wp >= 154 and wp <= 177:
        print("it is level2.")
    elif wp >= 178 and wp <= 208:
        print("it is level3.")
    else:
        print("it is level4.")
main()
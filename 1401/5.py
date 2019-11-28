def main():
    age = int(input("please enter yur age;"))
    enrolled = input("whether you are currently enrolled to vote:")
    if age > 18 and enrolled =="yes":
        print("You are old enough to vote, but are not enrolled")
    elif age >18 and enrolled =="no":
        print("Go Vote!")
    elif age <18 and enrolled =="yes":
        print("You are not yet 18 but you are enrolled")
    else:
        print("Go home kid")
main()

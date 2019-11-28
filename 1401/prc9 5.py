
def main():
    correct = 0
    wrong = 0
    capitals = {'South Australia': 'Adelaide', 'Queensland': 'Brisbane', 'Australian Capital Territory': 'Canberra','Northern Territory': 'Darwin', 'Tasmania': 'Hobart', 'Victoria': 'Melbourne', 'Western Australia': 'Perth', 'New South Wales': 'Sydney'}

    for x in capitals:
        answer = input("What is the capital city of the" + str(x)+":" )
        if answer == capitals[x]:
            correct = correct + 1
        else:
            wrong = wrong + 1
    print("You got" + str(correct) +"correct answers and" + str(wrong)+ "wrong answers.")
main()
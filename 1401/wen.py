
def main():
    sentence = str(input("pls enter the sentence"))
    if sentence != "":
        sentence = int(sentence)
        length = len(sentence)
        dividePhrase (length, sentence)
        number =  getAsterisks ()
        for i in  number:
            print("*")
        print("first_line\n")
        print("second_line\n")
        for i in number:
            print("*")

    else:
        print("invalid input")
        main()


def getAsterisks ():
    number = 20
    return number

def dividePhrase (length, sentence):
    half_length = length / 2
    first_line= sentence[0:half_length]
    second_line=sentence[half_length:length]
    return first_line,  second_line

main()

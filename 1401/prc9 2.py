def main():
    score = []
    for i in range(5):
        b = i + 1
        p = int(input("please enter the number %d :" %b))

        print(determine_grade(p))
        score.append(p)
    print("The average score is %.2f"%(calc_average(score)))

def calc_average(score):
    sum = 0
    for c in score:
        sum = sum + c
    return sum / len(score)

def determine_grade(p):
    if p < 50:
        return "F"
    if p>= 85:
        return"HD"
    if p>=75 and p<84:
        return "D"
    if p>=65 and p<74:
        return "C"
    if p>=50 and p<64:
        return "p"
main()



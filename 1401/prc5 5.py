def main():
    student = int(input("The number of students"))
    score = int(input("The test score of student"))
    for i in range(student):
        print("Student number " + str(i+1) + "\n------------------\n")
        sum = 0
        for u in range(score):
            sum += int(input("Enter test number " + str(u+1) + ""))
        average = sum / score


        print("The average for student number " + str(i+1) + " is " + str(average))
main()
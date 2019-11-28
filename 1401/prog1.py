def main():
     day1 = int(input("please enter Day1 sleep:"))#this is to gain the day1 data
     day2 = int(input("please enter Day2 sleep:"))#gain day2 data
     day3 = int(input("please enter Day3 sleep:"))#gain day 3data
     day4 = int(input("please enter Day4 sleep:"))#gain day4 data
     day5 = int(input("please enter Day5 sleep:"))#gain day5 data
     total = day1 + day2 + day3 + day4 + day5#the formula to get thee result of total
     debt = 40 - total# the formula of debt
     if debt <= 0:#to  make the choice
         print("Your total hours of sleep were:",int(total))
         print("You really sleep for enough time")
     else:
         print("Your total hours of sleep were:", int(total))
         print("Your sleep debt over this time is:",int(debt))
         print("You need more sleep!")
main()
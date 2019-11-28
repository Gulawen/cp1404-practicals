def main():
 for i in range(50):
     total = 1 + i
     if total % 3 ==0 and total % 5 == 0:
         print("FizzBuzz")
     elif total % 5 == 0:
         print("Buzz")
     elif total % 3 == 0:
         print("Fizz")
     else:
         print(str(total))
main()
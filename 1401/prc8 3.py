import random
def main():
    counter1 = 0
    counter2 = 0
    for i in range(100):
        x = random.randint(1,1000)
        t = x % 2
        if t == 0:
            counter1=counter1+1
        else:
            counter2=counter2+1
    print("there is "+ str(counter1)+"even" +"there is"+str(counter2)+"odd")
main()
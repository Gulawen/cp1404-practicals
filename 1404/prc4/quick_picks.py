
import random

MIN = 1
MAX = 45

def main():

	POOL = range(MIN,MAX+1)
	try:
		pick_n = int(input("How many quick picks? "))
		while(pick_n<1):
			pick_n = int(input("Input must be greater than 0 try again: "))
	except:
		print("Wrong input enter again: ")
		main()


	for i in range(pick_n):
		line = []
		for j in range(6):
			n = random.randint(0,44)
			while(POOL[n] in line):
				n = random.randint(1,45)
			line.append(POOL[n])
		line.sort()
		print(line)

main()
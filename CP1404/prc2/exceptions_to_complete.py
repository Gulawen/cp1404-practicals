finished = False
result = 0
while not finished:
    try:
        integer= input("pls enter integer")
        result = int(integer)
        finished = True
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)
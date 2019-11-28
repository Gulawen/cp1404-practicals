user_choice = input('Please enter the file name that you want to open: ')

f = open(user_choice, 'r')
print(f.read())

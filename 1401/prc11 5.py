file_name = input('Please enter the file name you want to use : ')


def file_one():

    user_name = input("Please enter your name : ")

    user_age = input("Please enter your age : ")

    user_address = input("Please enter your address : ")

    f = open(file_name, 'a')

    f.write('Name:{}\nAge:{}\nAddress:{}\n\n'.format(
        user_name, user_age, user_address))

    f.close()


file_one()

choice = input(
    'Do you want to enter another person\'s data?(Y for yes and anything else is no. : ').lower()

while choice == 'y':
    file_one()
    choice = input(
        'Do you want to enter another person\'s data?(Y for yes and anything else is no. : ').lower()
print('Good ByeD\n')

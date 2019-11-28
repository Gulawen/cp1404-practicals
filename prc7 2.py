import random


def main():
    wind_speed = random.randint(0, 255)
    print(cals_category(wind_speed))
def cals_category(wind_speed):
    if wind_speed in range(0, 118):
        message = str(wind_speed) + "\n It is not yet a cyclone"
    elif wind_speed in range(119, 153):
        message = str(wind_speed) + "\n It is a Category 1 cyclone"
    elif wind_speed in range(154, 177):
        message = str(wind_speed) + "\n It is a Category 2 cyclone"
    elif wind_speed in range(178, 208):
        message = str(wind_speed) + "\n It is a Category 3 cyclone"
    elif wind_speed in range(209, 251):
        message = str(wind_speed) + "\n It is a Category 4 cyclone"
    else:
        message = str(wind_speed) + "\n It is a Category 5 cyclone"

    print(message)


main()

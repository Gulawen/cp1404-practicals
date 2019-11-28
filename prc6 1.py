def main():
    height = float(input("Enter your height in meters"))
    weight = float(input("Enter your weight in meters"))
    BMI = height / weight * weight
    print("the BMI is ",str(BMI))
main()
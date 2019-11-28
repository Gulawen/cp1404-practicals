def main():
    years = int(input("please enter the year:"))
    totalr = 0
    for i in range(years):
        for month in range(12):
            rain = int(input("please enter the rainfall of month" +  str(month+1)))
            totalr = rain + totalr

    totalm = years * 12
    ar = totalr/totalm
    print("the total rain is",str(totalr), "the average rain is", str(ar))
main()
def main():
    fn = input("enter the first people name:")
    d1 = int(input("pls enter the first birth year"))
    sn = input("enter the second people name:")
    d2 = int(input("pls enter the second birth year"))
    d3 = d1 + 70
    d4 = d2 + 70
    print("fn",  "will become eligible in", str(d3), "and", "sn", "will become eligible in", str(d4))
main()
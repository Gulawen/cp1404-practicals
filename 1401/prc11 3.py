wjh = open("data.txt", "w")
for x in range(1, 51):
    str_x = str(x)

    wjh.write(str_x+  "\n")

wjh.close()

wjh = open("data.txt", "r")
print(wjh.read())

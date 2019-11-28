Driver = 100
Iron = 30
Patter = 10
club = input("please enter the choice of the club")
if choice == "Driver":
    distance = distance - Driver * x
    if distance > 0:
        print(club())
        counter = counter + 1
    elif distance < 0:
        distance = 0 - distance
    else:
        db = par - counter
        if db < 0:
            db = 0 - db
            print("Clunk...After" + str(counter) + "hits, the ball is in the hole! Disappointing.You are" + str(db) + "over the par")

            elif db = 0:
            print("Clunk...After" + str(counter) + "hits, the ball is in the hole! And that’s par")

            else:
            print("Clunk...After" + str(counter) + "hits, the ball is in the hole! Disappointing.You are" + str(
                db) + "under the par")
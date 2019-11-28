import random
#make the list to save the score and pars
scores = []
pars = []
#main function the body of the programm get the name, par and distance from player
def main():
    name = input("Please enter your name:")
    print("Welcome to the game,",str(name))
    print("Let's play golf, CP1401 style!")
    counter = 0
    fk = 0
    total_score = 0
#to get the par and distance
    par = int(input("Choose a par for this course (between 3-5 inclusive):"))
    while par < 3 or par > 5:
        print("I’m sorry, you must choose a number between 3-5 inclusive. Please enter again.")
        par = int(input("Choose a par for this course (between 3-5 inclusive):"))
    distance = get_distance()
    run(par, distance, counter, name, fk, total_score)

#get the distance
def get_distance():
    distance = int(input("How many meters to the hole (between 195 – 250 inclusive)："))
    while distance > 250 or distance < 195:
        print("please enter the right distance")
        distance = int(input("How many meters to the hole (between 195 – 250 inclusive)："))
    return distance

#display menu
def menu():
    menu_op = input("1 - Display (I)nstructions\n2 - Display (P)lay golf\n3 - Display (Q)uit\n")
    return menu_op

#the main function of the menu for player to choose
def run(par, distance, counter, name, fk, total_score):
    print("Let's play golf, CP1401 style!")
    print("Golf!")
    menu_op = menu()
    if menu_op == "I" or menu_op =="i":
        display_instruction(par, distance)
    elif menu_op == "P" or menu_op=="p":
        fk+=1
        if fk ==1:
            first(distance, counter, par, total_score)
        else:
            play(distance, counter, par, total_score)
    elif menu_op == "Q" or menu_op =="q":
        quit(name)
        return 0
    else:
        print("Invalid menu choice.")
        run(par, distance, counter, name, fk, total_score)
    run(par,distance,counter, name, fk, total_score)


#show introduction
def display_instruction(par, distance):
    print("This is a simple golf game in which each hole is" + str(distance) + "game away with par" + str(par) + ".\n" + "You are able to choose from 3 clubs, the Driver, Iron or Putter.\n"" The Driver will hit around 100m, the Iron around 30m and the Putter around 10m.\n"" The putter is best used very close to the hole.\n")

#play function when player choose play it will appear
def play(distance, counter, par,  total_score):
    print("The distance is" + str(distance))
    club = cl()
    Driver = random.randint(80, 120)
    Iron = random.randint(24, 36)
    Putter = random.randint(8, 12)
    counter = counter + 1
    if club =="Driver" or club =="D" or club== "d":
        dis = Driver
    elif club =="Iron" or club=="I" or club=="i":
        dis = Iron
    elif club== "Putter" or club=="P" or club=="p":
        if distance <= 10:
            x = random.randint(80,120)
            dis = distance * x//100
            if dis == 0:
                dis == 1
        else:
            dis = Putter
    else:
        print("Invalid choice")
        play(distance, counter, par,  total_score)
    print("You shot went" +str(dis))
    distance = abs(distance - dis)
    if distance == 0:
        db = par - counter
        scores.append(counter)
        pars.append(db)
        total_score += counter
        if db < 0:
            db = 0 - db
            print("Clunk...After" + str(counter) + "hits, the ball is in the hole! Disappointing.You are" + str(db) + "over the par")
            total_score = overall(counter, total_score, par)
        elif db == 0:
            print("Clunk...After" + str(counter) + "hits, the ball is in the hole! And that’s par")
            total_score = overall(counter, total_score, par)
        else:
            print("Clunk...After" + str(counter) + "hits, the ball is in the hole! Disappointing.You are" + str(db) + "under the par")
            total_score = overall(counter, total_score, par)
        return total_score

    else:
        play(distance, counter, par,  total_score)


# choose clubs function
def cl():
    print("There is three clubs:\n")
    print("Driver: 100m (actual between 80 and 120)\n")
    print("Iron: 30m (actual between 24 and 36)\n")
    print("Putter: 10m(actual between 8 and 12)\n")
    club = input("please enter the choice of the club :")
    return club


#the function that show the function
def display_instruction(par, distance):
    print("This is a simple golf game in which each hole is" + str(distance) + "game away with par" + str(par) + ".\n" + "You are able to choose from 3 clubs, the Driver, Iron or Putter.\n"" The Driver will hit around 100m, the Iron around 30m and the Putter around 10m.\n"" The putter is best used very close to the hole.\n")

#the dunction that run for the first round
def first(distance, counter, par,  total_score):
    print("The distance is" + str(distance))
    club = cl()
    Driver = random.randint(80, 120)
    Iron = random.randint(24, 36)
    Putter = random.randint(8, 12)
    counter = counter + 1
    if club =="Driver" or club =="D" or club== "d":
        dis = Driver
    elif club =="Iron" or club=="I" or club=="i":
        dis = Iron
    elif club== "Putter" or club=="P" or club=="p":
        if distance <= 10:
            x = random.randint(80,120)
            dis = distance * x//100
            if dis==0:
                dis==1
        else:
            dis = Putter
    else:
        print("Invalid choice")
        first(distance, counter, par,  total_score)
    print("You shot went" +str(dis))
    distance = abs(distance - dis)
    if distance == 0:
        db = par - counter
        scores.append(counter)
        pars.append(db)
        total_score += counter
        if db < 0:
            db = 0 - db
            print("Clunk...After" + str(counter) + "hits, the ball is in the hole! Disappointing.You are" + str(db) + "over the par")
            overall(counter, total_score, par)
        elif db == 0:
            print("Clunk...After" + str(counter) + "hits, the ball is in the hole! And that’s par")
            overall(counter, total_score, par)
        else:
            print("Clunk...After" + str(counter) + "hits, the ball is in the hole! Disappointing.You are" + str(db) + "under the par")
            overall(counter, total_score, par)
        return total_score

    else:
        first(distance, counter, par,  total_score)


#the function that show the result of each round
def overall(counter, total_score, par):
    total_par = len(scores)* par
    margin = total_score - total_par
    if margin>0:
        print("Your overall score is"+ str(total_score)+ "And you are" + str(margin) + "over the par\n" +"after"+ str( len(scores))+ "holes")
    elif margin<0:
        margin = 0 - margin
        print("Your overall score is" + str(total_score) + "And you are" + str(margin) + "under the par\n" "after"+ str( len(scores))+ "holes")
    else:
        print("Your overall score is" + str(total_score) + "And that’s par\n" "after"+ str( len(scores))+ "holes")

#quit function
def quit(name):
    print("Farewell and thanks for playing"+ str(name))
    for i in range(len(scores)):
        print("Round %d : " %(i+1))
        print(str(scores[i])+"shots")

main()
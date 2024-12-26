#                 S W G
# computer =      0 1 2
# player =  S  0  D W L
#           W  1  L D W
#           G  2  W L D
import random

lis= [["D","W","L"],["L","D","W"],["W","L","D"]]
dic ={"s":0,"w":1,"g":2}
l = [0,1,2]

print(" Lets Start Playing the Sanke Water And Gun Game ")
plarerName = input("Enter your Name: ")
score = 0
f = open('/workspaces/Python/Intermediate/excerse4_score.txt',"r")

higestScore = int(f.read())
f.close()

print(f"      Current Higest Score is {higestScore}")
while True:

    val = input("Enter your option Choose from Sanke as s , water as w and Gun as g ")
    print(f"Current Score is {score}")
    if val not in ["s","w","g","q"]:
        print("Wrong Input Please choose either s g or w")
        continue
    if val=="q":
        print(f"Terminating the Game Thanks For Playing {plarerName} your higest score is: {score}")
        break
    random_num = random.choice(l)
    print(f"Optins Enterd by computer is {random_num}")
    if(score>higestScore):
        higestScore=score
    if lis[dic[val]][random_num] == "D":
        print("Match Draw")
    elif lis[dic[val]][random_num] == "W":
        score= score+1000
        print(f"You Won Congratulatons: {plarerName}")
    elif lis[dic[val]][random_num] == "L":
        score = score -5000
        print("You loose")
    else:
        continue


f = open('/workspaces/Python/Intermediate/excerse4_score.txt',"w")

f.write(str(higestScore))
f.close()
import random
print("hello ...! Welcome to the mansi's game")
human_score_card=0
computer_score_card=0
chances=5

for i in range(0,5):
    print("CHOICES:- \n1.Stone \n2.Paper \n3.Scissors")
    result=" "
    human=int(input("choose your option:- "))
    lst=["Stone","Paper","Scissors"]
    computer=random.choice(lst)

    #GAME
    while True:
        if human==1 or human==2 or human==3:
            chances-=1
            #STONE:- 
            if human==1 and computer==lst[0]:
                human="stone"
                result="DRAW"
            if human==1 and computer==lst[1]:
                human="stone"
                result="COMPUTER WINS"
                computer_score_card+=1
            if human==1 and computer==lst[2]:
                human="stone"
                result="HUMAN WINS"
                human_score_card+=1

            #PAPER 
            if human==2 and computer==lst[0]:
                human="Paper"
                result="HUMAN WINS"
                human_score_card+=1
            if human==2 and computer==lst[1]:
                human="Paper"
                result="DRAW"
            if human==2 and computer==lst[2]:
                human="Paper"
                result="COMPUTER WINS"
                computer_score_card+=1

            #SCISSORS 
            if human==3 and computer==lst[0]:
                human="Scissors"
                result="COMPUTER WINS"
                computer_score_card+=1
            if human==3 and computer==lst[1]:
                human="Scissors"
                result="DRAW"
            if human==3 and computer==lst[2]:
                human="Scissors"
                result="HUMAN WINS"
                human_score_card+=1
        
        print(human,"vs",computer)
        print(result)
        print("human score= ",human_score_card, "computer score= ",computer_score_card)
        print("chances left: ",chances)

        break
    else:
        print(" Invalid Option \n Please try again")
            
if human_score_card > computer_score_card:
    print("human beats computer by: ",human_score_card-computer_score_card)
elif human_score_card==computer_score_card:
    print("Match is tie")
else:
    print("computer beats human by: ",computer_score_card-human_score_card)
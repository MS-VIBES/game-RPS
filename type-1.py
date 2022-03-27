import random
game=["stone","paper","scissors"]
computer=random.choice(game)
user=input("enter your choice:- ")

if user==computer:
    print(" MATCH IS DRAW")
#STONE CASE
elif user=="stone" and computer=="paper":
    print("YOU LOOSE")
    print("I choose paper")
elif user=="stone" and computer=="scissors":
    print("YOU WIN")
    print("I choose scissors")
#PAPER  CASE
elif user=="paper" and computer=="stone":
    print("YOU WIN")
    print("I choose stone")
elif user=="paper" and computer=="scissors":
    print("YOU LOOSE")
    print("I choose scissors")

#SCISSOR CASE
elif user=="scissors" and computer=="paper":
    print("YOU WIN")
    print("I choose paper")
elif user=="scissors" and computer=="stone":
    print("YOU LOOSE")
    print("I choose stone")

else:
    print("value Error")
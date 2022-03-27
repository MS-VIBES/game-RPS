#IMPORTING ALL THE REQUIRED LIBRARY
from tkinter import *
from random import randint
from PIL import Image,ImageTk

#INITIATING THE WINDOW
window=Tk()
window.title("GAME: Rock,Paper & Scissors")
window.configure(background="black")


#ADDING IMAGES FOR THE LEFT AS WELL AS RIGHT SIDE
#       computer images(left side)
image_rock1=ImageTk.PhotoImage(Image.open("D:\\PROJECTS\\MINOR PROJECTS\\4. PYTHON\\rock paper and scissors\\images\\rock(1).png"))
image_paper1=ImageTk.PhotoImage(Image.open("D:\\PROJECTS\\MINOR PROJECTS\\4. PYTHON\\rock paper and scissors\\images\\paper(1).png"))
image_scissors1=ImageTk.PhotoImage(Image.open("D:\\PROJECTS\\MINOR PROJECTS\\4. PYTHON\\rock paper and scissors\\images\\scissors(2).png"))

#           User images(Right Side)
image_rock2=ImageTk.PhotoImage(Image.open("D:\\PROJECTS\\MINOR PROJECTS\\4. PYTHON\\rock paper and scissors\\images\\rock(2).png"))
image_paper2=ImageTk.PhotoImage(Image.open("D:\\PROJECTS\\MINOR PROJECTS\\4. PYTHON\\rock paper and scissors\\images\\paper(2).png"))
image_scissors2=ImageTk.PhotoImage(Image.open("D:\\PROJECTS\\MINOR PROJECTS\\4. PYTHON\\rock paper and scissors\\images\\scissors(2).png"))

#MAKING LABEL FOR USER AND COMPUTER.
Label_player=Label(window,image=image_rock1)
Label_computer=Label(window,image=image_rock1)

Label_computer.grid(row=1,column=0)
Label_player.grid(row=1,column=4)

#MAKING THE SCORE BOARD FOR USER AND COMPUTER
computer_score_board=Label(window,text=0,font=("arial",60,"bold"),fg="red")
player_score_board=Label(window,text=0,font=("arial",60,"bold"),fg="red")

player_score_board.grid(row=1,column=1)     #RHS
computer_score_board.grid(row=1,column=3)   #LHS

#ADDING THE INDICATORS.
player_indicator=Label(window,font=("arial",40,"bold"),text="PLAYER",bg="orange",fg="blue")
computer_indicator=Label(window,font=("arial",40,"bold"),text="COMPUTER",bg="orange",fg="blue")
computer_indicator.grid(row=0,column=1)
player_indicator.grid(row=0,column=3)


#  MAKING THE FUNCTIONS

#               function for a message.

def msg_updation(a):
        final_message["text"]=a

#       function for computer and player update.

def computer_update():
        final=int(computer_score_board['text'])
        final+=1
        computer_score_board['text']=str(final)

def player_update():
        final=int(player_score_board['text'])
        final+=1
        player_score_board['text']=str(final)

def winner_check(p,c):
        if p==c:
                msg_updation("It's a tie!...")
        elif p=="rock":
                if c=="paper":
                        msg_updation("computer wins!....")
                        computer_update()
                else:
                        msg_updation("Player Wins!...")
                        player_update()
        elif p=="paper":
                if c=="scissors":
                        msg_updation("Computer Wins!...")
                        computer_update()
                else:
                        msg_updation("Player Wins!..")
                        player_update()
        elif p=="scissors":
                if c=="rock":
                        msg_updation("computer Wins!...")
                        computer_update()
                else:
                        msg_updation("Player Wins!...")
                        player_update()
        else:
                pass
        
        #the below function will describe the relation between computer/player's selections and display of its images.

to_select=["rock","paper","scissors"]
def choice_update(a):
        choice_computer=to_select[randint(0,2)]
        if choice_computer=="rock":
                Label_computer.configure(image=image_rock1)
        elif choice_computer=="paper":
                Label_computer.configure(image=image_paper1)
        else:
                Label_computer.configure(image=image_scissors1)

        if a=="rock":
                Label_player.configure(image=image_rock2)
        elif a=="paper":
                Label_player.configure(image=image_paper2)
        else:
                Label_player.configure(image=image_scissors2)

        winner_check(a,choice_computer)

#DISPLAYING THE MESSAGE
final_message=Label(window,font=("arial",40,"bold"),bg="red",fg="white")
final_message.grid(row=3,column=2)

#ADDING THE BUTTONS
button_rock=Button(window,width=16,height=3,text="ROCK",font=("arial",20,"bold"),bg="yellow",fg="red",command=lambda:choice_update("rock")).grid(row=2,column=1)
button_paper=Button(window,width=16,height=3,text="PAPER",font=("arial",20,"bold"),bg="yellow",fg="red",command=lambda:choice_update("paper")).grid(row=2,column=2)
button_scissor=Button(window,width=16,height=3,text="SCISSORS",font=("arial",20,"bold"),bg="yellow",fg="red",command=lambda:choice_update("scissors")).grid(row=2,column=3)



#EXECUTE  THE WINDOW
window.mainloop()
from tkinter import *
from random import randint
from tkinter import ttk

window=Tk()
window.title("MS-Rock,Paper & Scissors")
window.iconbitmap("D:\\PROJECTS\\MINOR PROJECTS\\4. PYTHON\\rock paper and scissors\\icon.ico")
window.geometry("1000x1000")

#BODY

#1. adding background color 
window.config(bg="dark Red")

#2. Defining our pictures
rock=PhotoImage(file="D:\\PROJECTS\\MINOR PROJECTS\\4. PYTHON\\rock paper and scissors\\rock.png")
paper=PhotoImage(file="D:\\PROJECTS\\MINOR PROJECTS\\4. PYTHON\\rock paper and scissors\\paper.png")
scissors=PhotoImage(file="D:\\PROJECTS\\MINOR PROJECTS\\4. PYTHON\\rock paper and scissors\\scissors.png")

#3. Adding images to the list.
img_list=[rock,paper,scissors]

#4. picking random image i.e between 0-2
pick_img_no=randint(0,2)

#5. image throw up when a program starts
img_label=Label(window,image=img_list[pick_img_no],bd=0)
img_label.pack(pady=20)

#       defining the function for button-1
def spin():
        #pick a random number
        pick_img_no=randint(0,2)
        #show us the random picked image
        img_label.config(image=img_list[pick_img_no])

        #0=Rock
        #1=Paper
        #2=Scissors

# 10.  ADDING LOGIC TO THE DROPDOWN MENU

        #below given we have added the options in strings for the dropdown menu, you need to convert them into numbers creating a button
        if user_btn2.get()=="Rock":
                user_choice_value=0
        elif user_btn2.get()=="Paper":
                user_choice_value=1
        elif user_btn2.get()=="Scissors":
                user_choice_value=2

#11.  MAIN LOGIC.  

        #Determine the loss or win
        #if you pick Rock
        if user_choice_value==0: #Rock
                if pick_img_no==0:#Rock
                        Results_label.config(text="It's a Tie!..Spin Again...!")
                elif pick_img_no==1:#paper
                        Results_label.config(text="Paper covers rock!..You loose..!")
                elif pick_img_no==2:#Scissors
                        Results_label.config(text="Rock Smashes Scissors!...You won!..")
        #if you pick Paper
        if user_choice_value==1: #Paper
                if pick_img_no==1:
                        Results_label.config(text="It's a Tie!..Spin Again...!")
                elif pick_img_no==0:#Rock
                        Results_label.config(text="Paper covers rock!..You Win..!")
                elif pick_img_no==2:#Scissors
                        Results_label.config(text="Scissors cuts paper...You loose!..")
        #if you pick scissors
        if user_choice_value==2: #Scissors
                if pick_img_no==2:
                        Results_label.config(text="It's a Tie!..Spin Again...!")
                elif pick_img_no==0:#rock
                        Results_label.config(text="Rock smashes scissors!..You loose!")
                elif pick_img_no==1:#Paper
                        Results_label.config(text="Scissors cuts paper.You Win...!")

#7. USER CHOICE BOX
user_btn2=ttk.Combobox(window,value=("Rock","Paper","Scissors"))
user_btn2.current(0)
user_btn2.pack(pady=20)


#8. create Spin button
btn1=Button(window,text="spin!",command=spin)
btn1.pack(pady=10)

#9. Adding label to show the results
Results_label=Label(window,text="",font=("helvetica",18),bg="Dark Red")
Results_label.pack(pady=50)

#SHOWS THE WINDOW
window.mainloop()
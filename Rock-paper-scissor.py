import tkinter 
#import PIL
#from PIL import ImageTk, Image
from tkinter import *
import random as rd
main=Tk()
main.geometry("400x400")
main.title("Rock Paper Scissor Game")
comp_value={
    "0":"Rock",
    "1":"Paper",
    "2":"Scissor"
}

def reset_game():
    b1["state"]="active"
    b2["state"]="active"
    b3["state"]="active"
    l1.config(text="Player")
    l3.config(text="Computer")
    l4.config(text="")

def  button_disable():
    b1["state"] = "disable"
    b2["state"] = "disable"
    b3["state"] = "disable"

def isrock():
    c_v=comp_value[str(rd.randint(0,2))]
    if c_v=="Rock":
        match_result="Match Draw"
    elif c_v=="Paper":
        match_result="You win"
    else:
        match_result="Computer win"
    l4.config(text=match_result)
    l1.config(text="Rock")
    l3.config(text=c_v)
    button_disable()
def ispaper():
    c_v=comp_value[str(rd.randint(0,2))]
    if c_v=="Paper":
        match_result="Match Draw"
    elif c_v=="Scissor":
        match_result="You win"
    else:
        match_result="Computer win"
    l4.config(text=match_result)
    l1.config(text="Paper")
    l3.config(text=c_v)
    button_disable()
def isscissor():
    c_v=comp_value[str(rd.randint(0,2))]
    if c_v=="Scissor":
        match_result="Match Draw"
    elif c_v=="Rock":
        match_result="You win"
    else:
        match_result="Computer win"
    l4.config(text=match_result)
    l1.config(text="Scissor")
    l3.config(text=c_v)
    button_disable()
#img = ImageTk.PhotoImage(Image.open("https://static.vecteezy.com/system/resources/thumbnails/000/691/497/small/rock-paper-scissors-neon-icons.jpg"))
#label = Label(frame, image = img)
Label(main,
      text="Rock Paper Scissor",
      font="Bold 20",
      fg="white",
      #img = ImageTk.PhotoImage(Image.open("https://static.vecteezy.com/system/resources/thumbnails/000/691/497/small/rock-paper-scissors-neon-icons.jpg"))
      ).pack(pady=20)
frame=Frame(main)
frame.pack()

l1=Label(frame,
         text="Player",
         font=10)
l2=Label(frame,
         text="VS",
         font=10)
l3=Label(frame,
         text="Computer",
         font=10)
l1.pack(side=LEFT)
l2.pack(side=LEFT)
l3.pack()
l4 = Label(main,
           text="",
           font="normal 20 bold",
           bg="white",
           width=15,
           borderwidth=2,
           relief="solid")
l4.pack(pady=20)
f1=Frame(main)
f1.pack()
b1 = Button(f1, text="Rock",
            font=10, width=7,
            command=isrock)
 
b2 = Button(f1, text="Paper ",
            font=10, width=7,
            command=ispaper)
 
b3 = Button(f1, text="Scissor",
            font=10, width=7,
            command=isscissor)
b1.pack(side=LEFT, padx=10)
b2.pack(side=LEFT, padx=10)
b3.pack(padx=10)
 
Button(main, text="Reset Game",
       font=10, fg="red",
       bg="black", command=reset_game).pack(pady=20)
 
# Execute Tkinter
main.mainloop()

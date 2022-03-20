# Tic Tac Toe game using tkinter

# importing the modules required

from cgitb import text
import imp
from itertools import count
from tkinter import *
import tkinter.messagebox

#the window
root=Tk()

root.iconbitmap('tic-tac-toe.ico')

root.title('Tic-tac-toe')

root.resizable(False,False)

click= True

#counting variable to check the number of turns

count = 0

btn1=StringVar()
btn2=StringVar()
btn3=StringVar()
btn4=StringVar()
btn5=StringVar()
btn6=StringVar()
btn7=StringVar()
btn8=StringVar()
btn9=StringVar()

xPhoto = PhotoImage(file='cross.png')
oPhoto= PhotoImage(file= 'happy.png')

#Grid Buttons

def start():
    button1 = Button(root, height=9, width=19, bd=.5, relief ="sunken" , bg='#ccfff7', textvariable=btn1,
    command=lambda: press(1,0,0))
    button1.grid(row=0, column=0)
    button2 = Button(root, height=9, width=19, bd=.5, relief='sunken', bg='#ccfff7', textvariable=btn2,
    command=lambda: press(2,0,1))
    button2.grid(row=0, column=1)
    button3 = Button(root, height=9, width=19, bd=.5, relief='sunken', bg='#ccfff7', textvariable=btn3,
    command=lambda: press(3,0,2))
    button3.grid(row=0, column=2)
    button4 = Button(root, height=9, width=19, bd=.5, relief='sunken', bg='#99ffee', textvariable=btn4,
    command=lambda: press(4,1,0))
    button4.grid(row=1, column=0)
    button5 = Button(root, height=9, width=19, bd=.5, relief='sunken', bg='#99ffee', textvariable=btn5,
    command=lambda: press(5,1,1))
    button5.grid(row=1, column=1)
    button6 = Button(root, height=9, width=19, bd=.5, relief='sunken', bg='#99ffee', textvariable=btn6,
    command=lambda: press(6,1,2))
    button6.grid(row=1, column=2)
    button7 = Button(root, height=9, width=19, bd=.5, relief='sunken', bg='#66ffe6', textvariable=btn7,
    command=lambda: press(7,2,0))
    button7.grid(row=2, column=0)
    button8 = Button(root, height=9, width=19, bd=.5, relief='sunken', bg='#66ffe6', textvariable=btn8,
    command=lambda: press(8,2,1))
    button8.grid(row=2, column=1)
    button9 = Button(root, height=9, width=19, bd=.5, relief='sunken', bg='#66ffe6', textvariable=btn9,
    command=lambda: press(9,2,2))
    button9.grid(row=2, column=2)

    # changing the value of button
def press(num, r,c):
    global click, count
    if click == True:
        labelPhoto = Label(root, image = xPhoto)
        labelPhoto.grid(row=r, column=c)

        if num == 1:
            btn1.set('X')
        elif num == 2:
            btn2.set('X')
        elif num == 3:
            btn3.set('X')
        elif num == 4:
            btn4.set('X')
        elif num == 5:
            btn5.set('X')
        elif num == 6:
            btn6.set('X')
        elif num == 7:
            btn7.set('X')
        elif num == 8:
            btn8.set('X')
        else:
            btn9.set('X')
        count += 1
        click = False
        checkWin()

    # check the win


import random
from tkinter import font
from tkinter.font import BOLD
from PIL import Image,ImageTk
import tkinter

root=tkinter.Tk()
root.geometry('400x400')
root.title('Dice Simulator')

dice=['d1.png', 'd2.png', 'd3.png', 'd4.png', 'd5.png', 'd6.png']
DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))

ImageLabel = tkinter.Label(root, image=DiceImage)
ImageLabel.image = DiceImage
ImageLabel.pack(expand=True)

def rolling_dice():
    DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    ImageLabel.config(image=DiceImage)
    ImageLabel.image=DiceImage

button=tkinter.Button(root,text='Roll the dice',command=rolling_dice,bg="white",fg="black",font=BOLD)
button.pack(expand=True)

root.mainloop()
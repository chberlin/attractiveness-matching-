import tkinter as tk
from PIL import Image, ImageTk
from itertools import count
import tkinter
import tkinter.ttk as ttk
from PIL import Image, ImageTk
from Model import *


class Controller:
    def __init__(self):
        self.window = tkinter.Tk()
        self.model = Model()
        self.command = ""


    def mainloop(self):

        image = self.model.getImage()
        img = ImageTk.PhotoImage(Image.open(image))
        panel = tk.Label(self.window, image=img)
        panel.pack(side="bottom", fill="both", expand="yes")
        tkinter.ttk.Button(self.window, text="Quit", command=self.window.destroy).pack()

        name = tk.Label(self.window, text="This is " + self.model.randoName)
        name.pack()

        maleScore = tk.Label(self.window, text= "Male Beauty Score is ")
        maleScore.pack()

        femaleScore = tk.Label(self.window, text="Female Beauty Score is ")
        femaleScore.pack()

        self.model.getBeautyScore(image)

        maleScore['text'] = "Male Beauty Score is: " + self.model.maleBeautyRanking + "%"
        femaleScore['text'] = "Female Beuaty Score is " + self.model.femaleBeautyRanking + "%"

        distance = tk.Label(self.window, text= "Your distance from name is ")
        distance.pack()

        self.model.getDistance()
        distance['text'] = "Your distance from " + str(self.model.randoName) + " is " + str(int(self.model.getDistance())) + " miles"

        self.window.mainloop()

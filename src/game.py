import customtkinter as ctk                                             #Modern and customizable library for user interface based on TKinter. https://customtkinter.tomschimansky.com/
from customtkinter import *
import CTkMessagebox as msgbox                                          #CustomTKinter based pop-up extension. https://github.com/Akascape/CTkMessagebox
from tkinter import ttk
import PIL                                                              #library for image rendering
from PIL import Image
from pydub import AudioSegment
import random
from pydub.playback import play

class Game(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(width=1920, height=1080)

        #area in which numbers generally spawn
        self.frame = ctk.CTkFrame(self, width=1500, height=700, fg_color="#7F7F7F")
        self.frame.place(relx=0.5, rely=0.6, anchor="center")

        #each of the four buttons
        self.button1 = ctk.CTkButton(self.frame, text=self.genRandomNumber(), height=150, width=150, command=self.countdown1,
                                        fg_color="#FFD300", hover_color="#FEBE00", font=("Arial", 50))
        self.button1.place(relx=self.getRandomCoordinate(), rely=self.getRandomCoordinate(), anchor="center")

        self.button2 = ctk.CTkButton(self.frame, text=self.genRandomNumber(), height=150, width=150, command=self.countdown2,
                                        fg_color="#FFD300", hover_color="#FEBE00", font=("Arial", 50))
        self.button2.place(relx=self.getRandomCoordinate(), rely=self.getRandomCoordinate(), anchor="center")
        
        self.button3 = ctk.CTkButton(self.frame, text=self.genRandomNumber(), height=150, width=150, command=self.countdown3,
                                        fg_color="#FFD300", hover_color="#FEBE00", font=("Arial", 50))
        self.button3.place(relx=self.getRandomCoordinate(), rely=self.getRandomCoordinate(), anchor="center")

        self.button4 = ctk.CTkButton(self.frame, text=self.genRandomNumber(), height=150, width=150, command=self.countdown4,
                                        fg_color="#FFD300", hover_color="#FEBE00", font=("Arial", 50))
        self.button4.place(relx=self.getRandomCoordinate(), rely=self.getRandomCoordinate(), anchor="center")
    
    #generate a random number for each button
    def genRandomNumber(self):
        return random.randint(3,10)

    #random relative coordinate for each button
    def getRandomCoordinate(self):
        return random.random()

    #countdown for each button
    def countdown1(self):
        txt = self.button1.cget("text")
        if txt != "X":
            num=int(txt)
            if num > 1:
                num = num-1
                self.button1.configure(text=num)
            elif num == 1:
                num = 0
                self.button1.configure(text=num, fg_color="#00FF00", hover_color="#009F00")
            elif num == 0:
                num = "X"
                self.button1.configure(text=num, fg_color="#FF0000", hover_color="#9F0000")
    
    def countdown2(self):
        txt = self.button2.cget("text")
        if txt != "X":
            num=int(txt)
            if num > 1:
                num = num-1
                self.button2.configure(text=num)
            elif num == 1:
                num = 0
                self.button2.configure(text=num, fg_color="#00FF00", hover_color="#009F00")
            elif num == 0:
                num = "X"
                self.button2.configure(text=num, fg_color="#FF0000", hover_color="#9F0000")
    
    def countdown3(self):
        txt = self.button3.cget("text")
        if txt != "X":
            num=int(txt)
            if num > 1:
                num = num-1
                self.button3.configure(text=num)
            elif num == 1:
                num = 0
                self.button3.configure(text=num, fg_color="#00FF00", hover_color="#009F00")
            elif num == 0:
                num = "X"
                self.button3.configure(text=num, fg_color="#FF0000", hover_color="#9F0000")
    
    def countdown4(self):
        txt = self.button4.cget("text")
        if txt != "X":
            num=int(txt)
            if num > 1:
                num = num-1
                self.button4.configure(text=num)
            elif num == 1:
                num = 0
                self.button4.configure(text=num, fg_color="#00FF00", hover_color="#009F00")
            elif num == 0:
                num = "X"
                self.button4.configure(text=num, fg_color="#FF0000", hover_color="#9F0000")
                            
import customtkinter as ctk                                             #Modern and customizable library for user interface based on TKinter. https://customtkinter.tomschimansky.com/
from customtkinter import *
from tkinter import ttk
from pydub import AudioSegment
import random
import time
from pydub.playback import play
import menuPage

class Game(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(width=1920, height=1080)

        #timer text
        self.time = ctk.CTkLabel(self, font=("Times New Roman Bold", 150), text="6")
        self.time.place(relx=0.5, rely=0.2, anchor="center")

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

        self.time.after(0, self.timeCountdown)

    #generate a random number for each button
    def genRandomNumber(self):
        return random.randint(3,10)

    #random relative coordinate for each button
    def getRandomCoordinate(self):
        return random.random()

    #timer countdown
    def timeCountdown(self):
        num = int(self.time.cget("text"))
        if num > 1:
            res= str(num-1)
            self.time.configure(text=res)
            self.time.after(1000, self.timeCountdown)
        #time's up
        elif num == 1:
            self.time.after(0, self.result())

    #get the result
    def result(self):
        #check all numbers
        num1 = str(self.button1.cget("text")) == "0"
        num2 = str(self.button2.cget("text")) == "0"
        num3 = str(self.button3.cget("text")) == "0"
        num4 = str(self.button4.cget("text")) == "0"
        #destroy most graphical inputs
        self.frame.destroy()
        self.button1.destroy()
        self.button2.destroy()
        self.button3.destroy()
        self.button4.destroy()
        #communicate result
        if num1 and num2 and num3 and num4:
            self.time.configure(text="You most likely won")
        else:
            self.time.configure(text="You most likely lost")
        #return to menu
        self.after(2500, self.goToMenu)

    #return to menu
    def goToMenu(self):
        self.master.switch_frame(menuPage.MenuPage) 

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
                            
import customtkinter as ctk                                             #Modern and customizable library for user interface based on TKinter. https://customtkinter.tomschimansky.com/
from customtkinter import *
import CTkMessagebox as msgbox                                          #CustomTKinter based pop-up extension. https://github.com/Akascape/CTkMessagebox
from tkinter import ttk
import PIL                                                              #library for image rendering
from PIL import Image

class MenuPage(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(width=1920, height=1080)

        #Title
        self.title = ctk.CTkLabel(self, text="PyClash", font=("Arial", 150))
        self.title.place(relx=0.5, rely=0.3, anchor="center")

        #Start the game
        self.startBtn = ctk.CTkButton(self, text="Clash!", height=150, width=250, command=self.start_callback,
                                        fg_color="#FA8128", hover_color="DD571C")
        self.startBtn.place(relx=0.5, rely=0.5, anchor="center")
        
        #Exit the game


    def start_callback(self):
        print("Game is going to start!")
        #self.master.switch_frame(gameFrame.GameFrame)
import customtkinter as ctk                                             #Modern and customizable library for user interface based on TKinter. https://customtkinter.tomschimansky.com/
from customtkinter import *
import CTkMessagebox as msgbox                                          #CustomTKinter based pop-up extension. https://github.com/Akascape/CTkMessagebox
from tkinter import ttk
import PIL                                                              #library for image rendering
from PIL import Image
import menuPage

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        #main info
        self.title("PyClash")
        self.geometry("1920x1080")
        self.wm_attributes("-fullscreen", True)
        self.resizable(0,0)
        self.grid_columnconfigure((0, 1), weight=1)
        #start to initial page
        self._frame = None
        self.switch_frame(menuPage.MenuPage)

    #used to switch the various pages
    def switch_frame(self, frame_class):
        new_frame = frame_class(master=self)
        #if there's another frame initialized, destroy it
        if self._frame is not None:
            self._frame.destroy()
        #initialize the new frame
        self._frame = new_frame
        self._frame.pack()

#main starts the app
app = App()
app.mainloop()
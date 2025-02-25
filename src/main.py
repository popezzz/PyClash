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
        #informazioni principali
        self.title("PyClash")
        self.geometry("1920x1080")
        self.wm_attributes("-fullscreen", True)
        self.resizable(0,0)
        self.grid_columnconfigure((0, 1), weight=1)
        #inzia alla pagina iniziale (mettendo None come frame corrente)
        self._frame = None
        #da implementare controllo cookie di sessione
        self.switch_frame(menuPage.MenuPage)

    #funzione utilizzata per cambiare le varie pagine
    def switch_frame(self, frame_class):
        new_frame = frame_class(master=self)
        #se vi è già un frame (una pagina) in uso, essa viene distrutta
        if self._frame is not None:
            self._frame.destroy()
        #inizializzo la nuova pagina
        self._frame = new_frame
        self._frame.pack()

app = App()
app.mainloop()
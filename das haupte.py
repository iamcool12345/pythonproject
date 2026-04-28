#fidshg,ikrewgjhitg,hfddfjfkjkjfkdfkjbgkjeidhjdsfkjl,gnjdeijlbgfvjfjesadkjfbhdffkjlfkhdfsjilbkjkjfkjnmjbnmjnhjmikjjucvxkjkucxkjkudhjdfkjawjpogh.bsojugswjuorghsw:dsihyutfgrhfgkfrugfhsw'/riugslrgjrfierislgjfdjbvvbnrhgrhgrughruguerguawp/dlf,b,v,gvndidkiw[g;
import os
import tkinter as tk
from tkinter import PhotoImage as bild
from PIL import Image, ImageTk;
bildda    = os.path.join(os.path.dirname(__file__) , "718523.png") 
bildedit = Image.open(bildda)
print(bildedit.format, bildedit.size, bildedit.mode)


class bildui:
    def __init__(self,ui):
        self.x = 1
        self.name =tk.Entry(ui,textvariable="",bg="#ffffff",fg="#000000")
        self.name.grid(row=self.x, column=0, columnspan=1) 
        self.x = self.x +1
        self.okbaddne = tk.Button(ui,text="rain(er) DA!",command=self.open)
        self.okbaddne.grid(row=self.x, column=0, columnspan=2) 
     #   self.testimg = tk.Label(image=bildedit)
      #  self.test = ImageTk.PhotoImage(bildedit)
        
        self.x = self.x +1
        self.pic = tk.Label(ui)  # attach to ui!
        self.pic.grid(row=self.x, column=1)

        self.x = self.x +1
    def open(self):
        print("sddfkpogf.njgf")
        path = self.name.get()
        self.setpicture = Image.open(path) 
        self.testa=ImageTk.PhotoImage(self.setpicture)
        self.pic.config(image=self.testa)
        #self.pic.grid(row=self.x,column=1)
        #self.pic.configure(image=setpicture)

ui = tk.Tk()
ui.configure(background="#ff3ac6")
program = bildui(ui)
ui.mainloop()
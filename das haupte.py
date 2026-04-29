#fidshg,ikrewgjhitg,hfddfjfkjkjfkdfkjbgkjeidhjdsfkjl,gnjdeijlbgfvjfjesadkjfbhdffkjlfkhdfsjilbkjkjfkjnmjbnmjnhjmikjjucvxkjkucxkjkudhjdfkjawjpogh.bsojugswjuorghsw:dsihyutfgrhfgkfrugfhsw'/riugslrgjrfierislgjfdjbvvbnrhgrhgrughruguerguawp/dlf,b,v,gvndidkiw[g;
import os
import tkinter as tk
from PIL import Image, ImageTk;
bildda    = os.path.join(os.path.dirname(__file__) , "718523.png") 
bildedit = Image.open(bildda)
print(bildedit.format, bildedit.size, bildedit.mode)

#"C:\Users\Sebbiarmy\Pictures\0331.mp4 vlcsnap-2026-01-25-20h42m01s288.png"
class bildui:
    def __init__(self,ui):
        self.x = 1
        self.name =tk.Entry(ui,textvariable="",bg="#ffffff",fg="#000000")
        self.name.grid(row=self.x, column=0, columnspan=1) 
        self.x = self.x +1
        self.okbaddne = tk.Button(ui,text="rain(er) DA!",command=self.open)
        self.okbaddne.grid(row=self.x, column=0, columnspan=2) 
        #self.testimg = tk.Label(image=bildedit)
        #self.test = ImageTk.PhotoImage(bildedit)
        self.x = self.x +1
        self.pic = tk.Label(ui) 
        self.pic.grid(row=self.x, column=0)
        self.x = self.x +1
    def open(self):
        print("sddfkpogf.njgf")
        path = self.name.get()
        self.setpicture = Image.open(path).rotate(180)
        self.testa=ImageTk.PhotoImage(self.setpicture)
        self.pic.config(image=self.testa)
        self.pic.grid(column=0)
ui = tk.Tk()
ui.title("irgendwasmitlangenamen")
ui.configure(background="#000000")
ui.geometry('1920x1000')
ui.iconbitmap("icon.ico")
program = bildui(ui)
ui.mainloop()
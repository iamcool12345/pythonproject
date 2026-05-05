#fidshg,ikrewgjhitg,hfddfjfkjkjfkdfkjbgkjeidhjdsfkjl,gnjdeijlbgfvjfjesadkjfbhdffkjlfkhdfsjilbkjkjfkjnmjbnmjnhjmikjjucvxkjkucxkjkudhjdfkjawjpogh.bsojugswjuorghsw:dsihyutfgrhfgkfrugfhsw'/riugslrgjrfierislgjfdjbvvbnrhgrhgrughruguerguawp/dlf,b,v,gvndidkiw[g;
import os
import tkinter as tk
from PIL import Image, ImageTk, ImageDraw, ImageFont        
bildda    = os.path.join(os.path.dirname(__file__) , "718523.png") 
bildedit = Image.open(bildda)
print(bildedit.format, bildedit.size, bildedit.mode)

#"C:\Users\Sebbiarmy\Pictures\0331.mp4 vlcsnap-2026-01-25-20h42m01s288.png"
class bildui:
    def __init__(self,ui):
        self.x = 1
        self.font = "C:/Windows/Fonts/Cantoria MT Std Bold.otf"
        self.fontsize = 100
        self.ubaschreibenwert = tk.IntVar()


        self.beschreibung1= tk.Label(ui,text="DADAINOME",background="#FFFFFF",fg="#FF0000")
        self.beschreibung1.grid(row=self.x, column=0,) 
        self.name =tk.Entry(ui,textvariable="",bg="#ffffff",fg="#000000")
        self.name.grid(row=self.x, column=1, columnspan=1) 
        self.x = self.x +1
        self.beschreibung2= tk.Label(ui,text="Wass soln da stehn??",background="#FFFFFF",fg="#FF0000")
        self.beschreibung2.grid(row=self.x, column=0, ) 
        self.textinput =tk.Entry(ui,textvariable="",bg="#ffffff",fg="#000000")
        self.textinput.grid(row=self.x, column=1,) 
        self.x = self.x +1
        self.beschreibung3= tk.Label(ui,text="Wass soln die schrifd sain???",background="#FFFFFF",fg="#FF0000")
        self.beschreibung3.grid(row=self.x, column=0, ) 
        self.fontinput =tk.Entry(ui,textvariable="",bg="#ffffff",fg="#000000")#combobox?
        self.fontinput.grid(row=self.x, column=1, ) 
        self.x = self.x +1
        self.beschreibung4= tk.Label(ui,text="FARBE R/G/B",background="#FFFFFF",fg="#FF0000")
        self.beschreibung4.grid(row=self.x, column=0,) 
        self.rot =tk.Entry(ui,textvariable="",bg="#ffffff",fg="#000000")
        self.rot.grid(row=self.x, column=1) 
        self.grun =tk.Entry(ui,textvariable="",bg="#ffffff",fg="#000000")
        self.grun.grid(row=self.x, column=2,sticky="W") 
        self.blau =tk.Entry(ui,textvariable="",bg="#ffffff",fg="#000000")
        self.blau.grid(row=self.x, column=3) 
        self.x = self.x +1
        self.beschreibung4= tk.Label(ui,text="POSITION X/Y",background="#FFFFFF",fg="#FF0000")
        self.beschreibung4.grid(row=self.x, column=0,) 
        self.posx =tk.Entry(ui,textvariable="",bg="#ffffff",fg="#000000")
        self.posx.grid(row=self.x, column=1) 
        self.posy =tk.Entry(ui,textvariable="",bg="#ffffff",fg="#000000")
        self.posy.grid(row=self.x, column=2,sticky="W") 
        self.x = self.x +1
        self.okbaddne = tk.Button(ui,text="rain(er) DA!",command=self.open)
        self.okbaddne.grid(row=self.x, column=0) 
        self.ubaschreiben= tk.Checkbutton(ui,text="orignal ubaschreiben",variable=self.ubaschreibenwert, onvalue=1,offvalue=0,fg="#ffffff",bg="#000000")
        self.ubaschreiben.grid(row=self.x, column=1) 
        #self.testimg = tk.Label(image=bildedit)
        #self.test = ImageTk.PhotoImage(bildedit)
        self.x = self.x +1
        self.pic = tk.Label(ui) 
        self.pic.grid(row=self.x, column=0)
        self.x = self.x +1
    def open(self):
        print("sddfkpogf.njgf")
        path = self.name.get()
        text = self.textinput.get()
        if text!="":
            
            self.setpicture = Image.open(path)
            self.neuesbild = f"{path}_barbeided.png"
            x= self.posx.get()
            y = self.posy.get()
            self.textcursor=(int(x),int(y))
            r = self.rot.get()
            g = self.grun.get()
            b = self.blau.get()
            self.textcolor=(int(r),int(g),int(b))
            self.configured_font = ImageFont.truetype(self.font, size=self.fontsize)
            malen=ImageDraw.Draw(self.setpicture)
            malen.text(self.textcursor,text,font=self.configured_font,fill=(self.textcolor))
            if self.ubaschreibenwert == 0:
                self.setpicture.save(self.neuesbild)
                self.bild = Image.open(self.neuesbild)
                print("weg")
            else:
              #  self.setpicture.save(self.setpicture)
               # self.bild = Image.open(self.setpicture)
               # print("bhalten")
                self.setpicture.save(self.neuesbild)
                self.bild = Image.open(self.neuesbild)
            self.testa=ImageTk.PhotoImage(self.bild)

        else:
            self.setpicture = Image.open(path).rotate(180)
            self.testa=ImageTk.PhotoImage(self.setpicture)
        self.pic.config(image=self.testa)
        self.pic.grid(column=0,row=self.x,columnspan=10)
ui = tk.Tk()
ui.title("irgendwasmitlangenamen")
ui.configure(background="#000000")
#ui.geometry('1920x1000')
ui.iconbitmap("icon.ico")
program = bildui(ui)
ui.mainloop()
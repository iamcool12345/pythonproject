#fidshg,ikrewgjhitg,hfddfjfkjkjfkdfkjbgkjeidhjdsfkjl,gnjdeijlbgfvjfjesadkjfbhdffkjlfkhdfsjilbkjkjfkjnmjbnmjnhjmikjjucvxkjkucxkjkudhjdfkjawjpogh.bsojugswjuorghsw:dsihyutfgrhfgkfrugfhsw'/riugslrgjrfierislgjfdjbvvbnrhgrhgrughruguerguawp/dlf,b,v,gvndidkiw[g;
import os
import tkinter as tk
from PIL import Image, ImageTk, ImageDraw, ImageFont        
bildda    = os.path.join(os.path.dirname(__file__) , "718523.png") 
bildedit = Image.open(bildda)
import os
import shutil
print(bildedit.format, bildedit.size, bildedit.mode)

#"C:\Users\Sebbiarmy\Pictures\0331.mp4 vlcsnap-2026-01-25-20h42m01s288.png"
class bildui:
    def __init__(self,ui):
        self.x = 1
        self.font = "C:/Windows/Fonts/Cantoria MT Std Bold.otf"
        
        self.ubaschreibenwert = tk.IntVar()
        self.doppeltextwert = tk.IntVar()

        self.beschreibung1= tk.Label(ui,text="DADAINOME",background="#FFFFFF",fg="#FF0000") #EINLESUNGSDATEI
        self.beschreibung1.grid(row=self.x, column=0,)                                      
        self.name =tk.Entry(ui,textvariable="",bg="#ffffff",fg="#000000")
        self.name.grid(row=self.x, column=1, columnspan=1) 
        self.x = self.x +1

        self.beschreibung2= tk.Label(ui,text="Wass soln da stehn??",background="#FFFFFF",fg="#FF0000")  #WAS DRAUFGESCHRIEBEN WERDEN SOLL
        self.beschreibung2.grid(row=self.x, column=0, ) 
        self.textinput =tk.Entry(ui,textvariable="",bg="#ffffff",fg="#000000")
        self.textinput.grid(row=self.x, column=1,) 
        self.x = self.x +1

        self.beschreibung3= tk.Label(ui,text="Wass soln die schrifd sain??? und grose????",background="#FFFFFF",fg="#FF0000") #schrifdart
        self.beschreibung3.grid(row=self.x, column=0, ) 
        self.fontinput =tk.Entry(ui,textvariable="",bg="#ffffff",fg="#000000")#combobox?
        self.fontinput.grid(row=self.x, column=1, ) 
        self.fontsize =tk.Entry(ui,textvariable="",bg="#ffffff",fg="#000000")
        self.fontsize.grid(row=self.x, column=2, ) 
        self.x = self.x +1

        self.beschreibung4= tk.Label(ui,text="FARBE R/G/B",background="#FFFFFF",fg="#FF0000") #obere Farbe
        self.beschreibung4.grid(row=self.x, column=0,) 
        self.rot =tk.Entry(ui,textvariable="",bg="#ffffff",fg="#000000")
        self.rot.grid(row=self.x, column=1) 
        self.grun =tk.Entry(ui,textvariable="",bg="#ffffff",fg="#000000")
        self.grun.grid(row=self.x, column=2,sticky="W") 
        self.blau =tk.Entry(ui,textvariable="",bg="#ffffff",fg="#000000")
        self.blau.grid(row=self.x, column=3) 
        self.x = self.x +1

        self.beschreibung5= tk.Label(ui,text="HINTEREFARBE R/G/B richtung +-",background="#FFFFFF",fg="#FF0000") #hinter Farbe
        self.beschreibung5.grid(row=self.x, column=0,) 
        self.roth =tk.Entry(ui,textvariable="",bg="#ffffff",fg="#000000")
        self.roth.grid(row=self.x, column=1) 
        self.grunh =tk.Entry(ui,textvariable="",bg="#ffffff",fg="#000000")
        self.grunh.grid(row=self.x, column=2,sticky="W") 
        self.blauh =tk.Entry(ui,textvariable="",bg="#ffffff",fg="#000000")
        self.blauh.grid(row=self.x, column=3) 
        self.wierum =tk.Entry(ui,textvariable="",bg="#ffffff",fg="#000000")
        self.wierum.grid(row=self.x, column=4) 
        self.x = self.x +1

        self.beschreibung4= tk.Label(ui,text="POSITION X/Y Abstand schib",background="#FFFFFF",fg="#FF0000")
        self.beschreibung4.grid(row=self.x, column=0,) 
        self.posx =tk.Entry(ui,textvariable="",bg="#ffffff",fg="#000000")
        self.posx.grid(row=self.x, column=1) 
        self.posy =tk.Entry(ui,textvariable="",bg="#ffffff",fg="#000000")
        self.posy.grid(row=self.x, column=2,sticky="W") 
        self.abstand =tk.Entry(ui,textvariable="",bg="#ffffff",fg="#000000")
        self.abstand.grid(row=self.x, column=3,sticky="W") 
        self.x = self.x +1

        self.okbaddne = tk.Button(ui,text="rain(er) DA!",command=self.open)
        self.okbaddne.grid(row=self.x, column=0) 
        self.ubaschreiben= tk.Checkbutton(ui,text="orignal ubaschreiben",variable=self.ubaschreibenwert, onvalue=1,offvalue=0,fg="#FF0000",bg="#000000")
        self.ubaschreiben.grid(row=self.x, column=1) 
        self.doppeltext= tk.Checkbutton(ui,text="doppeltext",variable=self.doppeltextwert, onvalue=1,offvalue=0,fg="#FF0000",bg="#000000")
        self.doppeltext.grid(row=self.x, column=2) 


        self.x = self.x +1
        self.pic = tk.Label(ui) 
        self.pic.grid(row=self.x, column=0)
        self.x = self.x +1
    def open(self):
        #print("sddfkpogf.njgf")
        path = self.name.get()
        text = self.textinput.get()
        fontd = self.fontinput.get() or self.font
        if text!="":
            self.setpicture = Image.open(path)
            self.neuesbild = f"{path}_barbeided.png"
            x= self.posx.get()   or 0
            y = self.posy.get()  or 0
            self.textcursor=(int(x),int(y))
            r = self.rot.get()   or 0
            g = self.grun.get()  or 0
            b = self.blau.get()  or 0
            self.textcolor=(int(r),int(g),int(b))
            grose = self.fontsize.get() or 30
            self.configured_font = ImageFont.truetype(fontd, size=int(grose))
            malen=ImageDraw.Draw(self.setpicture)
            malen.text(self.textcursor,text,font=self.configured_font,fill=(self.textcolor))
            if self.doppeltextwert.get() == 1:
                print("es wird doppelt gmacht")
                richtung = self.wierum.get()
                print(f"RICHTUNG{richtung}")
                if richtung == "+":
                    print("PLUS")
                    posx = int(self.abstand.get()) + int(x)
                    self.textcursor=(posx,int(y))
                else:
                    print("MINUS")
                    posx = int(x) - int(self.abstand.get()) 
                    self.textcursor=(posx,int(y))
                r = self.roth.get() or 0
                g = self.grunh.get() or 0 
                b = self.blauh.get() or 0
                self.textcolor=(int(r),int(g),int(b))
                malen.text(self.textcursor,text,font=self.configured_font,fill=(self.textcolor))
            if self.ubaschreibenwert.get() == 1:
                self.setpicture.save(self.neuesbild)
                self.setpicture.close()
                os.remove(path)
                shutil.copyfile(self.neuesbild,path)
                self.setpicture = Image.open(path)
                self.bild = Image.open(path)
                os.remove(self.neuesbild)
                print("weg")
            else:
                self.setpicture.save(self.neuesbild)
                self.bild = Image.open(self.neuesbild)
                print("bhalten")
            self.testa=ImageTk.PhotoImage(self.bild)

        else:
            self.setpicture = Image.open(path)#.rotate(180)
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
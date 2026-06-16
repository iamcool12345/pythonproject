#fidshg,ikrewgjhitg,hfddfjfkjkjfkdfkjbgkjeidhjdsfkjl,gnjdeijlbgfvjfjesadkjfbhdffkjlfkhdfsjilbkjkjfkjnmjbnmjnhjmikjjucvxkjkucxkjkudhjdfkjawjpogh.bsojugswjuorghsw:dsihyutfgrhfgkfrugfhsw'/riugslrgjrfierislgjfdjbvvbnrhgrhgrughruguerguawp/dlf,b,v,gvndidkiw[g;
import os

from win32api import GetSystemMetrics
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw, ImageFont        
#bildda    = os.path.join(os.path.dirname(__file__) , "718523.png") 
#bildedit = Image.open(bildda)
import os
import shutil
import pygame as sounds
#print(bildedit.format, bildedit.size, bildedit.mode)
#"C:\Users\Sebbiarmy\Pictures\0331.mp4 vlcsnap-2026-01-25-20h42m01s288.png"
class bildui:
    def __init__(self,ui):
        self.verkleinerungszahl = 70
        self.bildschirmhöhe = GetSystemMetrics(1)
        self.bildschirmbreite = GetSystemMetrics(0)
        self.verfügbarehöhe = self.bildschirmhöhe /100 * int(self.verkleinerungszahl)
        print(f"{self.bildschirmbreite}x{self.bildschirmhöhe}")
        self.x = 1
        #self.font = "C:/Windows/Fonts/Cantoria MT Std Bold.otf"
        self.fontfolder = "C:/Windows/Fonts/"
        self.ubaschreibenwert = tk.IntVar()
        self.doppeltextwert = tk.IntVar()
        self.ausgwählteschrift = tk.StringVar()

        self.beschreibung1= tk.Label(ui,text="Bildname: ",background="#FFFFFF",fg="#FF0000") #EINLESUNGSDATEI
        self.beschreibung1.grid(row=self.x, column=0,)                                      
        self.name =tk.Entry(ui,textvariable="",bg="#ffffff",fg="#000000")
        self.name.grid(row=self.x, column=1, columnspan=1) 
        self.x = self.x +1

        self.beschreibung2= tk.Label(ui,text="Wass soln da stehn??",background="#FFFFFF",fg="#FF0000")
        self.beschreibung2.grid(row=self.x, column=0, ) 
        self.textinput =tk.Entry(ui,textvariable="",bg="#ffffff",fg="#000000")
        self.textinput.grid(row=self.x, column=1,) 
        self.x = self.x +1

        self.beschreibung3= tk.Label(ui,text="Wass soln die schrift sein??? und gröse????",background="#FFFFFF",fg="#FF0000") #schriftart
        self.beschreibung3.grid(row=self.x, column=0, ) 
        #self.fontinput =tk.Entry(ui,textvariable="",bg="#ffffff",fg="#000000")#combobox?
        
        self.fontinput = ttk.Combobox(ui,textvariable="eigene links >>")
        self.fontinput['values']= ('eigene links angeben >>','kremlin','Clannad_Round_Regular','13383','lexia_','HammerSickle','')
        self.fontinput['state'] = 'readonly'
        self.fontinput.index(2)
        self.fontinput.grid(row=self.x, column=1, ) 
        self.fontinputcustom =tk.Entry(ui,textvariable="",bg="#ffffff",fg="#000000")
        self.fontinputcustom.grid(row=self.x, column=2, ) 
        self.fontsize =tk.Entry(ui,textvariable="",bg="#ffffff",fg="#000000")
        self.fontsize.grid(row=self.x, column=3, ) 
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
        self.doppeltextrichtung = ttk.Combobox(ui,textvariable="vorwärts")
        self.doppeltextrichtung['values']= ('vorwärts','rückwärts')
        self.doppeltextrichtung['state'] = 'readonly'
        self.doppeltextrichtung.grid(row=self.x, column=4) 
        self.doppeltextrichtung.index(0)
   #     self.wierum =tk.Entry(ui,textvariable="",bg="#ffffff",fg="#000000")
    #    self.wierum.grid(row=self.x, column=4) 
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
        self.anzeigekasten=tk.Listbox(ui,background="#5fa41c",width=100)
        self.anzeigekasten.grid(row=1, column=6, columnspan=1,rowspan=5)
        self.anzeigecount = 0;

        self.x = self.x +1
        self.pic = tk.Label(ui) 
        self.pic.grid(row=self.x, column=0)
        self.x = self.x +1
    def open(self):
        sounds.mixer.init()
        sounds.mixer.music.load("sounds\ähhhmmmm.mp3")
        sounds.mixer.music.play()
        while sounds.mixer.music.get_busy():
            pass
        #print("sddfkpogf.njgf")
        path = self.name.get()
        text = self.textinput.get()
        schrift = self.fontinput.get()
        print(schrift)
        if schrift!='eigene links >>': #combobox benuzadefiniert ausgwählt dann die selbst reingschribne nehmen
            fontd=self.fontfolder+schrift+".ttf"
        else:
            fontd = self.fontinputcustom.get() or self.font
        #else wenn combobox was ausgwählt
    
        if text!="":
            try:
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
                self.anzeigeboxschreiben(f"rainer schwingt seinen flotten pinsl und mahlt ezdaller wie ein ArBeiTsSüchTiGeR Oger den TExt {text} auf DeIn BilD")

            except Exception as e:
                self.anzeigeboxschreiben(f"FEHLARRRRRRR gib ezaller fieleicht mal teggsd an!! {e}")
            if self.doppeltextwert.get() == 1:
                try:
                    print("es wird doppelt gmacht")
                    richtung = self.doppeltextrichtung.get()
                    print(f"RICHTUNG{richtung}")
                    if richtung == "vorwärts":
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
                    self.anzeigeboxschreiben(f"rainer schwingt seinen flotten pinsl erneut und mahlt ezdaller wie ein ArBeiTsSüchTiGeR Oger den TExt {text} nochma auf DeIn BilD")
                except:
                    self.anzeigeboxschreiben(f"rainer hats net gschafft den text erneut zu schreiben")
                    sounds.mixer.music.load("sounds\wie_bidde.mp3")
                    sounds.mixer.music.play()
                    while sounds.mixer.music.get_busy():
                        pass
            if self.ubaschreibenwert.get() == 1:#altes überschreiben
                self.setpicture.save(self.neuesbild)
                self.setpicture.close()
                os.remove(path)
                shutil.copyfile(self.neuesbild,path)
                self.setpicture = Image.open(path)
                self.bild = Image.open(path)
                os.remove(self.neuesbild)
                self.anzeigeboxschreiben(f"nach der arbeid zermeddlt rainer dein originales bild")
                print("weg")
            else:
                self.setpicture.save(self.neuesbild)
                self.bild = Image.open(self.neuesbild)
                print("bhalten")
            self.testa=ImageTk.PhotoImage(self.bild)
    ##    else:
        try:
            self.setpicture = Image.open(path)#.rotate(180)
            self.testa=ImageTk.PhotoImage(self.setpicture)  
            höhe = self.testa.height()
            breite = self.testa.width()
            
            if höhe>self.verfügbarehöhe:
            #    self.setpicture
                self.setpicture.close()
                self.setpicture = Image.open(path).resize((int(breite/100*int(self.verkleinerungszahl)),int(self.verfügbarehöhe)))
                print("zu gros!")
                self.testa=ImageTk.PhotoImage(self.setpicture)
                höhe = self.testa.height()
                breite = self.testa.width()
            
            self.pic.config(image=self.testa)
            self.pic.grid(column=0,row=self.x,columnspan=10)
            self.anzeigeboxschreiben(f"Die auflösung des bilds ist:『{self.testa.width()}x{self.testa.height()}』")
            sounds.mixer.music.load("sounds\drache_lacht_5.mp3")
            sounds.mixer.music.play()
        except Exception as e:
            self.anzeigeboxschreiben(f"FEHLARRRRRRR gib ezaller fieleicht mal a dadai an!!{e}")
            sounds.mixer.music.load("sounds\du_scheiß_idiot_alder.mp3")
            sounds.mixer.music.play()
            while sounds.mixer.music.get_busy():
                pass



        
        
    def anzeigeboxschreiben(self,text):
        self.anzeigecount = self.anzeigecount +1
        if self.anzeigecount > 10:
            self.anzeigekasten.delete(0,'end')
            self.anzeigecount = 0
        self.anzeigekasten.insert(tk.END,text)

ui = tk.Tk()
sounds.mixer.init()
sounds.mixer.music.load("sounds\hagebuddne.mp3")
sounds.mixer.music.play()
while sounds.mixer.music.get_busy():
    pass
sounds.mixer.music.load("sounds\meddlloid3.mp3")
sounds.mixer.music.play()
ui.title("irgendwasmitlangenamen")
ui.configure(background="#000000")
def play_sound(a):
    sounds.mixer.music.load("sounds\yes.mp3")
    sounds.mixer.music.play()
ui.bind_class("Entry","<KeyRelease>", play_sound)
#ui.geometry('1920x1000')
ui.iconbitmap("icon.ico")
program = bildui(ui)
ui.mainloop()

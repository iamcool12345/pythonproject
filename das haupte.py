import os
from win32api import GetSystemMetrics #für bildschirmgröße
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw, ImageFont        
import os
import shutil
import pygame as sounds
ogerbild = os.path.join(os.path.dirname(__file__) , "oger.png") 
class bildui:
    def __init__(self,ui):
        self.verkleinerungszahl = 60
        self.bildschirmhöhe = GetSystemMetrics(1)
        self.bildschirmbreite = GetSystemMetrics(0)
        self.verfügbarehöhe = self.bildschirmhöhe /100 * int(self.verkleinerungszahl)
        print(f"größe:{self.bildschirmbreite}x{self.bildschirmhöhe}")
        self.x = 1
        self.schriftenordner = "C:/Windows/Fonts/"
        self.überschreibenwert = tk.IntVar()
        self.doppeltextwert = tk.IntVar()
        self.ausgwählteschrift = tk.StringVar()
        #zeile 1
        self.beschreibung1= tk.Label(ui,text="Bildname: ",background="#FFFFFF",fg="#FF0000") #EINLESUNGSDATEI
        self.beschreibung1.grid(row=self.x, column=0,)                                      
        self.name =tk.Entry(ui,textvariable="",bg="#ffffff",fg="#000000")
        self.name.grid(row=self.x, column=1, columnspan=1) 
        self.oger=ImageTk.PhotoImage(Image.open(ogerbild))  
        self.ogeranzeigen = tk.Label(image=self.oger,background="#000000")
        self.ogeranzeigen.grid(row=0,column=4,rowspan=5)
        self.x = self.x +1
        #zeile 2
        self.beschreibung2= tk.Label(ui,text="Wass soln da stehn??",background="#FFFFFF",fg="#FF0000")
        self.beschreibung2.grid(row=self.x, column=0, ) 
        self.textinput =tk.Entry(ui,textvariable="",bg="#ffffff",fg="#000000")
        self.textinput.grid(row=self.x, column=1,) 
        self.x = self.x +1
        #zeile 3
        self.beschreibung3= tk.Label(ui,text="Wass soln die schrift sein? und größe?",background="#FFFFFF",fg="#FF0000") #schriftart
        self.beschreibung3.grid(row=self.x, column=0, ) 
        self.fontinput = ttk.Combobox(ui,textvariable="eigene links >>",height=0,font=('C:/Windows/fonts/Cantoria MT Std Regular',9))
        self.fontinput['values']= ('eigene links angeben >>','kremlin','Clannad_Round_Regular','13383','lexia_','HammerSickle','Cantoria MT Std Regular')
        self.fontinput['state'] = 'readonly'
        self.fontinput.insert(0,"eigene links >>")
        self.fontinput.grid(row=self.x, column=1, ) 
        self.fontinputcustom =tk.Entry(ui,textvariable="",bg="#ffffff",fg="#000000",text="hier eigene")
        self.fontinputcustom.insert(0,"hier eigene angeben")
        self.fontinputcustom.grid(row=self.x, column=2, ) 
        self.fontsize =tk.Entry(ui,textvariable="",bg="#ffffff",fg="#000000")
        self.fontsize.grid(row=self.x, column=3, ) 
        self.x = self.x +1
        #zeile 4
        self.beschreibung4= tk.Label(ui,text="FARBE R/G/B",background="#FFFFFF",fg="#FF0000") #obere Farbe
        self.beschreibung4.grid(row=self.x, column=0,) 
        self.rot =tk.Entry(ui,textvariable="",bg="#ffffff",fg="#000000")
        self.rot.grid(row=self.x, column=1) 
        self.grun =tk.Entry(ui,textvariable="",bg="#ffffff",fg="#000000")
        self.grun.grid(row=self.x, column=2,sticky="W") 
        self.blau =tk.Entry(ui,textvariable="",bg="#ffffff",fg="#000000")
        self.blau.grid(row=self.x, column=3) 
        self.x = self.x +1
        #zeile 5
        self.beschreibung5= tk.Label(ui,text="HINTEREFARBE R/G/B richtung",background="#FFFFFF",fg="#FF0000") #hinter Farbe
        self.beschreibung5.grid(row=self.x, column=0,) 
        self.rotdoppel =tk.Entry(ui,textvariable="",bg="#ffffff",fg="#000000")
        self.rotdoppel.grid(row=self.x, column=1) 
        self.gründoppel =tk.Entry(ui,textvariable="",bg="#ffffff",fg="#000000")
        self.gründoppel.grid(row=self.x, column=2,sticky="W") 
        self.blaudoppel =tk.Entry(ui,textvariable="",bg="#ffffff",fg="#000000")
        self.blaudoppel.grid(row=self.x, column=3) 
        self.doppeltextrichtung = ttk.Combobox(ui,textvariable="vorwärts",height=0,font=('C:/Windows/fonts/Cantoria MT Std Regular',9))
        self.doppeltextrichtung['values']= ('vorwärts','rückwärts')
        self.doppeltextrichtung['state'] = 'readonly'
        self.doppeltextrichtung.grid(row=self.x, column=4) 
        self.doppeltextrichtung.index(0)
        self.x = self.x +1
        #zeile 6
        self.beschreibung4= tk.Label(ui,text="POSITION X/Y Abstand schib",background="#FFFFFF",fg="#FF0000")
        self.beschreibung4.grid(row=self.x, column=0,) 
        self.posx =tk.Entry(ui,textvariable="",bg="#ffffff",fg="#000000")
        self.posx.grid(row=self.x, column=1) 
        self.posy =tk.Entry(ui,textvariable="",bg="#ffffff",fg="#000000")
        self.posy.grid(row=self.x, column=2,sticky="W") 
        self.abstand =tk.Entry(ui,textvariable="",bg="#ffffff",fg="#000000")
        self.abstand.grid(row=self.x, column=3,sticky="W") 
        self.x = self.x +1
        #zeile 7
        self.okbaddne = tk.Button(ui,text="     rain(er) DA!    ",command=self.open,height=0,padx=0,pady=0,font=('C:/Windows/fonts/Cantoria MT Std Regular',8))
        self.okbaddne.grid(row=self.x, column=0) 
        self.überschreiben= tk.Checkbutton(ui,text="orignal überschreiben",variable=self.überschreibenwert, onvalue=1,offvalue=0,fg="#FF0000",bg="#000000")
        self.überschreiben.grid(row=self.x, column=1) 
        self.doppeltext= tk.Checkbutton(ui,text="doppeltext",variable=self.doppeltextwert, onvalue=1,offvalue=0,fg="#FF0000",bg="#000000")
        self.doppeltext.grid(row=self.x, column=2) 
        self.anzeigekasten=tk.Listbox(ui,background="#000000",foreground="#00ffff",width=100,highlightcolor="#000000",borderwidth=0,highlightbackground="#000000")
        self.anzeigekasten.grid(row=1, column=6, columnspan=1,rowspan=5)
        self.anzeigecount = 0
        #das bild
        self.x = self.x +1
        self.pic = tk.Label(ui,background="#000000") 
        self.pic.grid(row=self.x, column=0)
        self.x = self.x +1
    def open(self):
        sounds.mixer.init()
        sounds.mixer.music.load("sounds/ähhhmmmm.mp3")
        sounds.mixer.music.play()
        while sounds.mixer.music.get_busy():
            pass
        #print("sddfkpogf.njgf")
        path = self.name.get()
        text = self.textinput.get()
        schrift = self.fontinput.get()
        print(schrift)
        if schrift!='eigene links >>': 
            fontd=self.schriftenordner+schrift+".ttf"
        else:
            fontd = self.fontinputcustom.get() or self.font
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
                sounds.mixer.music.load("sounds/wie_bidde.mp3")
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
                    r = self.rotdoppel.get() or 0
                    g = self.gründoppel.get() or 0 
                    b = self.blaudoppel.get() or 0
                    self.textcolor=(int(r),int(g),int(b))
                    malen.text(self.textcursor,text,font=self.configured_font,fill=(self.textcolor))
                    self.anzeigeboxschreiben(f"rainer schwingt seinen flotten pinsl erneut und mahlt ezdaller wie ein ArBeiTsSüchTiGeR Oger den TExt {text} nochma auf DeIn BilD")
                except:
                    self.anzeigeboxschreiben(f"rainer hats net gschafft den text erneut zu schreiben")
                    sounds.mixer.music.load("sounds/wie_bidde.mp3")
                    sounds.mixer.music.play()
                    while sounds.mixer.music.get_busy():
                        pass
            if self.überschreibenwert.get() == 1:#altes überschreiben
                self.setpicture.save(self.neuesbild)
                self.setpicture.close()
                os.remove(path)
                shutil.copyfile(self.neuesbild,path)
             #   self.setpicture = Image.open(path)
             #  self.bild = Image.open(path)
                os.remove(self.neuesbild)
                self.anzeigeboxschreiben(f"nach der arbeid zermeddlt rainer dein originales bild")
                print("weg")
            else:
                path = self.neuesbild
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
            self.anzeigeboxschreiben(f"Die originale auflösung des bilds ist:『{self.testa.width()}x{self.testa.height()}』")
            if höhe>self.verfügbarehöhe:
                self.setpicture.close()
                breite = int(breite/100*int(self.verkleinerungszahl))
                print("bild ist zu groß zum anzeigen")
                höhe = int(self.verfügbarehöhe)
                self.setpicture = Image.open(path).resize((int(breite),int(höhe)))
                self.anzeigeboxschreiben(f"Die verkleinerte angezeigte größe des bilds ist:『{breite}x{höhe}』")
            if breite > self.bildschirmbreite:
                breite = self.bildschirmbreite#int(breite/100*int(self.verkleinerungszahl))
                print("immer noch zu gros!")
                höhe = int(self.verfügbarehöhe)
                self.setpicture = Image.open(path).resize((int(breite),int(höhe)))
                self.anzeigeboxschreiben(f"Die erneut verkleinerte angezeigte größe des bilds ist:『{breite}x{höhe}』")
            self.testa=ImageTk.PhotoImage(self.setpicture)
            höhe = self.testa.height()
            breite = self.testa.width()
            self.pic.config(image=self.testa)
            self.pic.grid(column=0,row=self.x,columnspan=10)
            
            sounds.mixer.music.load("sounds/drache_lacht_5.mp3")
            sounds.mixer.music.play()
        except Exception as e:
            self.anzeigeboxschreiben(f"FEHLARRRRRRR gib ezaller fieleicht mal a dadai an!!{e}")
            sounds.mixer.music.load("sounds/du_scheiß_idiot_alder.mp3")
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
sounds.mixer.music.load("sounds/hagebuddne.mp3")
sounds.mixer.music.play()
while sounds.mixer.music.get_busy():
    pass
sounds.mixer.music.load("sounds/meddlloid3.mp3")
sounds.mixer.music.play()
ui.title("irgendwasmitlangenamen")
ui.configure(background="#000000")
def play_sound(a):
    #print(a)
    print(f"jemand schreibt {a.keysym}")
    sounds.mixer.music.load("sounds/yes.mp3")
    sounds.mixer.music.play()
ui.bind_class("Entry","<KeyRelease>", play_sound)
#ui.geometry('1920x1000')
ui.iconbitmap("programmtitelbild.ico")
program = bildui(ui)
ui.mainloop()

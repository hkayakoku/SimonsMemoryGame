from tkinter import *
import functools
import random
import time


fonts = ['FreeMono', 'SansSerif' ,'NewCourier', 'TimesNewRoman', 'FreeSans','Ubuntu','Kinnari','Loma','FreeSerif','Georgia',
'Arial','Helvetica','Impact','Tohoma','Verdana','']
fontSizes = [50 , 64 , 46 , 57 , 41 , 49 ,55 , 38]
color = ['green','red','brown','gray','Khaki','yellow',
'purple','coral','gold','orange','deepskyblue','tomato']


LEVEL = 0
liste = []

def initialize():
        global LEVEL
        LEVEL = LEVEL + 1
        canvas.delete("all")
        button1["text"] = "Started !!!"
        canvas.after (15,deneme)
        
def deneme():
        
        global liste
        liste = []

        for i in range(0,LEVEL):
                number = random.randint(0,100)
                liste.append(number)
                
        for i in range(0,len(liste)):                    
                x = random.randint(15,400)
                y = random.randint(15,300)
                fontnum = random.randint(0,len(fonts)-1)
                sizenum = random.randint(25,42)
                colornum = random.randint(0,len(color)-1)

                canvas_id2 = canvas.create_text(100, 100, anchor="nw",
                fill = color[colornum], font = (fonts[fontnum],sizenum))
                
                canvas.itemconfig(canvas_id2, text=liste[i])
                canvas.move(canvas_id2,x,y)
                canvas.update()
                canvas.after (1500)
        canvas.delete("all")
        ikinciekran()
        
def ikinciekran():
        deger = Tk()
        deger.geometry('200x100-300+250')
        etiket = Label (deger,text = "Enter Value: ")
        etiket.pack()
        yeni = Frame(deger)
        yeni.pack(pady = 12, padx = 5,side = BOTTOM)
        giris = Entry(deger)
        giris.focus()
        giris.pack()
        buton1 = Button(yeni , text = "OK!" , command = functools.partial(degeral,giris,deger))  
        buton1.pack()     
        
def degeral(giris,deger):
        metin = giris.get()
        deger.destroy()
        global LEVEL
        str1 = ' '.join(str(e) for e in liste)
        if metin == str1:
                canvas_id2 = canvas.create_text(200, 200, anchor="nw",
                fill = 'green', font = ('Helvetica',40))
                
                canvas.itemconfig(canvas_id2, text="LEVEL UP!\nLEVEL: " + str(LEVEL+1))
                canvas.after (2000,initialize)
        else:
                global liste
                canvas_id2 = canvas.create_text(200, 200, anchor="nw",
                fill = 'red', font = ('Helvetica',40))
                canvas.itemconfig(canvas_id2, text="GAME OVER\nScore: " + str(LEVEL-1))
                canvas_id3 = canvas.create_text(200, 400, anchor="nw",
                fill = 'green', font = ('Helvetica',20))
                canvas.itemconfig(canvas_id3, text="List: " + str(liste))
                canvas_id4 = canvas.create_text(200, 435, anchor="nw",
                fill = 'orange', font = ('Helvetica',20))
                canvas.itemconfig(canvas_id4, text="You Entered: [" + metin + "]")
                button1["text"] = "New Game" 
                liste = []
                LEVEL = 0
                        
                
        deger.mainloop()

pencere = Tk()
pencere.geometry('800x600-10+10')

canvas = Canvas(pencere, width=800, height=500, bg = "black")
canvas.pack(side="top", fill="both", expand=TRUE)

canvas_id = canvas.create_text(250, 250, anchor="nw",
                fill = 'orange', font = ('Helvetica',17))
canvas.itemconfig(canvas_id,text = "This is Classic Memory Game\n\tPress Start")

button1 = Button (text = "Start" , command = initialize )
button1.pack()

mainloop()

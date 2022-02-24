from tkinter import*
import tkinter as tk
from turtle import left, width
from unittest.util import _MAX_LENGTH


window=Tk()
window.title("HS_Cal V 1.0")
window.configure(background="black")




#labelss

my_label=Label(window,text="©Hashan Sudeera",bg="gray",fg="orange",font="gilbert 5")
my_label.place(x=7,y=5)




#entry box

ent=Entry(window,width=8, relief=RIDGE,border=0,font="Carre 35",justify=RIGHT,bg="gray",fg="white")
ent.place(x=4,y=18)

#funtion

def delete():
        a = ent.get()
        ent.delete(first=len(a)-1,last="end")
def fresult():
        if ent.get() == "":
                pass
        elif ent.get()[0] == "0":
                ent.delete(0,"end")
        else:
                c_res = ent.get()
                c_res = eval(c_res)
                clearf()
                ent.insert("end",c_res)
def clearf():
        ent.delete(0,"end")



#numbers

Char_num1=Button(window,text="9",bg="dimgray",fg="white",font="Carre 25",command=lambda : ent.insert("end","9"),borderwidth=3,relief=RIDGE,width=3,height=1,border=0)
Char_num1.place(x=7,y=60)

Char_num2=Button(window,text="8",bg="dimgray",fg="white",font="Carre 25",command=lambda : ent.insert("end","8"),borderwidth=3,relief=RIDGE,width=3,height=1,border=0)
Char_num2.place(x=62,y=60)

Char_num3=Button(window,text="7",bg="dimgray",fg="white",font="Carre 25",command=lambda : ent.insert("end","7"),borderwidth=3,relief=RIDGE,width=3,height=1,border=0)
Char_num3.place(x=117,y=60)

Char_num4=Button(window,text="6",bg="dimgray",fg="white",font="Carre 25",command=lambda : ent.insert("end","6"),borderwidth=3,relief=RIDGE,width=3,height=1,border=0)
Char_num4.place(x=117,y=100)

Char_num5=Button(window,text="5",bg="dimgray",fg="white",font="Carre 25",command=lambda : ent.insert("end","5"),borderwidth=3,relief=RIDGE,width=3,height=1,border=0)
Char_num5.place(x=62,y=100)

Char_num4=Button(window,text="4",bg="dimgray",fg="white",font="Carre 25",command=lambda : ent.insert("end","4"),borderwidth=3,relief=RIDGE,width=3,height=1,border=0)
Char_num4.place(x=7,y=100)

Char_num3=Button(window,text="3",bg="dimgray",fg="white",font="Carre 25",command=lambda : ent.insert("end","3"),borderwidth=3,relief=RIDGE,width=3,height=1,border=0)
Char_num3.place(x=117,y=140)

Char_num2=Button(window,text="2",bg="dimgray",fg="white",font="Carre 25",command=lambda : ent.insert("end","2"),borderwidth=3,relief=RIDGE,width=3,height=1,border=0)
Char_num2.place(x=62,y=140)

Char_num1=Button(window,text="1",bg="dimgray",fg="white",font="Carre 25",command=lambda : ent.insert("end","1"),borderwidth=3,relief=RIDGE,width=3,height=1,border=0)
Char_num1.place(x=7,y=140)

Char_num0=Button(window,text="0",bg="dimgray",fg="white",font="Carre 25",command=lambda : ent.insert("end","0"),borderwidth=3,relief=RIDGE,width=3,height=1,border=0)
Char_num0.place(x=7,y=180)

Char_num00=Button(window,text="00",bg="dimgray",fg="white",font="Carre 25",command=lambda : ent.insert("end","00"),borderwidth=3,relief=RIDGE,width=3,height=1,border=0)
Char_num00.place(x=62,y=180)

Char_numdot=Button(window,text=".",bg="dimgray",fg="white",font="Carre 25",command=lambda : ent.insert("end","."),borderwidth=3,relief=RIDGE,width=3,height=1,border=0)
Char_numdot.place(x=117,y=180)




#plus,mines,and other buttons


Char_plus=Button(window,text="+",bg="orange",fg="black",font="lkmatara98 14",command=lambda : ent.insert("end","+"),borderwidth=3,relief=RIDGE,width=5,height=1,border=0)
Char_plus.place(x=172,y=100)

Char_mines=Button(window,text="-",bg="orange",fg="black",font="lkmatara98 14",command=lambda : ent.insert("end","-"),borderwidth=3,relief=RIDGE,width=5,height=1,border=0)
Char_mines.place(x=172,y=140)

Char_guna=Button(window,text="x",bg="orange",fg="black",font="lkmatara98 14",command=lambda : ent.insert("end","*"),borderwidth=3,relief=RIDGE,width=5,height=1,border=0)
Char_guna.place(x=172,y=180)

Char_devition=Button(window,text="÷",bg="orange",fg="black",font="lkmatara98 14",command=lambda : ent.insert("end","/"),borderwidth=3,relief=RIDGE,width=5,height=1,border=0)
Char_devition.place(x=172,y=220)

Char_eq=Button(window,text="=",bg="orange",fg="white",font="Carre 25",command=fresult,borderwidth=3,relief=RIDGE,width=7,height=1,border=0)
Char_eq.place(x=7,y=220)

Char_clear=Button(window,text="C",bg="orange",fg="black",font="lkmatara98 14",command=clearf,borderwidth=3,relief=RIDGE,width=5,height=0,border=0)
Char_clear.place(x=172,y=60)

delete = Button(window,text="Del",width=4,command=delete,borderwidth=3,relief=RIDGE,font="lkmatara98 14",bg="white",fg="black",border=0)
delete.place(x=122,y=220)



window.geometry("235x270")
window.mainloop()
from tkinter import *
from tkinter import font

exp = ""


root = Tk()
root.title("CALCULATOR")
icon = PhotoImage(file='icon.png')
root.iconphoto(False,icon)

root.geometry('400x600')
custom_font = font.Font(size=24)

def add_value(vals):
    global exp
    exp = str(exp) +str(vals)
    data.set(exp)

def clear():
    global exp
    exp = ""
    data.set(exp)

def evaluate():
    global exp
    exp = eval(exp)
    data.set(exp)

data = StringVar()

e1 = Entry(root,font=custom_font,textvariable=data)
e1.place(x=22,y=15,height=40,width=350)

btn1 = Button(root,text='1',command=lambda : add_value(1),bg='lightblue')
btn1.place(x=65,y=75,height=60,width=60)

btn2 = Button(root,text='2',command=lambda : add_value(2),bg='lightblue')
btn2.place(x=130,y=75,height=60,width=60)

btn3 = Button(root,text='3',command=lambda : add_value(3),bg='lightblue')
btn3.place(x=195,y=75,height=60,width=60)

btn_add = Button(root,text='+',command=lambda : add_value('+'),bg='lightblue')
btn_add.place(x=260,y=75,height=60,width=60)

btn4 = Button(root,text='4',command=lambda : add_value(4),bg='lightblue')
btn4.place(x=65,y=140,height=60,width=60)

btn5 = Button(root,text='5',command=lambda : add_value(5),bg='lightblue')
btn5.place(x=130,y=140,height=60,width=60)

btn6 = Button(root,text='6',command=lambda : add_value(6),bg='lightblue')
btn6.place(x=195,y=140,height=60,width=60)

btn_sub = Button(root,text='-',command=lambda : add_value('-'),bg='lightblue')
btn_sub.place(x=260,y=140,height=60,width=60)

btn7 = Button(root,text='7',command=lambda : add_value(7),bg='lightblue')
btn7.place(x=65,y=205,height=60,width=60)

btn8 = Button(root,text='8',command=lambda : add_value(8),bg='lightblue')
btn8.place(x=130,y=205,height=60,width=60)

btn9 = Button(root,text='9',command=lambda : add_value(9),bg='lightblue')
btn9.place(x=195,y=205,height=60,width=60)

btn_prod = Button(root,text='*',command=lambda : add_value('*'),bg='lightblue')
btn_prod.place(x=260,y=205,height=60,width=60)

btnD = Button(root,text='.',command=lambda : add_value('.'),bg='lightblue')
btnD.place(x=65,y=270,height=60,width=60)

btn0 = Button(root,text='0',command=lambda : add_value(0),bg='lightblue')
btn0.place(x=130,y=270,height=60,width=60)

btnEq= Button(root,text='/',command=lambda : add_value('/'),bg='lightblue')
btnEq.place(x=195,y=270,height=60,width=60)

btn_div = Button(root,text='=',command=evaluate,bg='lightblue')
btn_div.place(x=260,y=270,height=60,width=60)

btn_C = Button(root,text='CLEAR',command=clear,bg='lightblue')
btn_C.place(x=65,y=335,height=60,width=253)

root.mainloop()

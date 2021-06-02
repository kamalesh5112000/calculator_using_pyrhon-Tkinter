from tkinter import *
import math
window = Tk()
window.title("Calculator")
sc_variable=StringVar()
l=Label(window,text="SCIENTIFIC CALCULATOR",font="lucida 30")
l.grid(row=0,column=0,columnspan=5)
screen=Entry(window,textvariable=sc_variable,font='lucida 30',fg='white',bg='spring green',borderwidth=10)
screen.grid(row=1,column=0,columnspan=5,padx=10,pady=15)

def clicked(display):
    getv=screen.get()
    screen.delete(0,END)
    screen.insert(0,getv+display)
    return
def ac():
    screen.delete(0,END)
    return
def delet():
    cnt=screen.get()
    size=len(cnt)-1
    screen.delete(size,END)

def calculate():
    ans=screen.get()
    ans=eval(ans)
    screen.delete(0,END)
    screen.insert(0,ans)

def scicalc(getval):
    val=getval.widget
    text=val['text']
    no=screen.get()
    output=''
    if text=='deg':
        output=str(math.degrees(float(no)))
    if text=='sin':
        output=str(math.sin(float(no)))
    if text=='cos':
        output=str(math.cos(float(no)))
    if text=='tan':
        output=str(math.tan(float(no)))
    if text=='lg':
        output=str(math.log10(float(no)))
    if text=='obx':
        output=str(1/(float(no)))
    if text=='sqrt':
        output=str(math.sqrt(float(no)))
    if text=='mod':
        output=str(math.modf(float(no)))
    if text=='pi':
        if no=="":
            output=str(math.pi)
        else:
            output=str(float(no)*math.pi)
    if text=='e':
        if no=="":
            output=str(math.e)
        else:
            output=str(math.ev**float(no))
    screen.delete(0,END)
    screen.insert(0,output)

imgsin=PhotoImage(file='D:/calculater/btnsin.png')
btnsin=Button(window,text="sin",image=imgsin,width=60,height=60,borderwidth=0,command=lambda :clicked("sin"))
btnsin.bind("<Button-1>",scicalc)
btnsin.grid(row=2,column=0)
imgcos=PhotoImage(file='D:/calculater/btncos.png')
btncos=Button(window,text="cos",image=imgcos,width=60,height=60,borderwidth=0,command=lambda:clicked("cos"))
btncos.bind("<Button-1>",scicalc)
btncos.grid(row=2,column=1)
imgtan=PhotoImage(file='D:/calculater/btntan.png')
btntan=Button(window,text="tan",image=imgtan,width=60,height=60,borderwidth=0,command=lambda:clicked("tan"))
btntan.bind("<Button-1>",scicalc)
btntan.grid(row=2,column=2)
imgdeg=PhotoImage(file='D:/calculater/btndeg.png')
btndeg=Button(window,text="deg",image=imgdeg,width=60,height=60,borderwidth=0,command=lambda:clicked("deg"))
btndeg.bind("<Button-1>",scicalc)
btndeg.grid(row=2,column=3)
imglog=PhotoImage(file='D:/calculater/btnlog.png')
btnlog=Button(window,text="lg",image=imglog,width=60,height=60,borderwidth=0,command=lambda:clicked("log"))
btnlog.bind("<Button-1>",scicalc)
btnlog.grid(row=2,column=4)
imgsqrt=PhotoImage(file='D:/calculater/btnsqrt.png')
btnsqrt=Button(window,text="sqrt",image=imgsqrt,width=60,height=60,borderwidth=0,command=lambda:clicked("sqrt"))
btnsqrt.bind("<Button-1>",scicalc)
btnsqrt.grid(row=3,column=0)
imgobx=PhotoImage(file='D:/calculater/btnobx.png')
btnobx=Button(window,text="obx",image=imgobx,width=60,height=60,borderwidth=0,command=lambda:clicked("/x"))
btnobx.bind("<Button-1>",scicalc)
btnobx.grid(row=3,column=1)
imgpi=PhotoImage(file='D:/calculater/btnpi.png')
btnpi=Button(window,text="pi",image=imgpi,width=60,height=60,borderwidth=0,command=lambda:clicked("pi"))
btnpi.bind("<Button-1>",scicalc)
btnpi.grid(row=3,column=2)
imge=PhotoImage(file='D:/calculater/btne.png')
btne=Button(window,text="e",image=imge,width=60,height=60,borderwidth=0,command=lambda:clicked("e"))
btne.bind("<Button-1>",scicalc)
btne.grid(row=3,column=3)
imgmod=PhotoImage(file='D:/calculater/btnmod.png')
btnmod=Button(window,text="mod",image=imgmod,width=60,height=60,borderwidth=0,command=lambda:clicked("mod"))
btnmod.bind("<Button-1>",scicalc)
btnmod.grid(row=3,column=4)

img7=PhotoImage(file='D:/calculater/btn7.png')
seven=Button(window,text="7",image=img7,width=60,height=60,borderwidth=0,command=lambda:clicked("7"))
seven.grid(row=4,column=0)
img8=PhotoImage(file='D:/calculater/btn8.png')
eight=Button(window,text="8",image=img8,width=60,height=60,borderwidth=0,command=lambda:clicked("8"))
eight.grid(row=4,column=1)
img9=PhotoImage(file='D:/calculater/btn9.png')
nine=Button(window,text="9",image=img9,width=60,height=60,borderwidth=0,command=lambda:clicked("9"))
nine.grid(row=4,column=2)
imgdel=PhotoImage(file='D:/calculater/btndel.png')
btndel=Button(window,text="DEL",image=imgdel,width=60,height=60,borderwidth=0,command=delet)
btndel.grid(row=4,column=3)
imgac=PhotoImage(file='D:/calculater/btnac.png')
btnac=Button(window,text="AC",image=imgac,width=60,height=60,borderwidth=0,command=ac)
btnac.grid(row=4,column=4)
img4=PhotoImage(file='D:/calculater/btn4.png')
four=Button(window,text="4",image=img4,width=60,height=60,borderwidth=0,command= lambda :clicked("4"))
four.grid(row=5,column=0)
img5=PhotoImage(file='D:/calculater/btn5.png')
five=Button(window,text="5",image=img5,width=60,height=60,borderwidth=0,command=lambda :clicked("5"))
five.grid(row=5,column=1)
img6=PhotoImage(file='D:/calculater/btn6.png')
six=Button(window,text="6",image=img6,width=60,height=60,borderwidth=0,comman=lambda :clicked("6"))
six.grid(row=5,column=2)
imgmul=PhotoImage(file='D:/calculater/btnmul.png')
btnmul=Button(window,text="*",image=imgmul,width=60,height=60,borderwidth=0,command=lambda :clicked("*"))
btnmul.grid(row=5,column=3)
imgdiv=PhotoImage(file='D:/calculater/btndiv.png')
btndiv=Button(window,text="/",image=imgdiv,width=60,height=60,borderwidth=0,command=lambda :clicked("/"))
btndiv.grid(row=5,column=4)
img=PhotoImage(file='D:/btn1.png')
btnimag=Button(window,text="1",image=img,fg="black",width=80,height=60,borderwidth=0,command=lambda :clicked("1"))
btnimag.grid(row=6,column=0)
img2=PhotoImage(file='D:/calculater/btn2.png')
two=Button(window,text="2",image=img2,width=60,height=60,borderwidth=0,command=lambda :clicked("2"))
two.grid(row=6,column=1)
img3=PhotoImage(file='D:/calculater/btn3.png')
three=Button(window,text="3",image=img3,width=60,height=60,borderwidth=0,command=lambda :clicked("3"))
three.grid(row=6,column=2)
imgpls=PhotoImage(file='D:/calculater/btnpls.png')
btnpls=Button(window,text="+",image=imgpls,width=60,height=60,borderwidth=0,command=lambda :clicked("+"))
btnpls.grid(row=6,column=3)
imgmns=PhotoImage(file='D:/calculater/btnmns.png')
btnmns=Button(window,text="-",image=imgmns,width=60,height=60,borderwidth=0,command=lambda :clicked("-"))
btnmns.grid(row=6,column=4)
img0=PhotoImage(file='D:/calculater/btn0.png')
zero=Button(window,text="0",image=img0,width=60,height=60,borderwidth=0,command=lambda :clicked("0"))
zero.grid(row=7,column=0)
imgdot=PhotoImage(file='D:/calculater/btndot.png')
btndot=Button(window,text=".",image=imgpls,width=60,height=60,borderwidth=0,command=lambda :clicked("."))
btndot.grid(row=7,column=1)
imgop=PhotoImage(file='D:/calculater/btnop.png')
btnop=Button(window,text="(",image=imgop,width=60,height=60,borderwidth=0,command=lambda :clicked("("))
btnop.grid(row=7,column=2)
imgcp=PhotoImage(file='D:/calculater/btncp.png')
btncp=Button(window,text=")",image=imgcp,width=60,height=60,borderwidth=0,command=lambda :clicked(")"))
btncp.grid(row=7,column=3)
imgeql=PhotoImage(file='D:/calculater/btneql.png')
btneql=Button(window,text="=",image=imgeql,width=60,height=60,borderwidth=0,bg="green",command=calculate)
btneql.grid(row=7,column=4)

window.mainloop()

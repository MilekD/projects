from tkinter import *
import tkinter.messagebox


def OH():
    a = rownowaznik.get()
    result=56100/a
    a1.set(format(result,'.4f'))
    print (result)

def Izo():
    y=liczba_izo.get()
    i=42*100/y
    a2.set(format(i,'.4f'))
    print(i)

def mas():
    T=temp.get()+273.15 #[K]
    V=v.get()*0.001 #[m^2]
    n=(101300*V)/(8.314*T)
    m=n*18
    a3.set(format(m,'.4f'))
    print(m)


def z():
    zaw=zawart.get()
    inc=inco.get()
    a=(100/a1.get()+((a3.get() * Co.get()) / 100 - zawart.get())/9)*a2.get()*inc
    a4.set(format(a,'.4f'))
    print(a)

def m_pianki():
    m=v.get()*d.get()
    a5.set(format(m,'.4f'))
    print(m)


def il_poliolu():
    x=a5.get()*100/(100+a4.get())
    a6.set(format(x,'.4f'))
    print(x)

def il_izocyj():
    x=a5.get()-a6.get()
    a7.set(format(x,'.4f'))
    print(x)

def m_wody():
    x = (a3.get() * Co.get()) / 100 - zawart.get()
    a8.set(format(x,'.4f'))
    print(x)

def mol():
    T = temp.get() + 273.15  # [K]
    V = v.get() * 0.001  # [m^2]
    n = (101300 * V) / (8.314 * T)
    a9.set(format(n,'.4f'))

def masa_spien():
    x=((100-Co.get())*a9.get()*M.get())/100
    a10.set(format(x,'.4f'))
    print(x)

def all():
    OH()
    Izo()
    mas()
    z()
    m_pianki()
    il_poliolu()
    il_izocyj()
    m_wody()
    mol()
    masa_spien()

def toggle_entry():
    global hidden
    if hidden:
        e.grid(row=8, column=1)
        ee.grid(row=8,column=0,sticky=E)
        eee.grid(row=8,column=2,sticky=W)
        c.grid(row=9,column=1)
        cc.grid(row=9, column=0,sticky=E)
        ccc.grid(row=9, column=2, sticky=W)
        p.grid(row=18, column=1, columnspan=1, sticky='WE')
        pp.grid(row=18, column=0, sticky='E')
        ppp.grid(row=18, column=2,sticky='W')

    else:
        e.grid_remove()
        ee.grid_remove()
        eee.grid_remove()
        c.grid_remove()
        cc.grid_remove()
        ccc.grid_remove()
        p.grid_remove()
        pp.grid_remove()
        ppp.grid_remove()

    hidden = not hidden

def info():
    tkinter.messagebox.showinfo("infoooo","Program do liczenia receptur pianek (wersja demo). \n \n Created by M.D.")

#=================================Root==================================================

root=Tk()
root.title('Pianex')
root.configure(bg='gray14')
#root.iconbitmap(r'spon.ico')
menu=Menu(root)
root.config(menu=menu)

subMenu=Menu(menu,tearoff=0)
menu.add_cascade(label="Info",menu=subMenu)
subMenu.add_command(label="info", command=info)

#=================================Zmienne==============================================
rownowaznik = DoubleVar()
liczba_izo = DoubleVar()
temp = DoubleVar()
v = DoubleVar()
inco = DoubleVar()
zawart = DoubleVar()
d = DoubleVar()
Co=DoubleVar(root,value=100)
M = DoubleVar()

a1 = DoubleVar()
a2= DoubleVar()
a3= DoubleVar()
a4= DoubleVar()
a5= DoubleVar()
a6= DoubleVar()
a7= DoubleVar()
a8= DoubleVar()
a9= DoubleVar()
a10= DoubleVar()

#====================================Labels============================================

label_1=Label(root,text="Wartosc liczby hydroksylowej:",font=("Helvetica",9,"bold"),bg="gray14",fg="white").grid(row=0,sticky=E)
label_2=Label(root,text="Liczba izocyjanianowa:",font=("Helvetica",9,"bold"),bg="gray14",fg="white").grid(row=1,sticky=E)
label_3=Label(root,text="Temperatura pianki:",font=("Helvetica",9,"bold"),bg="gray14",fg="white").grid(row=2,sticky=E)
label_4=Label(root,text="Objetosc pianki:", anchor="e",font=("Helvetica",9,"bold"),bg="gray14",fg="white").grid(row=3,sticky=E)
label_5=Label(root,text="Indeks izocyjanianowy:", anchor="e",font=("Helvetica",9,"bold"),bg="gray14",fg="white").grid(row=4,sticky=E)
label_6=Label(root,text="Zawartosc wody w poliolu:", anchor="e",font=("Helvetica",9,"bold"),bg="gray14",fg="white").grid(row=5,sticky=E)
label_7=Label(root,text="Gestosc pozorna:", anchor="e",font=("Helvetica",9,"bold"),bg="gray14",fg="white").grid(row=6,sticky=E)

label_11=Label(root,text="[mgOH/g]",bg="gray14",fg="white").grid(row=0,column=2,sticky=W)
label_21=Label(root,text="[%]",bg="gray14",fg="white").grid(row=1,column=2,sticky=W)
label_31=Label(root,text="[C]",bg="gray14",fg="white").grid(row=2,column=2,sticky=W)
label_41=Label(root,text="[dm^3]",bg="gray14",fg="white").grid(row=3,column=2,sticky=W)
label_61=Label(root,text="[%mas.]",bg="gray14",fg="white").grid(row=5,column=2,sticky=W)
label_71=Label(root,text="[kg/m^3]",bg="gray14",fg="white").grid(row=6,column=2,sticky=W)


#=======================================ENTRY===========================================

entry_1=Entry(root,textvariable=rownowaznik,bg="pale goldenrod").grid(row=0,column=1)
entry_2=Entry(root,textvariable=liczba_izo,bg="pale goldenrod").grid(row=1,column=1)
entry_3=Entry(root,textvariable=temp,bg="pale goldenrod").grid(row=2,column=1)
entry_4=Entry(root,textvariable=v,bg="pale goldenrod").grid(row=3,column=1)
entry_5=Entry(root,textvariable=inco,bg="pale goldenrod").grid(row=4,column=1)
entry_6=Entry(root,textvariable=zawart,bg="pale goldenrod").grid(row=5,column=1)
entry_7=Entry(root,textvariable=d,bg="pale goldenrod").grid(row=6,column=1)



#=======================================BUTTON===============================================

b = Button(root, text='OBLICZ', command=all,font=("Helvetica",13,"bold"),bg="red3",fg="ghost white").grid(row=10, column=1, padx=5, pady=5)
b2 = Button(root)

#=====================================CHECKBUTTON=============================================

hidden=True
Checkbutton(root, text='Inna zawartosc CO2', command=toggle_entry,bg="gray14",fg="white").grid(row=7, column=0)
e = Entry(root,textvariable=Co,bg="pale goldenrod")
ee=Label(root,text="Udzial CO2 :",font=("Helvetica",9,"bold"),bg="gray14",fg="white")
eee=Label(root,text="[%]",bg="gray14",fg="white")
cc=Label(root,text="Masa molowa spieniacza :",font=("Helvetica",9,"bold"),bg="gray14",fg="white")
ccc=Label(root,text="[g/mol]",bg="gray14",fg="white")
c=Entry(root,textvariable=M,bg="pale goldenrod")

p = Label(root, textvariable=a10, relief='raised',bg="pale goldenrod")
pp=Label(root, text='Ilosc spieniacza:',font=("Helvetica",9,"bold"),bg="gray14",fg="white")
ppp=Label(root,text="[g]",bg="gray14",fg="white")


#=====================================SET_LABELS================================================

Label(root, text='Rownowaznik grup OH w KOH :',font=("Helvetica",9,"bold"),bg="gray14",fg="white").grid(row=11, column=0, sticky='E')
Label(root, text='[g/mol]',bg="gray14",fg="white").grid(row=11, column=2,sticky='W')
Label(root, textvariable=a1, relief='raised',bg="pale goldenrod").grid(row=11, column=1, columnspan=1, sticky='WE')


Label(root, text='Rownowaznik grup izocyjanian. :',font=("Helvetica",9,"bold"),bg="gray14",fg="white").grid(row=12, column=0, sticky='E')
Label(root, textvariable=a2, relief='raised',bg="pale goldenrod").grid(row=12, column=1, columnspan=1, sticky='WE')


Label(root, text='Ilosc wody :',font=("Helvetica",9,"bold"),bg="gray14",fg="white").grid(row=13, column=0, sticky='E')
Label(root, text='[g]',bg="gray14",fg="white").grid(row=13, column=2,sticky='W')
Label(root, textvariable=a8, relief='raised',bg="pale goldenrod").grid(row=13, column=1, columnspan=1, sticky='WE')


Label(root, text='Zap. na skl. izocyjanian.:',font=("Helvetica",9,"bold"),bg="gray14",fg="white").grid(row=14, column=0, sticky='E')
Label(root, text='[g]',bg="gray14",fg="white").grid(row=14, column=2,sticky='W')
Label(root, textvariable=a4, relief='raised',bg="pale goldenrod").grid(row=14, column=1, columnspan=1, sticky='WE')


Label(root, text='Masa pianki :',font=("Helvetica",9,"bold"),bg="gray14",fg="white").grid(row=15, column=0, sticky='E')
Label(root, text='[g]',bg="gray14",fg="white").grid(row=15, column=2,sticky='W')
Label(root, textvariable=a5, relief='raised',bg="pale goldenrod").grid(row=15, column=1, columnspan=1, sticky='WE')


Label(root, text='Ilosc poliolu:',font=("Helvetica",9,"bold"),bg="gray14",fg="white").grid(row=16, column=0, sticky='E')
Label(root, text='[g]',bg="gray14",fg="white").grid(row=16, column=2,sticky='W')
Label(root, textvariable=a6, relief='raised',bg="pale goldenrod").grid(row=16, column=1, columnspan=1, sticky='WE')


Label(root, text='Ilosc izocyjanianu:',font=("Helvetica",9,"bold"),bg="gray14",fg="white").grid(row=17, column=0, sticky='E')
Label(root, text='[g]',bg="gray14",fg="white").grid(row=17, column=2,sticky='W')
Label(root, textvariable=a7, relief='raised',bg="pale goldenrod").grid(row=17, column=1, columnspan=1, sticky='WE')

#==================================================================================================

root.mainloop()



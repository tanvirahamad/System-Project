from tkinter import *

def print_something():
    help = Tk()
    help.title("Help")
    help.geometry("600x500")
    labl = Label(help, text='Help page', )
    labl.pack()
    help.mainloop()

def lol():
    About=Tk()
    About.title("About")
    About.geometry("600x500")
    labl = Label(help, text='About page',)
    labl.pack()
    About.mainloop()


def t():
    exit()

win =Tk()

Menuu=Menu(win)
win.config(menu=Menuu)

sub_menu1=Menu(Menuu,tearoff=0)
Menuu.add_cascade(label="Help",menu=sub_menu1)
sub_menu1.add_command(label="Help",command=print_something)
sub_menu1.add_command(label="About",command=lol)



sub_menu2=Menu(Menuu,tearoff=0)
Menuu.add_cascade(label="Exit",menu=sub_menu2)
sub_menu2.add_command(label="Exit",command=t)

win.mainloop()
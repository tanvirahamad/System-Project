import tkinter as *
from PIL import ImageTk, Image

HEIGHT = 500
WIDTH = 600


root = Tk()

canvas = Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

img = ImageTk.PhotoImage(Image.open("landscape.jpg"))

#background_image = tk.PhotoImage(file='C:/Users/tanvir/PycharmProjects/a_plus/landscape.jpg')
background_label = Label(root, image=img)
background_label.place(relwidth=1, relheight=1)

menu = Menu(root)
root.config(menu=menu)

def exitt():
    exitt()

subm1=Menu(menu)
menu.add_cascade(lable="help", menu=subm1)
subm1.add_command(lable="exit", command=exitt)

subm1=Menu(menu)
menu.add_cascade(lable="help", menu=subm1)
subm1.add_command(lable="exit", command=exitt)

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.06, relwidth=0.75, relheight=0.08, anchor='n')


global tkvar
tkvar = tk.StringVar()
global tkvar1
tkvar1 = tk.StringVar()
choice = {'Bangladesh', 'Tajmahal', 'UNREAL', 'BCB', 'KUET'}
tkvar.set('Chose an topic')
choice1 = {'5', '10', '15', '20'}
tkvar1.set('Chose mark')
popupMenu = tk.OptionMenu(frame, tkvar, *choice)
popupMenu.place(relwidth=0.35, relheight=1)


popupMenu1 = tk.OptionMenu(frame, tkvar1, *choice1)
popupMenu1.place(relx=0.4, relwidth=0.35, relheight=1)


#entry = tk.Entry(frame, font=40)
#entry.place(relwidth=0.35, relheight=1)

#entry2 = tk.Entry(frame, font=40)
#entry2.place(relx=0.4, relwidth=0.35, relheight=1)

button = tk.roundedbutton(frame, text="Submit", font=40)
button["bg"] = "red"
button["border"] = "0"
button.place(relx=0.8, relheight=1, relwidth=0.2)



mid_frame = tk.Frame(root, bg='#80c1ff', bd=5)
mid_frame.place(relx=0.5, rely=0.19, relwidth=0.75, relheight=0.07, anchor='n')

label = tk.Label(mid_frame)
label.place(relwidth=1, relheight=1)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.32, relwidth=0.75, relheight=0.6, anchor='n')

label1 = tk.Label(lower_frame)
label1.place(relwidth=1, relheight=1)

root.mainloop()
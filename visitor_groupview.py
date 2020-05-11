from tkinter import *

win = Tk()
win.title("Testing")
win.geometry('{}x{}'.format(800, 450))
canvas = Canvas(win, bg = "white")
canvas.pack(expand = TRUE, fill = BOTH)
banner = Label(canvas, bg = "black", height = 4, width = 600)
banner.place(x = 0, y= 0)

usersBanner = Label(canvas, bg = "black", height = 20, width = 30)
usersBanner.place(x = 30, y = 120)
groupBanner = Label(canvas, bg = "black", height = 20, width = 70)
groupBanner.place(x = 280, y = 120)

user1 = Button(canvas, text = "user1", height = 2, width = 15)
user2 = Button(canvas, text = "user2", height = 2, width = 15)
user3 = Button(canvas, text = "user3", height = 2, width = 15)
user1.place(x = 80, y = 200)
user2.place(x = 80, y = 250)
user3.place(x = 80, y = 300)

user1 = Button(canvas, text = "project1", height = 2, width = 50)
user2 = Button(canvas, text = "project2", height = 2, width = 50)
user3 = Button(canvas, text = "project3", height = 2, width = 50)
user1.place(x = 350, y = 200)
user2.place(x = 350, y = 250)
user3.place(x = 350, y = 300)

back = PhotoImage(file = r"images/back.png")
backButton = Button(canvas, image = back, bd = 0, bg = "black")
backButton.place(x = 20, y = 20)


win.mainloop()

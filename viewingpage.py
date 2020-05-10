from tkinter import*
import visitor

class viewPage:
    def __init__(self):

        self.win = Tk()
        self.win.title("Top OU Profile")
        self.win.geometry('{}x{}'.format(1000, 600))
        self.canvas = Canvas(self.win, bg='white')
        self.profPic = PhotoImage(file = r"images/profile.png")
        self.icon = Label(self.canvas, image = self.profPic, bg = 'white')
        self.banner = Label(self.canvas, bg = "black", height = 4, width = 600)
        self.username = Label(self.canvas, text = "Username \nReputation Score:",
                            font="Arial 20 bold", bg = 'white')
        # place holder for top 3 projects
        self.project1 = Button(self.canvas, text="Project 1", font='Arial 20 bold', bg='white',
                                fg="black", width = 30, height = 2)
        self.project2 = Button(self.canvas, text="Project 2", font='Arial 20 bold', bg='white',
                                fg="black", width = 30, height = 2)
        self.project3 = Button(self.canvas, text="Project 3", font='Arial 20 bold', bg='white',
                                fg="black", width = 30, height = 2)
        self.back = PhotoImage(file = r"images/back.png")
        self.backButton = Button(self.canvas, image = self.back, command = self.visitor,
                                bd = 0, bg = "black")

    def main(self):
        self.canvas.pack(expand=TRUE, fill=BOTH)
        self.banner.place(x = 0, y= 0)
        self.icon.place(x = 50, y = 100)
        self.username.place(x = 50, y = 380)
        self.project1.place(x = 380, y = 150)
        self.project2.place(x = 380, y = 250)
        self.project3.place(x = 380, y = 350)
        self.backButton.place(x = 20, y = 20)

        self.win.mainloop()

    def visitor(self):
        self.win.destroy()
        back = visitor.VisitorPage()
        back.main()

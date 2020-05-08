from tkinter import *
import welcome


class VisitorPage:

    def __init__(self):
        self.win = Tk()
        self.win.title("The Hive - Visitor Page")
        self.win.geometry('{}x{}'.format(800, 450))
        self.canvas = Canvas(self.win, bg='#454b54')

        # self.pageTitle = Label(self.canvas, text="Visitor Page", bg="#454b54", fg="#f7cc35",
        #                        font="Arial 20 bold")
        self.welButton = Button(self.canvas, text="Login/Register", font='Arial 20 bold', bg='#454b54',
                                fg="#f7cc35", command=self.welcome)
        # place holder for top 3 projects
        self.project1 = Button(self.canvas, text="Project 1", font='Arial 20 bold', bg='white',
                                fg="black")
        self.project2 = Button(self.canvas, text="Project 2", font='Arial 20 bold', bg='white',
                                fg="black")
        self.project3 = Button(self.canvas, text="Project 3", font='Arial 20 bold', bg='white',
                                fg="black")
        # place holder for top 3 users
        self.user1 = Button(self.canvas, text="User 1", font='Arial 20 bold', bg='white',
                                fg="black")
        self.user2 = Button(self.canvas, text="User 2", font='Arial 20 bold', bg='white',
                                fg="black")
        self.user3 = Button(self.canvas, text="User 3", font='Arial 20 bold', bg='white',
                                fg="black")


    def main(self):
        self.canvas.pack(expand=TRUE, fill=BOTH)
        # self.pageTitle.pack(expand=TRUE)
        self.welButton.place(x = 300, y = 50)
        self.project1.place(x = 100, y = 225)
        self.project2.place(x = 300, y = 225)
        self.project3.place(x = 500, y = 225)

        self.user1.place(x = 100, y = 325)
        self.user2.place(x = 300, y = 325)
        self.user3.place(x = 500, y = 325)

        self.win.mainloop()

    def welcome(self):
        self.win.destroy()
        wel = welcome.WelcomeWindow()
        wel.main()


if __name__ == "__main__":
    x = VisitorPage()
    x.main()

from tkinter import *
import welcome


class VisitorPage:

    def __init__(self):
        self.win = Tk()
        self.win.title("The Hive")
        self.win.geometry('{}x{}'.format(800, 450))
        self.canvas = Canvas(self.win, bg='#454b54')

        self.pageTitle = Label(self.canvas, text="Visitor Page", bg="#454b54", fg="#f7cc35",
                               font="Arial 20 bold")
        self.welButton = Button(self.canvas, text="Login/Register", font='Arial 20 bold', bg='#454b54',
                                fg="#f7cc35", command=self.welcome)

    def main(self):
        self.canvas.pack(expand=TRUE, fill=BOTH)
        self.pageTitle.pack(expand=TRUE)
        self.welButton.pack(expand=TRUE, anchor=N)
        self.win.mainloop()

    def welcome(self):
        self.win.destroy()
        wel = welcome.WelcomeWindow()
        wel.main()


if __name__ == "__main__":
    x = VisitorPage()
    x.main()

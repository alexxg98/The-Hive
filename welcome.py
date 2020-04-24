from tkinter import *
import login
import register


class WelcomeWindow:

    def __init__(self):
        self.win = Tk()
        self.win.title("The Hive")
        self.win.geometry('{}x{}'.format(800, 450))
        self.canvas = Canvas(self.win, bg='#454b54')

        self.img = PhotoImage(file='images/icon.png')
        self.icon = Label(self.canvas, image=self.img, bg='#454b54')

        self.pageTitle = Label(self.canvas, text="Welcome to The Hive", bg='#454b54',
                               font="Arial 20 bold", fg='#f7cc35')

        self.logButton = Button(self.canvas, text="Login", font='Arial 20 bold',
                                bg='#454b54', fg='#f7cc35', command=self.login)
        self.regButton = Button(self.canvas, text="Register", font='Arial 20 bold',
                                bg='#454b54', fg='#f7cc35', command=self.register)

    def main(self):
        self.canvas.pack(expand=TRUE, fill=BOTH)
        self.icon.pack(expand=TRUE)
        self.pageTitle.pack(expand=TRUE)
        self.logButton.pack(expand=TRUE)
        self.regButton.pack(expand=TRUE)
        self.win.mainloop()

    def login(self):
        self.win.destroy()
        log = login.LoginWindow()
        log.main()

    def register(self):
        self.win.destroy()
        reg = register.RegisterWindow()
        reg.main()

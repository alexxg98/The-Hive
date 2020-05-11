from tkinter import *
import login
import register


class WelcomeWindow:

    def __init__(self):
        self.win = Tk()
        self.win.title("The Hive")
        self.win.geometry('{}x{}'.format(800, 450))
        self.canvas = Canvas(self.win, bg='#36393F')
        self.frame = Frame(self.canvas, bg='#36393F')
        self.img = PhotoImage(file='images/icon.png')
        self.icon = Label(self.frame, image=self.img, bg='#36393F')

        self.logButton = Button(self.frame, text="Login", font='Arial 20 bold',
                                bg='#454b54', fg='#f7cc35', command=self.login)
        self.regButton = Button(self.frame, text="Register", font='Arial 20 bold',
                                bg='#454b54', fg='#f7cc35', command=self.register)

    def main(self):
        self.canvas.pack(expand=TRUE, fill=BOTH)
        self.frame.pack(expand=TRUE)
        self.logButton.grid(row=0, column=0)
        self.icon.grid(row=1, column=1)
        self.regButton.grid(row=0, column=2)
        Label(self.frame, text="The Hive", bg='#36393F',
              font="Arial 20 bold", fg='#f7cc35').grid(row=2, column=1)
        self.win.mainloop()

    def login(self):
        self.win.destroy()
        log = login.LoginWindow()
        log.main()

    def register(self):
        self.win.destroy()
        reg = register.RegisterWindow()
        reg.main()

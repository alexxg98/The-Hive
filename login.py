from tkinter import *
from tkinter import messagebox
import dashboard


class LoginWindow:

    def __init__(self):
        self.win = Tk()
        # reset the window and background color
        self.canvas = Canvas(self.win, width=600, height=500, bg='white')
        self.canvas.pack(expand=YES, fill=BOTH)

        # show window in center of the screen
        width = self.win.winfo_screenwidth()
        height = self.win.winfo_screenheight()
        x = int(width / 2 - 600 / 2)
        y = int(height / 2 - 500 / 2)
        str1 = "600x500+" + str(x) + "+" + str(y)
        self.win.geometry(str1)

        # disable resize of the window
        self.win.resizable(width=False, height=False)

        # change the title of the window
        self.win.title("Login")

    def add_frame(self):
        self.frame = Frame(self.win, height=400, width=450)
        self.frame.place(x=80, y=50)
        self.label = Label(self.frame)
        self.label.place(x = 150, y = 20)

        #now create a login form
        self.label = Label(self.frame, text="User Login")
        self.label.config(font=("Courier", 20, 'bold'))
        self.label.place(x=140, y = 170)

        self.emlabel = Label(self.frame, text="Enter Email")
        self.emlabel.config(font=("Courier", 12, 'bold'))
        self.emlabel.place(x=50, y= 250)

        self.email = Entry(self.frame, font='Courier 12')
        self.email.place(x=200, y= 250)

        self.pslabel = Label(self.frame, text="Enter Password")
        self.pslabel.config(font=("Courier", 12, 'bold'))
        self.pslabel.place(x = 50, y = 280)

        self.password = Entry(self.frame,show='*', font='Courier 12')
        self.password.place(x = 200, y = 280)

        self.button = Button(self.frame, text="Login", font='Courier 15 bold',
                             command=self.login)
        self.button.place(x = 170, y = 310)

        self.win.mainloop()





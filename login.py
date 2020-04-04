from tkinter import *
import profile
import welcome


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
        # now create a login form
        self.label = Label(text="The Hive")
        self.label.config(font=("Courier", 20, 'bold'))
        self.label.place(x=140, y=170)

        self.emlabel = Label(text="Enter Username")
        self.emlabel.config(font=("Courier", 12, 'bold'))
        self.emlabel.place(x=50, y=250)

        self.email = Entry(font='Courier 12')
        self.email.place(x=200, y=250)

        self.pslabel = Label(text="Enter Password")
        self.pslabel.config(font=("Courier", 12, 'bold'))
        self.pslabel.place(x=50, y=280)

        self.password = Entry(show='*', font='Courier 12')
        self.password.place(x=200, y=280)

        self.button = Button(text="Login", font=('helvetica', 20),
                             bg='dark green', fg='white', command=self.profile)
        self.button.place(x=170, y=310)

        self.button = Button(text="Back", font=('helvetica', 10),
                             bg='dark green', fg='white', command=self.welcome)
        self.button.place(x=10, y=400)

        self.win.mainloop()

    def profile(self):
        self.win.destroy()
        prof = profile.ProfileWindow()
        prof.add_frame()

    def welcome(self):
        self.win.destroy()
        wel = welcome.WelcomeWindow()
        wel.add_frame()

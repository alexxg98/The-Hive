from tkinter import *

import profile
import welcome


class RegisterWindow:

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
        self.win.title("Register")

    def add_frame(self):


        self.label = Label(text="The Hive")
        self.label.config(font=("Courier", 18, 'bold'))
        self.label.place(x=50, y=100)

        self.namelabel = Label(text="Enter Name")
        self.namelabel.config(font=("Courier", 12, 'bold'))
        self.namelabel.place(x=50, y=150)

        self.name = Entry(font='Courier 12')
        self.name.place(x=200, y=150)

        self.emlabel = Label(text="Enter Email")
        self.emlabel.config(font=("Courier", 12, 'bold'))
        self.emlabel.place(x=50, y=180)

        self.email = Entry(font='Courier 12')
        self.email.place(x=200, y=180)

        self.interestlabel = Label(text="Enter Interest")
        self.interestlabel.config(font=("Courier", 12, 'bold'))
        self.interestlabel.place(x=50, y=210)

        self.interest = Entry(font='Courier 12')
        self.interest.place(x=200, y=210)

        self.credlabel = Label(text="Enter Credentials")
        self.credlabel.config(font=("Courier", 12, 'bold'))
        self.credlabel.place(x=50, y=240)

        self.credentials = Entry(font='Courier 12')
        self.credentials.place(x=230, y=240)

        self.reflabel = Label(text="Enter Reference")
        self.reflabel.config(font=("Courier", 12, 'bold'))
        self.reflabel.place(x=50, y=270)

        self.reference = Entry(font='Courier 12')
        self.reference.place(x=230, y=270)



        self.button = Button(text="Register", font=('Courier Bold', 30),
                             bg='dark green', fg='white', command=self.profile)
        self.button.place(x=170, y=400)

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

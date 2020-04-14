from tkinter import *
from tkinter import messagebox

import su
import welcome
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="alfheim",
    database="TheHive"
)

cursor = db.cursor()


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

    def main(self):
        self.label = Label(text="The Hive")
        self.label.config(font=("Courier", 20, 'bold'))
        self.label.place(x=140, y=170)

        self.unlabel = Label(text="Enter Username")
        self.unlabel.config(font=("Courier", 12, 'bold'))
        self.unlabel.place(x=50, y=250)

        self.username = Entry(font='Courier 12')
        self.username.place(x=200, y=250)

        self.pslabel = Label(text="Enter Password")
        self.pslabel.config(font=("Courier", 12, 'bold'))
        self.pslabel.place(x=50, y=280)

        self.password = Entry(show='*', font='Courier 12')
        self.password.place(x=200, y=280)

        self.button = Button(text="Login", font=('helvetica', 20), bg='dark green', fg='white', command=self.log_btn())
        self.button.place(x=170, y=310)

        self.button = Button(text="Back", font=('helvetica', 10), bg='dark green', fg='white', command=self.welcome)
        self.button.place(x=10, y=400)

        self.win.mainloop()

    def log_btn(self):
        username = self.username.get()
        password = self.password.get()

        cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s',
                       (username, password))
        account = cursor.fetchone()

        if username == "" or password == "":
            messagebox.showinfo("Login Status", "All Fields are Required")
        elif account:
            self.su()
        else:
            messagebox.showerror("Error", "Account does not exist!")

    def su(self):
        self.win.destroy()
        super = su.main()
        super.main()

    def welcome(self):
        self.win.destroy()
        wel = welcome.WelcomeWindow()
        wel.main()

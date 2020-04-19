from tkinter import *
from tkinter import messagebox

import su
import welcome
import mysql.connector

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="cscD@t@Bas3",
    database="thehive"
)

cursor = db.cursor()


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

    def main(self):
        self.label = Label(text="The Hive")
        self.label.config(font=("Courier", 18, 'bold'))
        self.label.place(x=50, y=170)

        self.emlabel = Label(text="Enter Email")
        self.emlabel.config(font=("Courier", 12, 'bold'))
        self.emlabel.place(x=50, y=250)

        self.email = Entry(font='Courier 12')
        self.email.place(x=200, y=250)

        self.unlabel = Label(text="Enter Username")
        self.unlabel.config(font=("Courier", 12, 'bold'))
        self.unlabel.place(x=50, y=280)

        self.username = Entry(font='Courier 12')
        self.username.place(x=200, y=280)

        self.pslabel = Label(text="Enter Password")
        self.pslabel.config(font=("Courier", 12, 'bold'))
        self.pslabel.place(x=50, y=310)

        self.password = Entry(show='*', font='Courier 12')
        self.password.place(x=200, y=310)

        self.reflabel = Label(text="Enter Reference")
        self.reflabel.config(font=("Courier", 12, 'bold'))
        self.reflabel.place(x=50, y=340)

        self.reference = Entry(font='Courier 12')
        self.reference.place(x=200, y=340)

        self.button = Button(text="Register", font=('Courier Bold', 30), bg='dark green', fg='white',
                             command=self.reg_btn)
        self.button.place(x=170, y=400)

        self.button = Button(text="Back", font=('helvetica', 10), bg='dark green', fg='white', command=self.welcome)
        self.button.place(x=10, y=400)

        self.win.mainloop()

    def reg_btn(self):
        email = self.email.get()
        username = self.username.get()
        password = self.password.get()
        try:
            if username == "" or email == "" or password == "":
                messagebox.showinfo("Registration Status", "All Fields are Required")
            else:
                cursor.execute("INSERT INTO users (email, username, password) VALUES (%s, %s, %s)",
                               (email, username, password))
                db.commit()
                self.su()
        except mysql.connector.errors.IntegrityError:
            messagebox.showerror("Error", "Account already exists!")

    def su(self):
        self.win.destroy()
        super = su.main()
        super.main()

    def welcome(self):
        self.win.destroy()
        wel = welcome.WelcomeWindow()
        wel.main()

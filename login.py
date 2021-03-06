from tkinter import *
from tkinter import messagebox
import ou
import vip
import su
import welcome
import db
import changePassword

class LoginWindow:

    def __init__(self):
        self.win = Tk()
        self.win.title("The Hive")
        self.win.geometry('{}x{}'.format(800, 450))
        self.canvas = Canvas(self.win, bg='#454b54')

        self.userLabel = Label(self.canvas, text="Enter Username", font='Arial 20 bold', bg='#454b54',
                               fg='#f7cc35')
        self.username = Entry(self.canvas, font='Arial 20 bold', bg='white')

        self.passLabel = Label(self.canvas, text="Enter Password", font='Arial 20 bold', bg='#454b54',
                               fg='#f7cc35')
        self.password = Entry(self.canvas, show='*', font='Arial 20 bold', bg='white')

        self.forgotPassButton = Button(self.canvas, text="Forgot Password", font='Arial 15 bold', bg='#454b54',
                                 fg='#f7cc35', command=self.forgotPass)

        self.backButton = Button(self.canvas, text="Back", font='Arial 15 bold', bg='#454b54',
                                 fg='#f7cc35', command=self.welcome)
        self.logButton = Button(self.canvas, text="Login", font='Arial 15 bold', bg='#454b54', fg='#f7cc35',
                                command=self.log_btn)

    def main(self):
        self.canvas.pack(expand=TRUE, fill=BOTH)
        self.userLabel.pack(expand=TRUE)
        self.username.pack(expand=TRUE)

        self.passLabel.pack(expand=TRUE)
        self.password.pack(expand=TRUE)

        self.forgotPassButton.pack(expand=TRUE)
        self.backButton.pack(expand=TRUE)
        self.logButton.pack(expand=TRUE)

        self.win.mainloop()

    def ou(self):
        self.win.destroy()
        ordUser = ou.main()
        ordUser.main()

    def vip(self):
        self.win.destroy()
        vipUser = vip.main()
        vipUser.main()

    def su(self):
        self.win.destroy()
        superUser = su.main()
        superUser.main()

    def welcome(self):
        self.win.destroy()
        wel = welcome.WelcomeWindow()
        wel.main()

    def changePass(self):
        self.win.destroy()
        chgPass = changePassword.ChangePassword()
        chgPass.main()

    def forgotPass(self):
        self.win.destroy()
        chgPass = changePassword.ChangePassword()
        chgPass.main()

    def log_btn(self):
        username = self.username.get()
        password = self.password.get()

        db.cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password))
        account = db.cursor.fetchone()

        if account:
            # set user status to ON and all other users to NULL
            # Keep track of which user is logged in on this device
            db.cursor.execute("UPDATE users SET status = NULL")
            db.cursor.execute("UPDATE users SET status = 'ON' where username = '%s'" % username)

            #check repScore and change if neccessary
            repScore = db.getRepScore()
            if repScore>30:
                db.cursor.execute("UPDATE users SET user_type = 'VIP' WHERE status = 'ON'")
            elif repScore <25 and repScore>0:
                db.cursor.execute("UPDATE users SET user_type = 'OU' WHERE status = 'ON'")

            #Check if first time login
            db.cursor.execute("SELECT login_time FROM users WHERE username = '%s'" % username)
            firstLogin = db.cursor.fetchone()[0]
            if firstLogin == "FIRST":
                self.changePass()
            else:
                # Direct to user page based on type
                db.cursor.execute("SELECT user_type FROM users WHERE username = '%s'" % username)
                acct_type = db.cursor.fetchone()[0]
                if acct_type == "OU":
                    self.ou()
                elif acct_type == "VIP":
                    self.vip()
                elif acct_type == "SU":
                    self.su()
        elif username == "" or password == "":
            messagebox.showwarning("Login Status", "All fields are required!")
        else:
            messagebox.showerror("Login Status", "Account does not exist!")

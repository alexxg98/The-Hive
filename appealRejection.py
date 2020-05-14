from tkinter import *
from tkinter import messagebox
import db
import welcome


class AppealRejection:

    def __init__(self):
        self.win = Tk()
        self.win.title("The Hive")
        self.win.geometry('{}x{}'.format(800, 450))
        self.canvas = Canvas(self.win, bg='#454b54')

        self.emailLabel = Label(self.canvas, text="Email", font='Arial 15 bold', bg='#454b54',
                                fg='#f7cc35')
        self.email = Entry(self.canvas, font='Arial 15 bold', bg='white')

        self.appealLabel = Label(self.canvas, text="Appeal Statement", font='Arial 15 bold', bg='#454b54',
                               fg='#f7cc35')
        self.appeal = Entry(self.canvas, font='Arial 15 bold', bg='white')


        self.checkButton = Button(self.canvas, text="Check", font='Arial 15 bold', bg='#454b54',
                                 fg='#f7cc35', command=self.check_btn)

        self.backButton = Button(self.canvas, text="Back", font='Arial 15 bold', bg='#454b54',
                                 fg='#f7cc35', command=self.welcome)
        self.appealButton = Button(self.canvas, text="Appeal", font='Arial 15 bold', bg='#454b54', fg='#f7cc35',
                                command=self.appeal_btn)

    def main(self):
        self.canvas.pack(expand=TRUE, fill=BOTH)
        self.emailLabel.pack(expand=TRUE)
        self.email.pack(expand=TRUE)
        self.checkButton.pack(expand=TRUE)
        self.appealLabel.pack(expand=TRUE)
        self.appeal.pack(expand=TRUE)
        self.backButton.pack(expand=TRUE)
        self.appealButton.pack(expand=TRUE)
        self.win.mainloop()

    def appeal_btn(self):
        email = self.email.get()
        appeal = self.appeal.get()

        messagebox.showinfo("Registration Status", "Thank You! A SuperUser will review your appeal "
                                                   "and if approved, an email will be sent to you with "
                                                   "your login details.")
        db.cursor.execute('UPDATE pending_users SET APPEAL = %s WHERE email = %s', (appeal, email))
        self.welcome()

    def check_btn(self):
        email = self.email.get()

        db.cursor.execute('SELECT * FROM pending_users WHERE email = %s ', (email,))
        pending = db.cursor.fetchone()

        db.cursor.execute("SELECT * FROM black_list WHERE blacklisted = %s", (email,))
        blacklisted = db.cursor.fetchone()

        if pending:
            db.cursor.execute("SELECT rejected FROM pending_users WHERE email = %s", (email,))
            rejNum = db.cursor.fetchone()[0]

            if rejNum == 0:
                messagebox.showinfo("Registration Status", "Your application has not been reviewed yet. Please be patient.")
            elif rejNum == 1:
                messagebox.showinfo("Registration Status", "Your application has been rejected. You have one chance to appeal. If desired, enter appeal statement.")
        elif blacklisted:
            messagebox.showinfo("Registration Status", "Sorry, your application was rejected twice. You have been placed in our blacklist.")
        else:
            messagebox.showinfo("Registration Status", "No application found for entered email.")


    def welcome(self):
        self.win.destroy()
        wel = welcome.WelcomeWindow()
        wel.main()

import string
import random
from tkinter import *
import smtplib
from email.message import EmailMessage
from tkinter.ttk import Treeview

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="TheHive"
)

cursor = db.cursor()

#function to send email to pending users
#subject & content changes depending on acceptance of user
def send_email(subject, content, receiver):
    sender = "thehiveof4men@gmail.com"
    password = "thehive111"

    message = EmailMessage()
    message['Subject'] = subject
    message['From'] = sender
    message['To'] = receiver
    message.set_content(content)
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, receiver, message.as_string())
    server.quit()

def generate_username(name):
    letters = name[0] + " ".join(name.split()[1:2])
    number = random.randint(100, 999)
    username = letters + str(number)
    return username.lower()

class PendingUser:

    def __init__(self):
        self.win = Tk()
        self.win.title("The Hive")
        self.win.geometry('{}x{}'.format(800, 450))
        self.canvas = Canvas(self.win, bg='#454b54')
        self.acceptButton = Button(self.canvas, text="Accept", font='Arial 15 bold', bg='#454b54',
                                   fg="#f7cc35", command=self.accept)
        self.rejectButton = Button(self.canvas, text="Reject", font='Arial 15 bold', bg='#454b54',
                                   fg="#f7cc35", command=self.reject)
        self.list = Treeview(self.canvas, columns=(1, 2, 3, 4, 5, 6), show="headings", height="15")

    def main(self):
        self.canvas.pack(expand=TRUE, fill=BOTH)

        self.list.pack()
        self.list.heading(1, text="ID")
        self.list.column(1, width=20)
        self.list.heading(2, text="Name")
        self.list.column(2, width=100)
        self.list.heading(3, text="Email")
        self.list.column(3, width=200)
        self.list.heading(4, text="Reference")
        self.list.column(4, width=100)
        self.list.heading(5, text="Interest")
        self.list.column(5, width=100)
        self.list.heading(6, text="Credential")
        self.list.column(6, width=100)
        
        #inserts entries from pending_users database table to list 
        cursor.execute('SELECT * FROM pending_users')
        records = cursor.fetchall()
        for row in records:
            self.list.insert('', END, values=row)

        self.acceptButton.pack(expand=TRUE, side=LEFT)
        self.rejectButton.pack(expand=TRUE, side=LEFT)

        self.win.mainloop()
    
    #this funtion is invoked when clicking on accept button on selected item
    def accept(self):
        #generates random password
        password = ''.join(random.choice(string.ascii_lowercase) for i in range(6))
        
        #takes the email and name from selected item
        # a, b, c, d, e, f represents the columns in TreeView List (ID, name, email, etc..)
        for selected_item in self.list.selection():
            a, b, c, d, e, f = self.list.item(selected_item, 'values')
            email = c
            username = generate_username(b)
        
        #selected item is deleted from list
        for selected_item in self.list.selection():
            self.list.delete(selected_item)
        
        #accepted applicant is added to users database table
        cursor.execute('INSERT INTO users (email, username, password, user_type) VALUES (%s, %s, %s, "OU")',
                       (email, username, password))
        db.commit()
        
        #accepted applicant is deleted from pending_users database table
        cursor.execute("DELETE FROM pending_users WHERE email = %s", (email,))
        db.commit()
        
        #email is sent to applicant with generated username + password
        subject = "Application Accepted!"
        content = '''\
            Congratz! Please change your password once you log in with the following credentials. \n
            Username: {username} \n
            Password: {password} \
            '''.format(username=username, password=password)
        send_email(subject, content, email)

    #function is called when clicking reject button on selected item
    def reject(self):
        #select email from selected item from list
        for selected_item in self.list.selection():
            a, b, c, d, e, f = self.list.item(selected_item, 'values')
            email = c
        
        #delete selected item from list
        for selected_item in self.list.selection():
            self.list.delete(selected_item)
        
        #delete item from pending_users table
        cursor.execute("DELETE FROM pending_users WHERE email = %s", (email,))
        db.commit()
        
        subject = "Application Denied"
        content = '''\
            Sorry, but your application has been denied. \n
            You have one chance to appeal and the SU will make a final decision to \n 
            reverse the rejection. If you receive another rejection, then you \n
            will be put in blacklist forever.  \
            '''
        send_email(subject, content, email)


if __name__ == "__main__":
    x = PendingUser()
    x.main()

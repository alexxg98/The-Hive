import os
from tkinter import *
from tkinter.ttk import Combobox
from prettytable import PrettyTable
import db

def inputUsers():
    db.cursor.execute("SELECT username FROM users WHERE user_type = 'VIP' AND status IS NULL")
    data = ["-Select VIP User-"]
    for row in db.cursor.fetchall():
        data.append(row[0])
    return data
class VotingPage:

    def __init__(self):
        self.win = Tk()
        self.win.title("Voting ")
        self.win.geometry('{}x{}'.format(800, 450))
        self.canvas = Canvas(self.win, bg='#454b54')
        self.frame = Frame(self.canvas, bg='#454b54', width=600, height=340)

        headerFormat = ["Your Name","Reason","SU Candidate"]
        self.table = PrettyTable(headerFormat)

        self.VIPlist = StringVar()

        self.votepage = Text(self.frame, width=80, height=15)

        self.selectVIP = Combobox(self.frame, width=15, textvariable=self.VIPlist, state="readonly")
        self.selectVIP['values'] = inputUsers()

        self.vote = Button(self.frame, text="Vote", command=self.add)
        self.view = Button(self.frame, text="View Votes", command=self.printVotes)

    def main(self):
        self.canvas.pack(expand=TRUE, fill=BOTH)
        self.frame.pack(expand=TRUE)
        Label(self.frame, text="Select a VIP to be promoted to SU", bg="#454b54", fg="#f7cc35",
              font="Arial 10 bold").grid(row=0, column=0, columnspan=4)

        self.selectVIP.grid(row=1, column=2)
        self.selectVIP.current(0)

        self.votepage.grid(row=2, columnspan=4, pady=10)
        self.vote.grid(row=3, column=0)
        self.view.grid(row=3, column=2)

        self.win.mainloop()

    def add(self):
        vipChoice = self.VIPlist.get()
        db.cursor.execute("SELECT votes FROM users WHERE username = '%s'"%vipChoice)
        incVote = db.cursor.fetchone()[0]
        incVote += 1
        db.cursor.execute("UPDATE users SET votes = %s WHERE username = %s",(incVote, vipChoice))

    def printVotes(self):
        self.table.clear_rows()

        db.cursor.execute("SELECT username FROM users WHERE user_type = 'VIP'")
        data = []
        for row in db.cursor.fetchall():
            data.append(row[0])

        for user in data:
            db.cursor.execute("SELECT votes FROM users WHERE username = '%s'"%user)
            numVote = db.cursor.fetchone()[0]
            display = user + ": " + str(numVote) + "\n\n"
            self.votepage.insert(INSERT,display)
            self.votepage.see(INSERT)

if __name__ == "__main__":
    x = VotingPage()
    x.main()

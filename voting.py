import os
from tkinter import *
from tkinter.ttk import Combobox
from prettytable import PrettyTable
import db

def inputUsers():
    db.cursor.execute("SELECT username FROM users WHERE user_type = 'VIP'")
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

        self.name = StringVar()
        self.reason = StringVar()
        self.VIPlist = StringVar()

        self.votepage = Text(self.frame, width=80, height=15)

        self.selectVIP = Combobox(self.frame, width=15, textvariable=self.VIPlist, state="readonly")
        self.selectVIP['values'] = inputUsers()

        self.vote = Button(self.frame, text="Vote", command=self.add)
        self.view = Button(self.frame, text="View Votes", command=self.printVotes)
        self.delete = Button(self.frame, text="Clear Votes", command=self.deleteAll)
        self.nameEntry = Entry(self.frame, width=15, textvariable=self.name)
        self.reasonEntry = Entry(self.frame, width=15, textvariable=self.reason)

    def main(self):
        self.canvas.pack(expand=TRUE, fill=BOTH)
        self.frame.pack(expand=TRUE)
        Label(self.frame, text="Select a VIP to be promoted to SU", bg="#454b54", fg="#f7cc35",
              font="Arial 10 bold").grid(row=0, column=0, columnspan=4)

        self.nameEntry.grid(row=1, column=0)
        self.nameEntry.insert(0, '-Your Name-')
        self.reasonEntry.grid(row=1, column=1)
        self.reasonEntry.insert(0, '-Reason-')

        self.selectVIP.grid(row=1, column=2)
        self.selectVIP.current(0)

        self.votepage.grid(row=2, columnspan=4, pady=10)
        self.vote.grid(row=3, column=0)
        self.view.grid(row=3, column=2)
        self.delete.grid(row=3, column=3)

        self.win.mainloop()
        
    def add(self):
        self.table.add_row([self.name.get(), self.reason.get(), self.VIPlist.get()])
        open("text.txt", "w").close()
        file_new = open("text.txt", "a")
        file_new.write(str(self.table) + '\n')
        file_new.close()

    def printVotes(self):
        self.votepage.delete(1.0, END)
        if os.stat("text.txt").st_size == 0:
            self.votepage.insert(INSERT, "Invalid Fields")
        else:
            with open("text.txt", "r") as file_new:
                contents = file_new.read()
                self.votepage.insert(INSERT, contents)
                self.votepage.see(INSERT)

    def deleteAll(self):
        self.votepage.delete(1.0, END)
        file = open("text.txt", "w+")
        file.truncate(0)
        file.close()


if __name__ == "__main__":
    x = VotingPage()
    x.main()

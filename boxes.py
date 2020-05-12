from tkinter import *
from tkinter.ttk import Treeview, Combobox
import db


def inputUsers():
    db.cursor.execute('SELECT username FROM users')
    data = ["-Select User to Add-"]
    for row in db.cursor.fetchall():
        data.append(row[0])
    return data


class BlackWhite:

    def __init__(self):
        self.win = Tk()
        self.win.title("White/Black List")
        self.win.geometry('{}x{}'.format(800, 450))
        self.canvas = Canvas(self.win, bg='#36393F')
        self.frame = Frame(self.canvas, bg='#36393F', width=600, height=340)
        self.userSelected = StringVar()
        self.whitebox = Treeview(self.frame, columns=1, show="headings", height="5")
        self.blackbox = Treeview(self.frame, columns=1, show="headings", height="5")
        self.userList = Combobox(self.frame, width=20, textvariable=self.userSelected, state="readonly")
        self.user = db.getName()

    def main(self):
        self.canvas.pack(expand=TRUE, fill=BOTH)
        self.frame.pack(expand=TRUE)

        Button(self.frame, text="Add", font='Arial 10 bold', bg='#36393F',
               fg="#f7cc35", command=self.addWhite).grid(row=0, column=0)
        Button(self.frame, text="Remove", font='Arial 10 bold', bg='#36393F',
               fg="#f7cc35", command=self.removeWhite).grid(row=1, column=0, padx=10)

        self.whitebox.grid(row=0, column=1, rowspan=2)
        self.whitebox.heading(1, text="WhiteBox")
        self.whitebox.column(1, width=100)

        self.blackbox.grid(row=0, column=2, rowspan=2)
        self.blackbox.heading(1, text="BlackBox")
        self.blackbox.column(1, width=100)

        Button(self.frame, text="Add", font='Arial 10 bold', bg='#36393F',
               fg="#f7cc35", command=self.addBlack).grid(row=0, column=3)
        Button(self.frame, text="Remove", font='Arial 10 bold', bg='#36393F',
               fg="#f7cc35", command=self.removeBlack).grid(row=1, column=3, padx=10)

        db.cursor.execute("SELECT whitelisted FROM white_list WHERE whitelister = '%s'" % self.user)
        for row in db.cursor.fetchall():
            self.whitebox.insert('', END, values=row)

        db.cursor.execute("SELECT blacklisted FROM black_list WHERE blacklister = '%s'" % self.user)
        for row in db.cursor.fetchall():
            self.blackbox.insert('', END, values=row)

        self.userList.grid(row=2, column=0, columnspan=4, pady=10)
        self.userList['values'] = inputUsers()
        self.userList.current(0)

        self.win.mainloop()

    def addWhite(self):
        # add selected user from combobox to whitebox
        self.whitebox.insert('', END, values=self.userSelected.get())

        # add to white_list table
        db.cursor.execute("INSERT INTO white_list VALUES(%s, %s)", (self.user, self.userSelected.get()))

    def removeWhite(self):
        for selected_item in self.whitebox.selection():
            whitelisted = self.whitebox.item(selected_item, 'values')[0]
            self.whitebox.delete(selected_item)
        db.cursor.execute("DELETE FROM white_list WHERE whitelister = %s AND whitelisted = %s",
                          (self.user, whitelisted))

    def addBlack(self):
        self.blackbox.insert('', END, values=self.userSelected.get())

        db.cursor.execute("INSERT INTO black_list VALUES(%s, %s)", (self.user, self.userSelected.get()))

    def removeBlack(self):
        for selected_item in self.blackbox.selection():
            blacklisted = self.blackbox.item(selected_item, 'values')[0]
            self.blackbox.delete(selected_item)
        db.cursor.execute("DELETE FROM black_list WHERE blacklister = %s AND blacklisted = %s",
                          (self.user, blacklisted))


if __name__ == "__main__":
    x = BlackWhite()
    x.main()

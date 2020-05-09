from tkinter import *
from tkinter.ttk import Treeview
import db


class CreateGroup:

    def __init__(self):
        self.win = Tk()
        self.win.title("The Hive")
        self.win.geometry('{}x{}'.format(500, 400))
        self.canvas = Canvas(self.win, bg='#454b54')
        self.canvas.pack(expand=TRUE, fill=BOTH)
        self.frame = Frame(self.canvas, bg='#454b54', width=600, height=340)
        self.frame.pack(expand=TRUE)
        self.textBox = Text(self.frame, width=20, height=5)
        self.tree = Treeview(self.frame, columns=1, show="headings", height="7")
        self.name = StringVar()

    def main(self):
        Label(self.frame, text="Group Name:", bg="#454b54", fg="#f7cc35",
              font="Arial 10 bold").grid(row=0, column=0)
        Entry(self.frame, width=20, textvariable=self.name).grid(row=1, column=0, pady=10)

        Label(self.frame, text="Description:", bg="#454b54", fg="#f7cc35",
              font="Arial 10 bold").grid(row=2, column=0)
        self.textBox.grid(row=3, column=0, pady=10)

        self.tree.grid(row=0, column=1, rowspan=5, padx=20)
        self.tree.heading(1, text="Select User")

        Button(self.frame, text="Send Invite", command=self.invite).grid(row=5, column=1, sticky=N)
        Button(self.frame, text="Create Group", command=self.create_group).grid(row=4, column=0)

        db.cursor.execute('SELECT username FROM users')
        users = db.cursor.fetchall()
        for row in users:
            self.tree.insert('', END, values=row)

        self.win.mainloop()

    def invite(self):
        for selected_item in self.tree.selection():
            user = self.tree.item(selected_item, 'values')
            # send invitation to selected user with group details (name, description, creator)

        for selected_item in self.tree.selection():
            self.tree.delete(selected_item)

    def create_group(self):
        description = self.textBox.get("1.0", "end-1c")
        db.cursor.execute("INSERT INTO projects(name, description) VALUES( %s, %s)", (self.name.get(), description))


if __name__ == "__main__":
    x = CreateGroup()
    x.main()

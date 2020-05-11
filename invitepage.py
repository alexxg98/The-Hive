from tkinter import *
from tkinter.ttk import Treeview
import db


class InvitePage:

    def __init__(self):
        self.win = Tk()
        self.win.title("The Hive")
        self.win.geometry('{}x{}'.format(800, 450))
        self.canvas = Canvas(self.win, bg='#36393F')
        self.frame = Frame(self.canvas, bg='#36393F', width=600, height=340)
        self.acceptButton = Button(self.frame, text="Accept", font='Arial 15 bold', bg='#36393F',
                                   fg="#f7cc35", command=self.accept)
        self.declineButton = Button(self.frame, text="Decline", font='Arial 15 bold', bg='#36393F',
                                    fg="#f7cc35", command=self.decline)
        self.list = Treeview(self.frame, columns=(1, 2, 3, 4), show="headings", height="15")
        self.user = db.getName()

    def main(self):
        self.canvas.pack(expand=TRUE, fill=BOTH)
        self.frame.pack(expand=TRUE)
        self.list.pack()
        self.list.heading(1, text="From")
        self.list.column(1, width=100)
        self.list.heading(2, text="ID")
        self.list.column(2, width=20)
        self.list.heading(3, text="Group Name")
        self.list.column(3, width=100)
        self.list.heading(4, text="Description")
        self.list.column(4, width=150)

        db.cursor.execute('SELECT inviter, projects.id, projects.name, projects.description FROM invitations, '
                          'projects WHERE invitations.group_id = projects.id AND invited = %s', (self.user,))
        for row in db.cursor.fetchall():
            self.list.insert('', END, values=row)

        self.acceptButton.pack(expand=TRUE, side=LEFT)
        self.declineButton.pack(expand=TRUE, side=LEFT)

        self.win.mainloop()

    def accept(self):
        for selected_item in self.list.selection():
            inviter = self.list.item(selected_item, 'values')[0]
            groupID = self.list.item(selected_item, 'values')[1]
            self.list.delete(selected_item)

        db.cursor.execute("DELETE FROM invitations WHERE inviter = %s AND invited = %s AND group_id = %s",
                          (inviter, self.user, groupID))
        db.cursor.execute("INSERT INTO group_membership VALUES(%s, %s)", (self.user, groupID))

    def decline(self):
        for selected_item in self.list.selection():
            inviter = self.list.item(selected_item, 'values')[0]
            groupID = self.list.item(selected_item, 'values')[1]
            self.list.delete(selected_item)

        db.cursor.execute("DELETE FROM invitations WHERE inviter = %s AND invited = %s AND group_id = %s",
                          (inviter, self.user, groupID))


if __name__ == "__main__":
    x = InvitePage()
    x.main()

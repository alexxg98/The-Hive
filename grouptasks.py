import os
from tkinter import *
from tkinter.ttk import Combobox
from prettytable import PrettyTable
import db


def inputUsers():
    # get all users from current group to put into combobox for assigned users
    groupId = db.getGroupID()
    db.cursor.execute('SELECT username FROM group_membership WHERE group_id = %s', (groupId, ))
    data = ["-Assigned User-"]
    for row in db.cursor.fetchall():
        data.append(row[0])
    return data


class GroupTasks:

    def __init__(self):
        self.win = Tk()
        self.win.title("The Hive")
        self.win.geometry('{}x{}'.format(800, 450))
        self.canvas = Canvas(self.win, bg='#454b54')
        self.frame = Frame(self.canvas, bg='#454b54', width=600, height=340)

        headerFormat = ["Task", "Deadline", "Assigned User", "Status"]
        self.table = PrettyTable(headerFormat)

        self.task = StringVar()
        self.deadline = StringVar()
        self.assigned = StringVar()
        self.status = StringVar()

        self.viewBox = Text(self.frame, width=60, height=15)

        self.assignedUser = Combobox(self.frame, width=15, textvariable=self.assigned, state="readonly")
        self.assignedUser['values'] = inputUsers()

        self.statusBar = Combobox(self.frame, width=10, textvariable=self.status, state="readonly")
        self.statusBar['values'] = ("-Status-", "Pending", "Complete", "Incomplete")

        self.taskEntry = Entry(self.frame, width=20, textvariable=self.task)
        self.dateEntry = Entry(self.frame, width=10, textvariable=self.deadline)

        self.create = Button(self.frame, text="Create", command=self.add)
        self.view = Button(self.frame, text="View Schedule", command=self.printTasks)
        self.delete = Button(self.frame, text="Clear Schedule", command=self.deleteAll)

    def main(self):
        self.canvas.pack(expand=TRUE, fill=BOTH)
        self.frame.pack(expand=TRUE)
        Label(self.frame, text="Group Tasks:", bg="#454b54", fg="#f7cc35",
              font="Arial 10 bold").grid(row=0, column=0, columnspan=4)

        self.taskEntry.grid(row=1, column=0)
        self.taskEntry.insert(0, '-Task-')
        self.dateEntry.grid(row=1, column=1)
        self.dateEntry.insert(0, '-Deadline-')

        self.assignedUser.grid(row=1, column=2)
        self.statusBar.grid(row=1, column=3)
        self.assignedUser.current(0)
        self.statusBar.current(0)

        self.viewBox.grid(row=2, columnspan=4, pady=10)
        self.create.grid(row=3, column=0)
        self.view.grid(row=3, column=2)
        self.delete.grid(row=3, column=3)

        self.win.mainloop()

    def add(self):
        self.table.add_row([self.task.get(), self.deadline.get(), self.assigned.get(), self.status.get()])
        open("text.txt", "w").close()
        file_new = open("text.txt", "a")
        file_new.write(str(self.table) + '\n')
        file_new.close()

    def printTasks(self):
        self.viewBox.delete(1.0, END)
        if os.stat("text.txt").st_size == 0:
            self.viewBox.insert(INSERT, "No Event Found")
        else:
            with open("text.txt", "r") as file_new:
                contents = file_new.read()
                self.viewBox.insert(INSERT, contents)
                self.viewBox.see(INSERT)

    def deleteAll(self):
        open("text.txt", "w").close()
        self.viewBox.delete(1.0, END)


if __name__ == "__main__":
    x = GroupTasks()
    x.main()

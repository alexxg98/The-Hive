from tkinter import *
from tkinter.ttk import Treeview
import db


class Comment:

    def __init__(self):
        self.win = Tk()
        self.win.title("The Hive")
        self.win.geometry('{}x{}'.format(600, 400))
        self.canvas = Canvas(self.win, bg='#454b54')
        self.canvas.pack(expand=TRUE, fill=BOTH)
        self.frame = Frame(self.canvas, bg='#454b54', width=600, height=340)
        self.frame.pack(expand=TRUE)
        self.textBox = Text(self.frame, width=20, height=5)
        self.textBox1 = Text(self.frame, width=20, height=5)
        self.tree = Treeview(self.frame, columns=1, show="headings", height="7")
        self.name = StringVar()

    def main(self):
        Label(self.frame, text="Write a complain:", bg="#454b54", fg="#f7cc35",
              font="Arial 10 bold").grid(row=0, column=0)
        self.textBox1.grid(row=1, column=0, pady=5)
        Button(self.frame, text="Complain", bg='#2C92D6', fg='#C5A32A').grid(row=2, column=0, sticky=N)

        Label(self.frame, text="Write a Compliment:", bg="#454b54", fg="#f7cc35",
              font="Arial 10 bold").grid(row=0, column=2)
        self.textBox.grid(row=1, column=2, pady=5)
        Button(self.frame, text="Compliment", bg='#2C92D6', fg='#C5A32A').grid(row=2, column=2)

        self.tree.grid(row=0, column=1, rowspan=5, padx=20)
        self.tree.heading(1, text="Select User")

        

        db.cursor.execute("SELECT username FROM users WHERE user_type <> 'SU'")
        users = db.cursor.fetchall()
        for row in users:
            self.tree.insert('', END, values=row)

        self.win.mainloop()
        

    def create_group(self):
        description = self.textBox.get("1.0", "end-1c")
        db.cursor.execute("INSERT INTO projects(name, description) VALUES(%s, %s)", (self.name.get(), description))


if __name__ == "__main__":
    x = Comment()
    x.main()

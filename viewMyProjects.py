from tkinter import *
from tkinter.ttk import Treeview
import db
import os

class ViewProjects:

    def __init__(self):
        self.win = Tk()
        self.win.title("The Hive")
        self.win.geometry('{}x{}'.format(700, 400))
        self.canvas = Canvas(self.win, bg='#454b54')
        self.widget = Label(self.canvas, text='Select Project: ', font='Arial 15 bold',fg='white', bg='#454b54')
        self.select = Button(self.canvas, text="SELECT", font='Arial 15 bold', bg='#454b54',
                                   fg="#f7cc35", command=self.selectToOpen)
        self.list = Treeview(self.canvas, columns=(1, 2, 3), show="headings", height="15")

    def main(self):
        self.canvas.pack(expand=TRUE, fill=BOTH)
        self.widget.pack(fill=X)
        self.list.pack()
        self.list.heading(1, text="Name")
        self.list.column(1, width=100)
        self.list.heading(2, text="Description")
        self.list.column(2, width=200)
        self.list.heading(3, text="Rank")
        self.list.column(3, width=65)

        user = db.getName()
        db.cursor.execute(" SELECT name,description,projRank FROM projects A\
                            INNER JOIN group_membership B\
                            ON A.id = B.group_id\
                            WHERE B.username = %s", (user,))
        for row in db.cursor.fetchall():
            self.list.insert('', END, values=row)

        self.select.pack(expand=TRUE)
        
        self.win.mainloop()

    def selectToOpen(self):
        
        for selected_item in self.list.selection():
            group_name = self.list.item(selected_item, 'values')[0]
            
        #track which group page is being viewed at the moment
        db.cursor.execute("UPDATE projects SET viewing = NULL")
        db.cursor.execute("UPDATE projects SET viewing = 'ON' where name = '%s'" % group_name)
        os.system('python group_page.py')
        self.win.destroy()

if __name__ == "__main__":
    x = ViewProjects()
    x.main()


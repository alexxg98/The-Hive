from tkinter import *
from tkinter.ttk import Treeview
import db
import reputationScore


class Comment:

    def __init__(self):
        self.win = Tk()
        self.win.title("The Hive")
        self.win.geometry('{}x{}'.format(600, 400))
        self.canvas = Canvas(self.win, bg='#454b54')
        self.canvas.pack(expand=TRUE, fill=BOTH)
        self.frame = Frame(self.canvas, bg='#454b54', width=600, height=340)
        self.frame.pack(expand=TRUE)
        self.textBox = Text(self.frame, width=20, height=10)
        self.textBox1 = Text(self.frame, width=20, height=10)
        self.users = Treeview(self.frame, columns=1, show="headings", height="7")
        # self.groups = Treeview(self.frame, columns=1, show="headings", height="7")

    def main(self):
        Label(self.frame, text="Write a complain:", bg="#454b54", fg="#f7cc35",
              font="Arial 10 bold").grid(row=0, column=0)
        self.textBox1.grid(row=1, column=0, pady=5)
        Button(self.frame, text="Complain", bg='#2C92D6', fg='#C5A32A', command=self.send_complain).grid(row=2, column=0, sticky=N)

        Label(self.frame, text="Write a Compliment:", bg="#454b54", fg="#f7cc35",
              font="Arial 10 bold").grid(row=0, column=2)
        self.textBox.grid(row=1, column=2, pady=5)
        Button(self.frame, text="Compliment", bg='#2C92D6', fg='#C5A32A', command=self.send_compliment).grid(row=2, column=2)

        self.users.grid(row=0, column=1, rowspan=7, padx=20)
        self.users.heading(1, text="Select User")
        # self.groups.grid(row=5, column=1, rowspan=7, padx=20)
        # self.groups.heading(1, text="Select Group")

        db.cursor.execute("SELECT username FROM users WHERE user_type <> 'SU'")
        users = db.cursor.fetchall()
        for row in users:
            self.users.insert('', END, values=row)
        
        ### implement how to complain a group  
        # user = db.getName()
        # db.cursor.execute(" SELECT name,description,projRank FROM projects A\
        #                     INNER JOIN group_membership B\
        #                     ON A.id = B.group_id\
        #                     WHERE B.username = %s", (user,))
        # group_list = db.cursor.fetchall()
        # for row in group_list:
        #     self.groups.insert('', END, values=row)

        self.win.mainloop()
        

    def send_complain(self):
        for selected_item in self.users.selection():
            user_id = self.users.item(selected_item, 'values')[0]
     
        description = self.textBox1.get("1.0", "end-1c")
        user = db.getName()
        db.cursor.execute("INSERT INTO comments\
            (commentator,userdirected,comment,comment_type)\
            values(%s,%s,%s,0)", (user,user_id,description))
        
        db.cursor.execute("SELECT reputation_score FROM users WHERE username = %s",(user_id,))
        curr_rs =  db.cursor.fetchone()[0]
        new_rs = reputationScore.changeScore(curr_rs,-1)
        db.cursor.execute("UPDATE users SET reputation_score = %s WHERE username = %s",(new_rs,user_id,))

    def send_compliment(self):
        for selected_item in self.users.selection():
            user_id = self.users.item(selected_item, 'values')[0]
     
        description = self.textBox.get("1.0", "end-1c")
        user = db.getName()
        db.cursor.execute("INSERT INTO comments\
            (commentator,userdirected,comment,comment_type)\
            values(%s,%s,%s,1)", (user,user_id,description))

        db.cursor.execute("SELECT reputation_score FROM users WHERE username = %s",(user_id,))
        curr_rs =  db.cursor.fetchone()[0]
        new_rs = reputationScore.changeScore(curr_rs,1)
        db.cursor.execute("UPDATE users SET reputation_score = %s WHERE username = %s",(new_rs,user_id,))

    
    def complain_group(self):
        for selected_item in  self.groups.selection():
            group_name = self.groups.item(selected_item, 'values')[0]

if __name__ == "__main__":
    x = Comment()
    x.main()

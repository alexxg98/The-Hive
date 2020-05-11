from tkinter import*
import visitor
import db

class viewProject:
    def __init__(self, projName):
        self.projName = projName
        db.cursor.execute("SELECT id FROM projects WHERE name = '%s'"%projName)
        projID = db.cursor.fetchone()[0]

        # Get users in this proj
        db.cursor.execute("SELECT username FROM group_membership WHERE group_id = '%d'"%projID)
        #store all username in array
        userList = []
        for row in db.cursor:
            userList.append(row)

        ##Store proj name in variable if exist
        try:
            user1 = userList[0]
        except:
            user1 = "NULL"

        try:
            user2 = userList[1]
        except:
            user2 = "NULL"
        try:
            user3 = userList[2]
        except:
            user3 = "NULL"


        self.win = Tk()
        self.win.title("Top Projects")
        self.win.geometry('{}x{}'.format(800, 450))
        self.canvas = Canvas(self.win, bg='white')
        self.banner = Label(self.canvas, bg = "black", height = 4, width = 600)

        self.project = Label(self.canvas, text = projName,
                        font="Arial 20 bold", bg = 'white')
        # place holder for top 3 projects
        self.project1 = Button(self.canvas, text=user1, font='Arial 20 bold', bg='white', fg="black", width = 30, height = 2)
        self.project2 = Button(self.canvas, text=user2, font='Arial 20 bold', bg='white', fg="black", width = 30, height = 2)
        self.project3 = Button(self.canvas, text=user3, font='Arial 20 bold', bg='white', fg="black", width = 30, height = 2)
        self.back = PhotoImage(file = r"images/back.png")
        self.backButton = Button(self.canvas, image = self.back, command = self.visitor, bd = 0, bg = "black")

    def main(self):
        self.canvas.pack(expand=TRUE, fill=BOTH)
        self.project.place(x = 50, y = 380)
        self.banner.place(x = 0, y= 0)
        self.project1.place(x = 380, y = 150)
        self.project2.place(x = 380, y = 250)
        self.project3.place(x = 380, y = 350)
        self.backButton.place(x = 20, y = 20)

        self.win.mainloop()

    def visitor(self):
        self.win.destroy()
        back = visitor.VisitorPage()
        back.main()

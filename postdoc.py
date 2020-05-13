from tkinter import*
from tkinter import scrolledtext
import sys
from tkinter.filedialog import askopenfile
import db
import checkForTaboo as checkT
import reputationScore as repScore

class PostDoc:
    def __init__(self):
        self.win = Tk()
        self.win.title('Post Updates')
        self.win.configure(bg = "#36393F")
        self.win.geometry('{}x{}'.format(600, 400))

        #Get and store user info from database
        name = db.getName()
        db.cursor.execute("SELECT id FROM projects WHERE viewing = 'ON'")
        groupID = db.cursor.fetchone()[0]
        db.cursor.execute("SELECT postid FROM posts WHERE group_id = '%s' ORDER BY postid DESC LIMIT 1" % groupID)
        postCount = db.cursor.fetchone()[0]
        tabooCount = db.getTabooCount()
        reputation = db.getRepScore()

        # Parent widget for the buttons
        self.buttons_frame = Frame(self.win)
        self.buttons_frame.configure(bg = "black")
        self.buttons_frame.grid(row=0, column=0, sticky=W+E)

        self.btn_Image = Button(self.buttons_frame, text='Clear', command = self.clear)
        self.btn_Image.grid(row=0, column=0, padx=(10), pady=10)

        self.btn_File = Button(self.buttons_frame, text='File', command = self.open_file)
        self.btn_File.grid(row=0, column=2, padx=(10), pady=10)

        self.submit_btn = Button(self.buttons_frame, text='Submit', command = lambda:self.submit(name, groupID, postCount+1, tabooCount, reputation))
        self.submit_btn.grid(row=0, column=4, padx=(10), pady=10)

        self.frame = LabelFrame(self.win, text="Hive Post", padx=5, pady=5, bg = "#36393F", fg = "white")
        self.frame.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky=E+W+N+S)

        self.win.columnconfigure(0, weight=1)
        self.win.rowconfigure(1, weight=1)

        self.frame.rowconfigure(0, weight=1)
        self.frame.columnconfigure(0, weight=1)

        # Create the textbox
        self.textbox = scrolledtext.ScrolledText(self.frame, width=40, height=10)
        self.textbox.grid(row=0, column=0, sticky=E+W+N+S)
        self.win.mainloop()

    def open_file(self):
        self.file = askopenfile(mode ='r', filetypes =[('Text Files', '*.txt')])
        if self.file is not None:
            self.content = self.file.read()
            self.textbox.insert(INSERT, self.content)
    def clear(self):
        self.textbox.delete("1.0","end")
    def submit(self, name, groupID, postCount, tabooCount, reputation):
        current_input = self.textbox.get("1.0", END)
        hasTaboo = checkT.check(current_input)
        post = current_input
        if hasTaboo:
            tabooCount += 1
            newRep = repScore.tabooWord(reputation, tabooCount)
            db.cursor.execute("Update users SET reputation_score = %s where username = %s", (newRep, name))
            db.cursor.execute("Update users SET taboo_count = %s where username = %s", (tabooCount, name))
            post = checkT.replaceTaboo(current_input)
        db.cursor.execute("INSERT into posts(postid, group_id, username, content) VALUES (%s, %s, %s, %s)",(postCount,groupID,name,post))
        #Saves post in DB and closes window
        self.win.destroy()

postGUI = PostDoc()

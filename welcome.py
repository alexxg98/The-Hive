from tkinter import *
import login
import register


class WelcomeWindow:

    #create a constructor
    def __init__(self):
        # create a tkinter window
        self.win = Tk()

        #reset the window and background color
        self.canvas = Canvas(self.win, width=600, height=400, bg='white')
        self.canvas.pack(expand=YES, fill=BOTH)

        #show window in center of the screen
        width = self.win.winfo_screenwidth()
        height = self.win.winfo_screenheight()
        x = int(width / 2 - 600 / 2)
        y = int(height / 2 - 400 / 2)
        str1 = "600x400+"+ str(x) + "+" + str(y)
        self.win.geometry(str1)

        #disable resize of the window
        self.win.resizable(width=False, height=False)

        #change the title of the window
        self.win.title("The Hive")

    def add_frame(self):
        #create a inner frame
        self.frame = Frame(self.win, height=300, width=450)
        self.frame.place(x=80, y=50)

        # place the photo in the frame
        self.img = PhotoImage(file='images/icon.png')
        self.label = Label(self.frame, image=self.img)
        self.label.place(x=150, y=20)

        self.labeltitle = Label(self.frame, text="Welcome to The Hive")
        self.labeltitle.config(font=("Courier", 20, 'bold'))
        self.labeltitle.place(x=40, y=170)

        self.button = Button(self.frame, text="Login", font=('helvetica', 20)
                             , bg='dark green', fg='white', command=self.login)
        self.button.place(x=90, y=220)

        self.button = Button(self.frame, text="Register", font=('helvetica', 20)
                             , bg='dark green', fg='white', command=self.register)
        self.button.place(x=200, y=220)

        self.win.mainloop()

    #open a new window on button press
    def login(self):
        # destroy current window
        self.win.destroy()

        #open the new window
        log = login.LoginWindow()
        log.add_frame()

    def register(self):
        # destroy current window
        self.win.destroy()

        #open the new window
        reg = register.RegisterWindow()
        reg.add_frame()


if __name__ == "__main__":
    x = WelcomeWindow()
    x.add_frame()

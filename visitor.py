from tkinter import *
import welcome


class VisitorPage:

    # create a constructor
    def __init__(self):
        # create a tkinter window
        self.win = Tk()

        # reset the window and background color
        self.canvas = Canvas(self.win, width=600, height=400, bg='white')
        self.canvas.pack(expand=YES, fill=BOTH)

        # show window in center of the screen
        width = self.win.winfo_screenwidth()
        height = self.win.winfo_screenheight()
        x = int(width / 2 - 600 / 2)
        y = int(height / 2 - 400 / 2)
        str1 = "600x400+" + str(x) + "+" + str(y)
        self.win.geometry(str1)

        # disable resize of the window
        self.win.resizable(width=False, height=False)

        # change the title of the window
        self.win.title("The Hive")

    def main(self):
        labeltitle = Label(text="Visitor Page")
        labeltitle.config(font=("Courier", 20, 'bold'))
        labeltitle.place(x=40, y=170)

        button = Button(text="Login/Register", font=('helvetica', 20)
                             , bg='dark green', fg='white', command=self.welcome)
        button.place(x=200, y=220)

        self.win.mainloop()

    # open a new window on button press
    def welcome(self):
        # destroy current window
        self.win.destroy()

        # open the new window
        wel = welcome.WelcomeWindow()
        wel.main()


if __name__ == "__main__":
    x = VisitorPage()
    x.main()

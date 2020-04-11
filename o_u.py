from tkinter import Label, Tk, Canvas, Frame, BOTH
from tkinter import*

# Class to create the hexagon framework
class hexagon(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.master.title("Ordinary User")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)

        user_select_1 = [387,250,300,200,
                    300,200,213,250,
                    213,250,213,350,
                    213,350,300,400,
                    300,400,387,350,
                    387,350,387,250]
        user_select_2 = [562,250,475,200,
                    475,200,388,250,
                    388,250,388,350,
                    388,350,475,400,
                    475,400,562,350,
                    562,350,562,250]
        user_select_3 = [474,400,387,350,
                    387,350,300,400,
                    300,400,300,500,
                    300,500,387,550,
                    387,550,474,500,
                    474,500,474,400]
        user_display_name = [452,313,387,275,
                    387,275,322,313,
                    322,313,322,388,
                    322,388,387,425,
                    387,425,452,388,
                    452,388,452,313]

        canvas.create_polygon(user_select_1, outline='black',
            fill='#2C92D6', width=2)
        canvas.create_polygon(user_select_2, outline='black',
            fill='#37CAEF', width=2)
        canvas.create_polygon(user_select_3, outline='black',
            fill='#3EDAD8', width=2)
        canvas.create_polygon(user_display_name, outline='black',
            fill='#ffffff', width=2)

        canvas.pack(fill=BOTH, expand=1)
        canvas.configure(bg='#36393F')
        # place holder for username
        canvas.create_text(385, 350, text = "USERNAME", fill = "black")
        # greeting for user
        canvas.create_text(120, 35, text = "Hello . . .", font = ("Pursia",20,),
            fill = "#7289DB")
        # My Projects
        canvas.create_text(120, 500, text = "MY PROJECTS", font = ("Pursia",15),
            fill = "#7289DB")
        # Button for social
        # photo = PhotoImage(file = "user.png")
        # Button(canvas, text = 'Click Me !', image = photo).pack()


def main():
    root = Tk()
    label = Label(
        text="The HIVE",
        fg="white",
        bg="black",
        width=200,
        height=5
    )
    label.pack()

    frame = hexagon()
    root.geometry("800x800")
    root.mainloop()


if __name__ == '__main__':
    main()

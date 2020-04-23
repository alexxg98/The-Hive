from tkinter import Label, Tk, Canvas, Frame, BOTH
from tkinter import*

# Class to create the hexagon framework
class hexagon(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.master.title("Ordinary User")
        self.pack(fill=BOTH, expand=TRUE)

        canvas = Canvas(self)
        user_select_1 = [500,200,413,150,
                        413,150,326,200,
                        326,200,326,300,
                        326,300,413,350,
                        413,350,500,300,
                        500,300,500,200]
        user_select_2 = [675,200,588,150,
                        588,150,501,200,
                        501,200,501,300,
                        501,300,588,350,
                        588,350,675,300,
                        675,300,675,200]
        user_select_3 = [587,351,500,301,
                        500,301,413,351,
                        413,351,413,451,
                        413,451,500,501,
                        500,501,587,451,
                        587,451,587,351]
        user_display_name = [565,263,500,225,
                            500,225,435,263,
                            435,263,435,338,
                            435,338,500,375,
                            500,375,565,338,
                            565,338,565,263]
        canvas.create_polygon(user_select_1, outline='black',
            fill='#2C92D6', width=2)
        canvas.create_polygon(user_select_2, outline='black',
            fill='#37CAEF', width=2)
        canvas.create_polygon(user_select_3, outline='black',
            fill='#3EDAD8', width=2)
        canvas.create_polygon(user_display_name, outline='black',
            fill='#ffffff', width=2)


        # hexagon for projects
        p1 = [95,391,75,380,
              75,380,55,391,
              55,391,55,409,
              55,409,75,420,
              75,420,95,409,
              95,409,95,391]
        p2 = [95,491,75,480,
              75,480,55,491,
              55,491,55,509,
              55,509,75,520,
              75,520,95,509,
              95,509,95,491]
        p3 = [95,591,75,580,
              75,580,55,591,
              55,591,55,609,
              55,609,75,620,
              75,620,95,609,
              95,609,95,591]
        canvas.create_polygon(p1,fill='white', width=1)
        canvas.create_polygon(p2,fill='white', width=1)
        canvas.create_polygon(p3,fill='white', width=1)

        # hexagon for user select
        s1 = [520,167,500,156,
              500,156,480,167,
              480,167,480,185,
              480,185,500,196,
              500,196,520,185,
              520,185,520,167]
        canvas.create_polygon(s1,fill='white', width=1)
        s2 = [412,355,392,344,
              392,344,372,355,
              372,355,372,373,
              372,373,392,384,
              392,384,412,373,
              412,373,412,355]
        canvas.create_polygon(s2,fill='white', width=1)
        s3 = [629,355,609,344,
              609,344,589,355,
              589,355,589,373,
              589,373,609,384,
              609,384,629,373,
              629,373,629,355]
        canvas.create_polygon(s3,fill='white', width=1)

        canvas.create_text(150, 400, text = "Project 1", font = ("Pursia",15),
            fill = "white")
        canvas.create_text(150, 500, text = "Project 2", font = ("Pursia",15),
            fill = "white")
        canvas.create_text(150, 600, text = "Project 3", font = ("Pursia",15),
            fill = "white")
        # hexagon for groups
        g1 = [795,391,775,380,
              775,380,755,391,
              755,391,755,409,
              755,409,775,420,
              775,420,795,409,
              795,409,795,391]
        g2 = [795,491,775,480,
              775,480,755,491,
              755,491,755,509,
              755,509,775,520,
              775,520,795,509,
              795,509,795,491]
        g3 = [795,591,775,580,
              775,580,755,591,
              755,591,755,609,
              755,609,775,620,
              775,620,795,609,
              795,609,795,591]
        canvas.create_polygon(g1,fill='white', width=1)
        canvas.create_polygon(g2,fill='white', width=1)
        canvas.create_polygon(g3,fill='white', width=1)
        canvas.create_text(850, 400, text = "Group 1", font = ("Pursia",15),
            fill = "white")
        canvas.create_text(850, 500, text = "Group 2", font = ("Pursia",15),
            fill = "white")
        canvas.create_text(850, 600, text = "Group 3", font = ("Pursia",15),
            fill = "white")


        canvas.pack(fill=BOTH, expand=1)
        canvas.configure(bg='#36393F')
        # place holder for username
        canvas.create_text(500, 300, text = "USERNAME", fill = "black")
        # greeting for user
        canvas.create_text(120, 50, text = "Hello . . .", font = ("Pursia",25),
            fill = "#7289DB")
        # My Projects
        canvas.create_text(120, 340, text = "MY PROJECTS", font = ("Pursia",15),
            fill = "#7289DB")
        canvas.create_text(815, 340, text = "MY GROUPS", font = ("Pursia",15),
            fill = "#7289DB")
        # Button for social
        # photo = PhotoImage(file = "user.png")
        # Button(canvas, text = 'Click Me !', image = photo).pack()


def main():
    root = Tk()
    # label = Label(
    #     text="The HIVE",
    #     fg="white",
    #     bg="black",
    #     width=200,
    #     height=3
    # )
    # label.pack()

    frame = hexagon()
    root.geometry("1000x700")
    root.mainloop()


if __name__ == '__main__':
    main()

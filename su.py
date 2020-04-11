from tkinter import Label, Tk, Canvas, Frame, BOTH

# Class to create the hexagon framework
class Hexagon(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.master.title("Shapes")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        # canvas.create_oval(10, 10, 80, 80, outline="#f11",
        #     fill="#1f1", width=2)
        # canvas.create_oval(110, 10, 210, 80, outline="#f11",
        #     fill="#1f1", width=2)
        # canvas.create_rectangle(230, 10, 290, 60,
        #     outline="#f11", fill="#1f1", width=2)
        # canvas.create_arc(30, 200, 90, 100, start=0,
        #     extent=210, outline="#f11", fill="#1f1", width=2)

        points = [387,250,300,200,
                    300,200,213,250,
                    213,250,213,350,
                    213,350,300,400,
                    300,400,387,350,
                    387,350,387,250]
        points_1 = [562,250,475,200,
                    475,200,388,250,
                    388,250,388,350,
                    388,350,475,400,
                    475,400,562,350,
                    562,350,562,250]
        points_2 = [474,400,387,350,
                    387,350,300,400,
                    300,400,300,500,
                    300,500,387,550,
                    387,550,474,500,
                    474,500,474,400]
        points_3 = [452,313,387,275,
                    387,275,322,313,
                    322,313,322,388,
                    322,388,387,425,
                    387,425,452,388,
                    452,388,452,313]
        points_4 = [350,213,250,213,
                    250,213,200,300,
                    200,300,250,387,
                    250,387,350,387,
                    350,387,400,300,
                    400,300,350,213]

        canvas.create_polygon(points, outline='#f11',
            fill='#6d879c', width=2)
        canvas.create_polygon(points_1, outline='#f11',
            fill='#4baffe', width=2)   
        canvas.create_polygon(points_2, outline='#f11',
            fill='#a7d2f5', width=2)
        canvas.create_polygon(points_3, outline='#f11',
            fill='#ffffff', width=2)   
        # canvas.create_polygon(points_4, outline='#f11',
        #     fill='#1f1', width=2)

        canvas.pack(fill=BOTH, expand=1)


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
    frame = Hexagon()
    root.geometry("800x800")
    root.mainloop()

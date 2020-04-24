from tkinter import Label, Tk, Canvas, Frame, BOTH
from tkinter import * 


# Class to create the hexagon framework
class Hexagon(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.master.title("Super User")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)

        #  Calculate dimensions: https://www.mathopenref.com/coordpolycalc.html
        # heaxagons
        user_select_1 = [587,350,500,300,
                    500,300,413,350,
                    413,350,413,450,
                    413,450,500,500,
                    500,500,587,450,
                    587,450,587,350]
        user_select_2 = [412,350,325,300,
                    325,300,238,350,
                    238,350,238,450,
                    238,450,325,500,
                    325,500,412,450,
                    412,450,412,350]
        user_select_3 = [500,200,413,150,
                    413,150,326,200,
                    326,200,326,300,
                    326,300,413,350,
                    413,350,500,300,
                    500,300,500,200]
        user_display_name = [478,313,413,275,
                    413,275,348,313,
                    348,313,348,388,
                    348,388,413,425,
                    413,425,478,388,
                    478,388,478,313]

        canvas.create_polygon(user_select_1, outline='black',
            fill='#2C92D6', width=2)
        canvas.create_polygon(user_select_2, outline='black',
            fill='#37CAEF', width=2)   
        canvas.create_polygon(user_select_3, outline='black',
            fill='#3EDAD8', width=2)
        canvas.create_polygon(user_display_name, outline='black',
            fill='#ffffff', width=2)   

        # hexagon for projects
        points_1 = [326,276,304,263,
                    304,263,282,276,
                    282,276,282,301,
                    282,301,304,313,
                    304,313,326,301,
                    326,301,326,276]
        points_2 = [544,276,522,263,
                    522,263,500,276,
                    500,276,500,301,
                    500,301,522,313,
                    522,313,544,301,
                    544,301,544,276]
        points_3 = [435,463,413,450,
                    413,450,391,463,
                    391,463,391,488,
                    391,488,413,500,
                    413,500,435,488,
                    435,488,435,463]

        canvas.create_polygon(points_1, fill='#2C92D6', width=2)
        canvas.create_polygon(points_2, fill='#37CAEF', width=2)
        canvas.create_polygon(points_3, fill='#3EDAD8', width=2)
        
        # hexagon for groups
        g1 = [795,391,775,380,
              775,380,755,391,
              755,391,755,409,
              755,409,775,420,
              775,420,795,409,
              795,409,795,391]
        g2 = [795,466,775,455,
              775,455,755,466,
              755,466,755,484,
              755,484,775,495,
              775,495,795,484,
              795,484,795,466]
        g3 = [795,541,775,530,
              775,530,755,541,
              755,541,755,559,
              755,559,775,570,
              775,570,795,559,
              795,559,795,541]

        canvas.create_polygon(g1, fill='white', width=1)
        canvas.create_polygon(g2, fill='white', width=1)
        canvas.create_polygon(g3, fill='white', width=1)
        canvas.create_text(850, 400, text = "Group 1", font = ("Pursia",15),
            fill = "white")
        canvas.create_text(850, 475, text = "Group 2", font = ("Pursia",15),
            fill = "white")
        canvas.create_text(850, 550, text = "Group 3", font = ("Pursia",15),
            fill = "white")
        
        
        
        canvas.pack(fill=BOTH, expand=1)
        canvas.configure(bg='#36393F')
        # place holder for username
        canvas.create_text(500, 300, text = "USERNAME", fill = "black")
        # greeting for user
        canvas.create_text(120, 35, text = "Hello . . .", font = ("Pursia",25),
            fill = "#7289DB")
        # My Projects
        canvas.create_text(120, 500, text = "MY PROJECTS", font = ("Pursia",15),
            fill = "#7289DB")
        # Button for social
        # photo = PhotoImage(file = "user.png")
        # Button(canvas, text = 'Click Me !', image = photo).pack()


def main():
    root = Tk()
    frame = Hexagon()
    
    root.geometry("1000x800")
    root.mainloop()

if __name__ == '__main__':
    main() 
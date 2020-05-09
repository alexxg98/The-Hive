import os
from tkinter import *
from tkinter.ttk import Combobox
from prettytable import PrettyTable


class SchedulePage:

    def __init__(self):
        self.win = Tk()
        self.win.title("The Hive")
        self.win.geometry('{}x{}'.format(800, 450))
        self.canvas = Canvas(self.win, bg='#454b54')
        self.frame = Frame(self.canvas, bg='#454b54', width=600, height=340)

        headerFormat = ["Group", "Date", "StartTime", "EndTime"]
        self.table = PrettyTable(headerFormat)

        self.group = StringVar()
        self.date = StringVar()
        self.startTime = StringVar()
        self.endTime = StringVar()

        self.schedule = Text(self.frame, width=50, height=15)

        self.TimeStartDrop = Combobox(self.frame, width=10, textvariable=self.startTime, state="readonly")
        self.TimeStartDrop['values'] = ("-Start-", "8:00am", "9:00am", "10:00am", "11:00am", "12:00pm", "1:00pm",
                                        "2:00pm", "3:00pm", "4:00pm", "5:00pm", "6:00pm", "7:00pm", "8:00pm",
                                        "9:00pm", "10:00pm")

        self.TimeEndDrop = Combobox(self.frame, width=10, textvariable=self.endTime, state="readonly")
        self.TimeEndDrop['values'] = ("-End-", "8:00am", "9:00am", "10:00am", "11:00am", "12:00pm", "1:00pm",
                                      "2:00pm", "3:00pm", "4:00pm", "5:00pm", "6:00pm", "7:00pm", "8:00pm",
                                      "9:00pm", "10:00pm")

        self.create = Button(self.frame, text="Create", command=self.add)
        self.view = Button(self.frame, text="View Schedule", command=self.printSchedule)
        self.delete = Button(self.frame, text="Clear Schedule", command=self.deleteAll)

    def main(self):
        self.canvas.pack(expand=TRUE, fill=BOTH)
        self.frame.pack(expand=TRUE)
        Label(self.frame, text="Add Group, Date, and Time:", bg="#454b54", fg="#f7cc35",
              font="Arial 10 bold").grid(row=0, column=0, columnspan=4)

        Entry(self.frame, width=15, textvariable=self.group).grid(row=1, column=0)
        Entry(self.frame, width=15, textvariable=self.date).grid(row=1, column=1)

        self.TimeStartDrop.grid(row=1, column=2)
        self.TimeEndDrop.grid(row=1, column=3)
        self.TimeStartDrop.current(0)
        self.TimeEndDrop.current(0)

        self.schedule.grid(row=2, columnspan=4, pady=10)
        self.create.grid(row=3, column=0)
        self.view.grid(row=3, column=2)
        self.delete.grid(row=3, column=3)

        self.win.mainloop()

    def add(self):
        self.table.add_row([self.group.get(), self.date.get(), self.startTime.get(), self.endTime.get()])
        open("text.txt", "w").close()
        file_new = open("text.txt", "a")
        file_new.write(str(self.table) + '\n')
        file_new.close()

    def printSchedule(self):
        self.schedule.delete(1.0, END)
        if os.stat("text.txt").st_size == 0:
            self.schedule.insert(INSERT, "No Event Found")
        else:
            with open("text.txt", "r") as file_new:
                contents = file_new.read()
                self.schedule.insert(INSERT, contents)
                self.schedule.see(INSERT)

    def deleteAll(self):
        open("text.txt", "w").close()
        self.schedule.delete(1.0, END)


if __name__ == "__main__":
    x = SchedulePage()
    x.main()

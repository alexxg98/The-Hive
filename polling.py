from tkinter import *
from tkinter.ttk import Combobox
import db


def viewResults():
    results = Toplevel()
    results.geometry('200x200')
    db.cursor.execute('SELECT * FROM polls')
    data = db.cursor.fetchall()
    for i in range(len(data)):
        Label(results, text=data[i][0] + ': ' + str(data[i][1]) + ' votes').pack()


def voteMeeting():
    votes = Toplevel(bg='#454b54')
    votes.geometry('300x200')

    def vote():
        db.cursor.execute('UPDATE polls SET votes=votes+1 WHERE entry = %s', (choice.get(),))
        db.db.commit()

    choice = StringVar()
    dates = ["-Select-"]
    db.cursor.execute('SELECT entry FROM polls')
    entries = db.cursor.fetchall()
    for i in range(len(entries)):
        dates.append(entries[i][0])

    Label(votes, text='Choose your vote ', bg="#454b54", fg="#f7cc35",
          font="Arial 15 bold").pack(expand=TRUE)
    select = Combobox(votes, values=dates, state='readonly', textvariable=choice)
    select.pack(expand=TRUE)
    select.current(0)
    Button(votes, text='Vote', command=vote).pack(expand=TRUE)


class PollingPage:

    def __init__(self):
        self.win = Tk()
        self.win.title("The Hive")
        self.win.geometry('{}x{}'.format(400, 300))
        self.canvas = Canvas(self.win, bg='#454b54')

        self.create = Button(self.canvas, text='Create Poll', font='Arial 15 bold', bg='#454b54',
                             fg='#f7cc35', command=self.createPoll)
        self.vote = Button(self.canvas, text='Vote', font='Arial 15 bold', bg='#454b54',
                           fg='#f7cc35', command=voteMeeting)
        self.view = Button(self.canvas, text='Poll Results', font='Arial 15 bold', bg='#454b54',
                           fg='#f7cc35', command=viewResults)

        self.pollDate = StringVar()
        self.pollStart = StringVar()
        self.pollEnd = StringVar()

        self.pollLab = Label(self.canvas, text='Enter available date and time for poll: ', bg="#454b54", fg="#f7cc35",
                             font="Arial 15 bold")
        self.dateEntry = Entry(self.canvas, width=15, textvariable=self.pollDate)
        self.proceedButton = Button(self.canvas, text='Proceed', command=self.proceed)

        self.TimeStartDrop = Combobox(self.canvas, width=10, textvariable=self.pollStart, state="readonly")
        self.TimeStartDrop['values'] = ("-Start-", "8:00am", "9:00am", "10:00am", "11:00am", "12:00pm", "1:00pm",
                                        "2:00pm", "3:00pm", "4:00pm", "5:00pm", "6:00pm", "7:00pm", "8:00pm",
                                        "9:00pm", "10:00pm")

        self.TimeEndDrop = Combobox(self.canvas, width=10, textvariable=self.pollEnd, state="readonly")
        self.TimeEndDrop['values'] = ("-End-", "8:00am", "9:00am", "10:00am", "11:00am", "12:00pm", "1:00pm",
                                      "2:00pm", "3:00pm", "4:00pm", "5:00pm", "6:00pm", "7:00pm", "8:00pm",
                                      "9:00pm", "10:00pm")

    def main(self):
        self.canvas.pack(expand=TRUE, fill=BOTH)
        self.create.pack(expand=TRUE)
        self.vote.pack(expand=TRUE)
        self.view.pack(expand=TRUE)
        self.win.mainloop()

    def createPoll(self):
        self.create.pack_forget()
        self.vote.pack_forget()
        self.view.pack_forget()
        self.pollLab.pack(expand=TRUE)
        self.dateEntry.pack(expand=TRUE)
        self.TimeStartDrop.pack(expand=TRUE)
        self.TimeStartDrop.current(0)
        self.TimeEndDrop.pack(expand=TRUE)
        self.TimeEndDrop.current(0)
        self.proceedButton.pack(expand=TRUE)

    def proceed(self):
        entry = self.pollDate.get() + " " + self.pollStart.get() + "-" + self.pollEnd.get()
        self.dateEntry.delete(0, END)
        db.cursor.execute('INSERT INTO polls VALUES (%s, %s)', (entry, 0))
        self.pollLab.pack_forget()
        self.dateEntry.pack_forget()
        self.TimeStartDrop.pack_forget()
        self.TimeEndDrop.pack_forget()
        self.proceedButton.pack_forget()
        self.main()


if __name__ == "__main__":
    x = PollingPage()
    x.main()

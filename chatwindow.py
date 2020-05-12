from tkinter import*
import mysql.connector
import sys
import db

#Get and store user info from database
name = db.getName()
username = '[' + name + ']: '

# send message through button
def Press_Button():
    get_input = input_field.get()
    input_field.delete(0, 'end')
    messages.configure(state='normal')
    messages.insert('end', username + '%s\n'%get_input)
    messages.configure(state = "disabled")

# send message through enter key
def Input_Enter(event):
    get_input = input_field.get()
    messages.configure(state='normal')
    messages.insert(INSERT, username + '%s\n'%get_input)
    messages.configure(state='disabled')
    user_input.set('')
    return "break"

filename = 'chat_log.txt'
def savelog():
    chatMessages = messages.get("1.0", END)
    with open(filename, 'w') as file:
            file.write(chatMessages)
# clear contents of chat_log.txt
def clear_log():
    file = open(filename, 'w+')
    file.truncate(0)


window = Tk()

chatBox = Scrollbar(window)
messages = Text(window, wrap='word', state='disabled', yscrollcommand=chatBox.set)
chatBox.configure(command=messages.yview)
messages.grid(row = 0, column = 0, columnspan = 10)

user_input = StringVar()
input_field = Entry(window, width = 90, text = user_input, bg="#e6f2ff")
input_field.grid(row = 1, column = 0)

frame = Frame(window)
input_field.bind("<Return>", Input_Enter)
frame.grid(row = 0, column = 0)
send = Button(window, text = "Send", command = Press_Button, bg = "black", fg = "white")
send.grid(row = 1, column = 1)
save = Button(window, text = "Save Log", bg = "red", fg = "white", command = lambda: savelog())
save.grid(row = 1, column = 2)
save = Button(window, text = "Clear Log", bg = "blue", fg = "white", command = lambda: clear_log())
save.grid(row = 1, column = 3)

messages.configure(state='normal')
try:
    with open(filename, 'r') as file:
        messages.insert(INSERT, file.read())
except IOError:
    file = open(filename, 'w')
messages.configure(state='disabled')
file.close()

window.resizable(False, False)
window.title("Hive Chat")
window.mainloop()

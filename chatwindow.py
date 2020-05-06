from tkinter import*

window = Tk()

messages = Text(window, bg = "#36393F", fg = "white")
messages.grid(row = 0, column = 0, columnspan = 2)

user_input = StringVar()
input_field = Entry(window, width = 100, text = user_input)
input_field.grid(row = 1, column = 0)
# place holder for username
username = "Username: "
# send message through button
def Press_Button():
    get_input = input_field.get()
    input_field.delete(0, 'end')
    messages.insert(INSERT, username + '%s\n'%get_input)
    user_input.set('')
    return "break"
# send message through enter key
def Input_Enter(event):
    get_input = input_field.get()
    messages.insert(INSERT, username + '%s\n'%get_input)
    user_input.set('')
    return "break"

frame = Frame(window)
input_field.bind("<Return>", Input_Enter)
frame.grid(row = 0, column = 0)
send = Button(window, text = "Send", command = Press_Button, bg = "black", fg = "white")
send.grid(row = 1, column = 1, columnspan = 2)

window.resizable(False, False)
window.title("Hive Chat")
window.mainloop()

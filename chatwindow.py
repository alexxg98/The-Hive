from tkinter import*

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
window = Tk()

chatBox = Scrollbar(window)
messages = Text(window, wrap='word', state='disabled', yscrollcommand=chatBox.set,bg = "#36393F", fg = "white")
chatBox.configure(command=messages.yview)
messages.grid(row = 0, column = 0, columnspan = 2)

user_input = StringVar()
input_field = Entry(window, width = 100, text = user_input)
input_field.grid(row = 1, column = 0)
# place holder for username
username = "Username: "


frame = Frame(window)
input_field.bind("<Return>", Input_Enter)
frame.grid(row = 0, column = 0)
send = Button(window, text = "Send", command = Press_Button, bg = "black", fg = "white")
send.grid(row = 1, column = 1, columnspan = 2)

window.resizable(False, False)
window.title("Hive Chat")
window.mainloop()

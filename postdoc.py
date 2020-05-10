from tkinter import*
from tkinter import scrolledtext
from tkinter.filedialog import askopenfile

class PostDoc:
    def __init__(self):
        self.win = Tk()
        self.win.title('Post Updates')
        self.win.configure(bg = "#36393F")
        self.win.geometry('{}x{}'.format(600, 400))

        # Parent widget for the buttons
        self.buttons_frame = Frame(self.win)
        self.buttons_frame.configure(bg = "black")
        self.buttons_frame.grid(row=0, column=0, sticky=W+E)

        self.btn_Image = Button(self.buttons_frame, text='Image', command = self.add_image)
        self.btn_Image.grid(row=0, column=0, padx=(10), pady=10)

        self.btn_File = Button(self.buttons_frame, text='File', command = self.open_file)
        self.btn_File.grid(row=0, column=2, padx=(10), pady=10)

        self.submit_btn = Button(self.buttons_frame, text='Submit')
        self.submit_btn.grid(row=0, column=4, padx=(10), pady=10)

        self.group1 = LabelFrame(self.win, text="Hive Post", padx=5, pady=5, bg = "#36393F", fg = "white")
        self.group1.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky=E+W+N+S)

        self.win.columnconfigure(0, weight=1)
        self.win.rowconfigure(1, weight=1)

        self.group1.rowconfigure(0, weight=1)
        self.group1.columnconfigure(0, weight=1)

        # Create the textbox
        self.textbox = scrolledtext.ScrolledText(self.group1, width=40, height=10)
        self.textbox.grid(row=0, column=0, sticky=E+W+N+S)
        self.win.mainloop()

    def open_file(self):
        self.file = askopenfile(mode ='r', filetypes =[('Text Files', '*.txt')])
        if self.file is not None:
            self.content = self.file.read()
            self.textbox.insert(INSERT, self.content)
    def add_image(self):
        self.img = PhotoImage(file = "images/add.png")
        self.txtbox.image_create(END, image = self.img) # Example 1
        # self.txtbox.window_create(END, window = Label(txtbox, image = self.img)) # Example 2


postGUI = PostDoc()

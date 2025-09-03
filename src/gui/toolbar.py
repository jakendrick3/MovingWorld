from tkinter import Frame, Menu

class Toolbar(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_toolbar()

    def create_toolbar(self):
        self.toolbar = Menu(self.master)
        self.master.config(menu=self.toolbar)

        # File menu
        file_menu = Menu(self.toolbar, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Exit", command=self.master.quit)
        self.toolbar.add_cascade(label="File", menu=file_menu)

        # Edit menu
        edit_menu = Menu(self.toolbar, tearoff=0)
        edit_menu.add_command(label="Undo", command=self.undo_action)
        edit_menu.add_command(label="Redo", command=self.redo_action)
        self.toolbar.add_cascade(label="Edit", menu=edit_menu)

        # Help menu
        help_menu = Menu(self.toolbar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)
        self.toolbar.add_cascade(label="Help", menu=help_menu)

    def open_file(self):
        # Logic to open a file
        pass

    def undo_action(self):
        # Logic to undo an action
        pass

    def redo_action(self):
        # Logic to redo an action
        pass

    def show_about(self):
        # Logic to show about information
        pass
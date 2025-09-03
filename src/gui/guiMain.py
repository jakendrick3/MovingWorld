import tkinter as tk
from tkinter import Menu
from src.gui.toolbar import Toolbar
from src.gui.mapView import MapView

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python GUI Map App")
        self.root.geometry("800x600")

        self.toolbar = Toolbar(self.root)
        self.map_view = MapView(self.root)

        self.setup_menu()

    def setup_menu(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)

        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)

    def open_file(self):
        # Logic to open a file can be implemented here
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
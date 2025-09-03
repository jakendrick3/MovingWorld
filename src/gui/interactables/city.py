from .interactable import Interactable
import tkinter as tk

class City(Interactable):
    def __init__(self, x, y, name, state=None):
        super().__init__(x, y, state)
        self.name = name
        self.tooltip = None
        self.hover_id = None

    def on_click(self, master):
        popup = tk.Toplevel(master)
        popup.title(f"City: {self.name}")
        label = tk.Label(popup, text=f"Welcome to {self.name}!\nState: {self.state}")
        label.pack(padx=10, pady=10)

    def on_hover(self, master):
        if self.tooltip is None:
            self.tooltip = tk.Toplevel(master)
            self.tooltip.wm_overrideredirect(True)
            self.tooltip.geometry(f"+{self.x+50}+{self.y+50}")
            label = tk.Label(self.tooltip, text=f"{self.name} (hover)", background="yellow")
            label.pack()
        self.hover_id = master.after(2000, lambda: None)  # Placeholder for delay

    def get_state(self):
        return self.state

    def set_state(self, key, value):
        self.state[key] = value

    def remove_tooltip(self):
        if self.tooltip:
            self.tooltip.destroy()
            self.tooltip = None
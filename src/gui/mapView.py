from tkinter import Canvas
from src.gui.interactables.city import City

class MapView:
    def __init__(self, master):
        self.master = master
        self.canvas = None
        self.cities = []
        self.create_map()
        self.add_city(100, 100, "New York")

        # Bind resize event
        self.master.bind("<Configure>", self.on_resize)

    def create_map(self):
        self.canvas = Canvas(self.master, width=800, height=600)
        self.canvas.pack(fill="both", expand=True)
        self.draw_map()

    def draw_map(self):
        self.canvas.delete("all")
        w = self.canvas.winfo_width()
        h = self.canvas.winfo_height()
        # Draw map area scaled to canvas size
        self.canvas.create_rectangle(w*0.0625, h*0.083, w*0.9375, h*0.917, fill="lightblue")
        self.canvas.create_text(w//2, h//2, text="Map Area", font=("Arial", int(h*0.04)))

        # Redraw cities at their logical positions
        for city, cid in self.cities:
            x, y = city.x, city.y
            # Optionally scale city positions if you want them to move with the map area

            # Remove old city marker and label
            self.canvas.delete(cid)
            # Draw new marker and label
            new_cid = self.canvas.create_oval(x-10, y-10, x+10, y+10, fill="blue", outline="black")
            lid = self.canvas.create_text(x, y-18, text=city.name, font=("Arial", 10))
            # Re-bind events
            self.canvas.tag_bind(new_cid, "<Button-1>", lambda e, c=city: c.on_click(self.master))
            def on_enter(event, c=city):
                if getattr(c, "hover_id", None):
                    try:
                        self.canvas.after_cancel(c.hover_id)
                    except Exception:
                        pass
                c.hover_id = self.canvas.after(2000, lambda: c.on_hover(self.master))
            def on_leave(event, c=city):
                if getattr(c, "hover_id", None):
                    try:
                        self.canvas.after_cancel(c.hover_id)
                    except Exception:
                        pass
                    c.hover_id = None
                c.remove_tooltip()
            self.canvas.tag_bind(new_cid, "<Enter>", on_enter)
            self.canvas.tag_bind(new_cid, "<Leave>", on_leave)
            # Update city id in self.cities
            city_index = self.cities.index((city, cid))
            self.cities[city_index] = (city, new_cid)

    def on_resize(self, event):
        # Redraw map and cities on resize
        self.draw_map()

    def add_city(self, x, y, name):
        city = City(x, y, name)
        cid = self.canvas.create_oval(x-10, y-10, x+10, y+10, fill="blue", outline="black")
        lid = self.canvas.create_text(x, y-18, text=name, font=("Arial", 10))
        self.cities.append((city, cid))

        self.canvas.tag_bind(cid, "<Button-1>", lambda e, c=city: c.on_click(self.master))
        def on_enter(event, c=city):
            if getattr(c, "hover_id", None):
                try:
                    self.canvas.after_cancel(c.hover_id)
                except Exception:
                    pass
            c.hover_id = self.canvas.after(2000, lambda: c.on_hover(self.master))
        def on_leave(event, c=city):
            if getattr(c, "hover_id", None):
                try:
                    self.canvas.after_cancel(c.hover_id)
                except Exception:
                    pass
                c.hover_id = None
            c.remove_tooltip()
        self.canvas.tag_bind(cid, "<Enter>", on_enter)
        self.canvas.tag_bind(cid, "<Leave>", on_leave)

    def add_interactive_element(self, x, y, text):
        self.canvas.create_oval(x-5, y-5, x+5, y+5, fill="red", tags="interactive")
        self.canvas.create_text(x, y-10, text=text, font=("Arial", 12), tags="interactive")

    def handle_click(self, event):
        print(f"Clicked at: {event.x}, {event.y}")
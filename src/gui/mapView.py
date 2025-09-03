from tkinter import Canvas
from src.gui.interactables.city import City

class MapView:
    def __init__(self, master, grid_rows=20, grid_cols=30):
        self.master = master
        self.canvas = None
        self.grid_rows = grid_rows
        self.grid_cols = grid_cols
        self.grid = [[None for _ in range(grid_cols)] for _ in range(grid_rows)]  # 2D matrix
        self.city_lookup = {}  # city_id -> City object
        self.create_map()
        self.master.bind("<Configure>", self.on_resize)

        # Example: add a city at grid coordinate (10, 15)
        self.add_city(10, 15, "New York")

    def create_map(self):
        self.canvas = Canvas(self.master, width=800, height=600)
        self.canvas.pack(fill="both", expand=True)
        self.draw_map()

    def draw_map(self):
        self.canvas.delete("all")
        w = self.canvas.winfo_width()
        h = self.canvas.winfo_height()
        left = w * 0.0625
        top = h * 0.083
        right = w * 0.9375
        bottom = h * 0.917
        map_w = right - left
        map_h = bottom - top

        # Draw map area
        self.canvas.create_rectangle(left, top, right, bottom, fill="lightblue")
        self.canvas.create_text(w//2, h//2, text="Map Area", font=("Arial", int(h*0.04)))

        # Draw grid lines
        cell_w = map_w / self.grid_cols
        cell_h = map_h / self.grid_rows
        for i in range(self.grid_cols + 1):
            x = left + i * cell_w
            self.canvas.create_line(x, top, x, bottom, fill="#cccccc")
        for j in range(self.grid_rows + 1):
            y = top + j * cell_h
            self.canvas.create_line(left, y, right, y, fill="#cccccc")

        # Draw cities
        for city_id, city in self.city_lookup.items():
            row, col = city.grid_row, city.grid_col
            # Clamp to grid bounds
            row = max(0, min(self.grid_rows - 1, row))
            col = max(0, min(self.grid_cols - 1, col))
            # Center of cell
            x = left + (col + 0.5) * cell_w
            y = top + (row + 0.5) * cell_h
            city.x, city.y = x, y  # update pixel position for events
            # Draw city marker and label
            cid = self.canvas.create_oval(x-10, y-10, x+10, y+10, fill="blue", outline="black")
            lid = self.canvas.create_text(x, y-18, text=city.name, font=("Arial", 10))
            # Bind events
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

    def on_resize(self, event):
        self.draw_map()

    def add_city(self, grid_row, grid_col, name):
        # Generate a unique city id
        city_id = f"{name}_{grid_row}_{grid_col}"
        city = City(0, 0, name)
        city.grid_row = grid_row
        city.grid_col = grid_col
        self.city_lookup[city_id] = city
        self.grid[grid_row][grid_col] = city_id
        self.draw_map()

    def get_city_at(self, grid_row, grid_col):
        city_id = self.grid[grid_row][grid_col]
        return self.city_lookup.get(city_id, None)
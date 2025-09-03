from abc import ABC, abstractmethod

class Interactable(ABC):
    def __init__(self, x, y, state=None):
        self.x = x
        self.y = y
        self.state = state or {}

    @abstractmethod
    def on_click(self, master):
        """Open a popup panel in the GUI when clicked."""
        pass

    @abstractmethod
    def on_hover(self, master):
        """Open a tooltip if hovered for more than 2 seconds."""
        pass

    @abstractmethod
    def get_state(self):
        """Return the state data of this interactable."""
        pass

    @abstractmethod
    def set_state(self, key, value):
        """Set a state value for this interactable."""
        pass
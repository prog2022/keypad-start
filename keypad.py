import tkinter as tk
from tkinter import ttk


#TODO fix the class declaration
class Keypad

    def __init__(self, parent, keynames=[], columns=1, **kwargs):
        #TODO call the superclass constructor with all args except
		# keynames and columns
        self.keynames = keynames
        self.init_components(columns)

    def init_components(self, columns):
        """Create a stretchable keypad of keys using the keynames list,
        starting with the first keynames elements at the top of keypad.
        Use as many rows as required by the keynames.
        """
        pass


if __name__ == '__main__':
    keys = list(iter('789456123 0.'))  # = ['7','8','9',...]

    root = tk.Tk()
    root.title("Keypad Demo")
    keypad = Keypad(root, keynames=keys, columns=3)
    keypad.pack(fill='both')
    root.mainloop()

import tkinter

DEFAULT_COLOUR = "#FF407D"

class Trivia_GUI:

    def __init__(self):
        
        self.window = tkinter.Tk()
        self.window.title("Trivia Game")
        
        self.window.config(padx=20, pady=20, bg=DEFAULT_COLOUR)
        
        
        self.window.mainloop()
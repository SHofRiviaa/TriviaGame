import tkinter

DEFAULT_COLOUR = "#FF407D"
CANVAS_COLOUR = "#5356FF"

class Trivia_GUI:

    def __init__(self):
        
        self.window = tkinter.Tk()
        self.window.title("Trivia Game")
        
        self.window.config(padx=20, pady=20, bg=DEFAULT_COLOUR)

        self.score_label = tkinter.Label(text="Score: 0", bg="white", fg=DEFAULT_COLOUR)
        self.score_label.grid(row=0, column=2)
        
        self.canvas = tkinter.Canvas(width=350, height=250, bg=CANVAS_COLOUR)
        self.question_test = self.canvas.create_text(150, 125, width=300, text="Question goes here", fill=DEFAULT_COLOUR, font=("Papyrus", 20, "italic"))

        self.canvas.grid(row=1, column=0, columnspan=3, pady=20)

        self.window.mainloop()


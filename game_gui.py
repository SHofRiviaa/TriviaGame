import tkinter
from PIL import Image, ImageTk
from trivia_controller import Trivia_Controller

DEFAULT_COLOUR = "#FF407D"
CANVAS_COLOUR = "#5356FF"

class Trivia_GUI:

    def __init__(self, trivia_controller: Trivia_Controller):
        self.trivia_controller = trivia_controller

        self.window = tkinter.Tk()
        self.window.title("Trivia Game")
        
        self.window.config(padx=20, pady=20, bg=DEFAULT_COLOUR)

        self.score_label = tkinter.Label(text="Score: 0", bg="white", fg=DEFAULT_COLOUR)
        self.score_label.grid(row=0, column=2)
        
        self.canvas = tkinter.Canvas(width=350, height=250, bg=CANVAS_COLOUR)
        self.question_test = self.canvas.create_text(150, 125, width=300, text="Question goes here", fill=DEFAULT_COLOUR, font=("Papyrus", 20, "italic"))

        self.canvas.grid(row=1, column=0, columnspan=3, pady=20)
        
        with Image.open("images\\thumbs_up.png") as img:
            img = img.resize((100, 100))
            thumbs_up_img = ImageTk.PhotoImage(img)

        thumbs_up_img = ImageTk.PhotoImage(img)
        self.thumbs_up_btn = tkinter.Button(image=thumbs_up_img, bg=DEFAULT_COLOUR,width=100, height=100)
        self.thumbs_up_btn.grid(row=2, column=0)
        
        with Image.open("images\\thumbs_down.png") as img:
            img = img.resize((100, 100))
            thumbs_down_img = ImageTk.PhotoImage(img)

        thumbs_down_img = ImageTk.PhotoImage(img)
        self.thumbs_down_btn = tkinter.Button(image=thumbs_down_img, bg=DEFAULT_COLOUR,width=100, height=100)
        self.thumbs_down_btn.grid(row=2, column=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.trivia_controller.still_has_questions():
            question = self.trivia_controller.next_question()
            self.canvas.itemconfig(self.question_test, text=question)
            self.score_label.config(text=f"Score: {self.trivia_controller.score}")
        else:
            self.canvas.itemconfig(self.question_test, text="You've reached the end of the quiz!")
            self.thumbs_up_btn.config(state="disabled")
            self.thumbs_down_btn.config(state="disabled")

    def thumbs_up_pressed(self):
        is_correct = self.trivia_controller.check_answer(True)
        self.give_feedback(is_correct)

    def thumbs_down_pressed(self):
        is_correct = self.trivia_controller.check_answer(False)
        self.give_feedback(is_correct)

    def give_feedback(self, is_correct):
        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)



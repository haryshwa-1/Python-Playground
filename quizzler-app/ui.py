from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
PADDING = 20
FONT = ("Arial", 20, "italic")
HEIGHT = 250
WIDTH = 300

class QuizInterface:
    def __init__(self, quiz_bank:QuizBrain):
        self.quiz = quiz_bank
        self.score = 0

        self.window = Tk()
        self.window.config(bg=THEME_COLOR, padx=PADDING, pady=PADDING)

        self.canvas = Canvas(height=HEIGHT, width=WIDTH, highlightthickness=0, bg="white")
        self.text = self.canvas.create_text(150, 125,width=280, text="hi",font=FONT,fill="black")
        self.canvas.grid(column= 0, row = 1, columnspan=2, pady=PADDING + PADDING, padx = PADDING)

        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")

        self.right = Button(image=true_img, command=lambda : self.correct("true"), padx=PADDING, pady=PADDING, bg=THEME_COLOR)
        self.right.grid(column=0,row=2)

        self.wrong = Button(image=false_img, command=lambda : self.correct("false"), padx=PADDING, pady= PADDING, bg= THEME_COLOR)
        self.wrong.grid(column=1, row=2)

        self.score_card = Label(text=f"Score: 0", font= FONT, bg=THEME_COLOR, fg="white")
        self.score_card.grid(column=1,row=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        q_text = self.quiz.next_question()
        if q_text is not False:
            self.canvas.itemconfig(self.text, text=q_text)
        else:
            self.canvas.itemconfig(self.text, text="You Completed the quiz!")
            self.right.config(state="disabled")
            self.wrong.config(state="disabled")

    def correct(self, ans):
        if self.quiz.check_answer(ans):
            self.score += 1
            self.score_card.config(text=f"Score: {self.score}")
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000 ,self.get_next_question)


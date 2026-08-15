from tkinter import * # type: ignore
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quizbrain: QuizBrain):
        self.quiz = quizbrain
        # self.Scorecount = 0
        self.window = Tk()
        self.window.title("Quizzier")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_lable = Label(
            text=f"Score : 0", font=("Arial", 10), bg=THEME_COLOR, fg="White"
        )
        self.score_lable.grid(row=1, column=2)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=290,
            text="Some Question ",
            font=("Arial", 17, "italic"),
            fill=THEME_COLOR,
        )
        self.canvas.grid(row=2, columnspan=3, pady=50)

        truepng = PhotoImage(file="day34/images/true.png")
        falsepng = PhotoImage(file="day34/images/false.png")
        self.true = Button(
            image=truepng, highlightthickness=0, command=self.checkfortrue
        )
        self.true.grid(row=3, column=1, padx=20)
        self.false = Button(
            image=falsepng, highlightthickness=0, command=self.checkforfalse
        )
        self.false.grid(row=3, column=2, padx=20)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_lable.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=q_text)
            
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quizz.")
            self.true.config(state="disabled")
            self.false.config(state="disabled")
    def checkfortrue(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def checkforfalse(self):
        self.is_right = self.quiz.check_answer("False")
        self.give_feedback(self.is_right)

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
    
from tkinter import *

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class Quizinterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        # Score Label
        self.score_label = Label(text='Score: 0', bg=THEME_COLOR, fg="white", font=("Arial", 11, "bold"))
        self.score_label.grid(column=1, row=0, sticky="e", padx=10, pady=10)

        # Question Canvas
        self.canvas = Canvas(width=300, height=250, bg='white')
        self.text = self.canvas.create_text(150, 125, text='', font=('Arial', 12, 'italic'), width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)

        #Images
        try:
            self.tick_img = PhotoImage(file='images/true.png')
            self.cross_img = PhotoImage(file='images/false.png')
        except TclError:
            print("Error: Image files not found!")

        # True Button
        self.true_button = Button(image=self.tick_img, highlightthickness=0, highlightbackground=THEME_COLOR, command=self.true)
        self.true_button.grid(column=0, row=2, pady=20, padx=20)

        # False Button
        self.false_button = Button(image=self.cross_img, highlightthickness=0, highlightbackground=THEME_COLOR,command=self.false)
        self.false_button.grid(column=1, row=2, pady=20, padx=20)

        self.next_question()
        self.window.mainloop()

    def next_question(self):
        """Fetch the next question and display it on the canvas."""
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=q_text)
        else:
            self.canvas.itemconfig(self.text, text="Game Over!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true(self):
        """Handle True button click."""
        self.give_feedback(self.quiz.check_answer("True"))

    def false(self):
        """Handle False button click."""
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        """Change background color for feedback and update score."""
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.window.after(1000, self.next_question)

THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain
class QuizInterface:
    def __init__(self,quizBrain:QuizBrain):
        self.quiz = quizBrain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)
        self.score = 0
        self.scoreLabel = Label(text=f"Score: {self.score}",bg=THEME_COLOR,fg="white",font=("Arial", 12, "bold"))
        self.scoreLabel.grid(column=1,row=0)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.questionText = self.canvas.create_text(
            150,
            125,
            text="some Text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"),
            width=280
        )
        self.canvas.grid(column = 0,row=1,columnspan=2,pady=50)

        self.true = PhotoImage(file="images/true.png")
        self.trueBtn = Button(image=self.true, highlightthickness=0,command=self.truePressed)
        self.false = PhotoImage(file="images/false.png")
        self.falseBtn = Button(image=self.false, highlightthickness=0,command=self.falsePressed)
        self.trueBtn.grid(column=0,row=2)
        self.falseBtn.grid(column=1,row=2)
        self.getNextQuestion()

        self.window.mainloop()

    def getNextQuestion(self):
        if self.quiz.still_has_questions():
            qText = self.quiz.next_question()
            self.canvas.itemconfig(self.questionText, text=qText)
            self.canvas.config(bg="white")
        else:
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.questionText, text=f"You have reached the end of the quiz! You scored {self.score}/10 ")
            self.trueBtn.config(state="disabled")
            self.falseBtn.config(state="disabled")



    def truePressed(self):
        self.giveFeedback(self.quiz.check_answer("True"))


    def falsePressed(self):
        self.giveFeedback(self.quiz.check_answer("False"))

    def giveFeedback(self,isRight):
        if isRight:
            self.canvas.config(bg="green")
            self.score +=1
            self.scoreLabel.config(text=f"Score: {self.score}")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.getNextQuestion)


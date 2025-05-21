from tkinter import *
from random import randint, choice

# Create the main window
root = Tk()
root.geometry("500x500")
root.title("🧮 Maths Quiz for Beginners")
root.config(bg="#F0F8FF")  # Light background for soft look

# Variables for storing quiz data
question = StringVar()
answer = StringVar()
givenAnswer = StringVar()
score = IntVar()
questionCount = IntVar()

# ------------------- UI ELEMENTS -------------------

# Heading
headingLabel = Label(root, text="🎓 Maths Quiz Game", font=('Helvetica', 22, 'bold'), bg="#F0F8FF", fg="#2C3E50")
headingLabel.pack(pady=20)

# Question display
questionLabel = Label(root, text="", font=('Helvetica', 18), bg="#F0F8FF", fg="#34495E")
questionLabel.pack(pady=10)

# User answer input
answerEntry = Entry(root, textvariable=givenAnswer, font=('Helvetica', 16), justify='center')
answerEntry.pack(pady=10)

# Submit and Restart buttons
buttonFrame = Frame(root, bg="#F0F8FF")
buttonFrame.pack(pady=10)

submitButton = Button(buttonFrame, text="✅ Submit", font=('Helvetica', 14), bg="#58D68D", fg="white", command=lambda: checkAnswer())
submitButton.grid(row=0, column=0, padx=10)

restartButton = Button(buttonFrame, text="🔄 Restart", font=('Helvetica', 14), bg="#5DADE2", fg="white", command=lambda: restartQuiz())
restartButton.grid(row=0, column=1, padx=10)

# Result
resultLabel = Label(root, text="Result", font=('Helvetica', 16), bg="#F0F8FF", fg="#8E44AD")
resultLabel.pack(pady=10)

# Score and progress
scoreLabel = Label(root, text="Score: 0", font=('Helvetica', 16), bg="#F0F8FF", fg="#2C3E50")
scoreLabel.pack(pady=5)

progressLabel = Label(root, text="Question: 0/10", font=('Helvetica', 16), bg="#F0F8FF", fg="#2C3E50")
progressLabel.pack(pady=5)

# ------------------- FUNCTIONS -------------------

def generateQuestion():
    if questionCount.get() >= 10:
        questionLabel.config(text="🎉 Quiz Completed!")
        return

    number1 = randint(1, 10)
    number2 = randint(1, 10)
    operator = choice(['+', '-', '*', '//'])  # Basic operators

    question.set(f"{number1} {operator} {number2}")
    answer.set(str(eval(question.get())))
    questionLabel.config(text=question.get())

def checkAnswer():
    if questionCount.get() < 10:
        if givenAnswer.get() == answer.get():
            resultLabel.config(text="✅ Correct!", fg="green")
            score.set(score.get() + 1)
        else:
            resultLabel.config(text=f"❌ Incorrect! Ans: {answer.get()}", fg="red")

        scoreLabel.config(text=f"Score: {score.get()}")
        questionCount.set(questionCount.get() + 1)
        progressLabel.config(text=f"Question: {questionCount.get()}/10")
        givenAnswer.set("")
        generateQuestion()

def restartQuiz():
    score.set(0)
    questionCount.set(0)
    givenAnswer.set("")
    resultLabel.config(text="Result", fg="#8E44AD")
    scoreLabel.config(text="Score: 0")
    progressLabel.config(text="Question: 0/10")
    generateQuestion()

# ------------------- START -------------------
generateQuestion()
root.mainloop()

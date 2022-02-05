# Qestion
from functools import total_ordering


class Question:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer
    def checkAnswer(self , answer):
        return self.answer == answer

# Quiz
class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionsIndex = 0

    def getQuestion(self):
        return self.questions[quiz.questionsIndex]
    
    def displayQuestion(self):
        question = self.getQuestion()
        print(f"Question {self.questionsIndex + 1} : {question.text} ")

        for q in question.choices:
            print("-"+ q)
        
        answer = input("Answer: ")
        self.guess(answer)
        self.loadQuestion()

    def guess(self, answer):
        question = self.getQuestion()
        
        if question.checkAnswer(answer):
            self.score += 1
        self.questionsIndex += 1

    
    def loadQuestion(self):
        if len(self.questions) == self.questionsIndex:
            self.showScore()
        else: 
            self.displayProgress()
            self.displayQuestion()
        
    def showScore(self):
        print("Your score is :",self.score)

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionsIndex + 1

        if questionNumber > totalQuestion:
            print("Your quiz finished.")
        else:
            print(f"Question {questionNumber} of {totalQuestion}".center(100,"*"))

q1 = Question("Which programing language is best ?", ["c#" , "python" , "java" , "javascript" ], "python")
q2 = Question("Which programing language is most popular ?", [ "python" , "java" ,"c#" , "javascript" ], "python")
q3 = Question("Which is the most profitable programming language?", ["c#" , "java" , "javascript" , "python" ], "python")
questions = [q1,q2,q3]

quiz = Quiz(questions)

quiz.loadQuestion()

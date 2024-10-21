from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questionBank = []

for dict in question_data:
    questionBank.append(Question(dict["text"], dict["answer"]))

quiz = QuizBrain(questionBank)

quiz.next_question()
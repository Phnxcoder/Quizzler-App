import requests
from question_model import Question
from quiz_brain import QuizBrain
from ui import Quizinterface

# Fetch quiz data
api = requests.get('https://opentdb.com/api.php?amount=10&type=boolean')
data = api.json()
question_data = data['results']

# Convert data into Question objects
question_bank = [Question(q["question"], q["correct_answer"]) for q in question_data]

# Start Quiz
quiz = QuizBrain(question_bank)
quiz_ui = Quizinterface(quiz)

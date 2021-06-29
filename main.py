from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for x in range(len(question_data)):
    question = Question(question_data[x]['question'],
                        question_data[x]['correct_answer'])
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've Completed the quiz!")

print(f"Your final score is {quiz.user_score}/{quiz.question_number} ")
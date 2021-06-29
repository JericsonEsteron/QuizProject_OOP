class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.user_score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.question_number += 1
        answer = input("Q.{0}: {1}. (True/false)?:"
                       .format(self.question_number,
                               self.question_list[self.question_number - 1].text))
        self.check_answer(answer, self.question_list[self.question_number - 1].answer)

    def check_answer(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            print("You for it right!")
            self.score(True)
        else:
            print("That's Wrong.")
            self.score(False)
        print(f"The Correct answer is {correct_answer}")
        print()

    def score(self, score_increased):
        if score_increased:
            self.user_score += 1
        print(f"Your current score is: {self.user_score}/{self.question_number}")

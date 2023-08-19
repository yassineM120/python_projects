

class QuizBrain:
    def __init__(self, q_questions_list):
        self.question_number = 0
        self.questions_list = q_questions_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        next_question = self.question_number + 1
        user_answer = input(f"Q.{next_question}: {current_question.text} (True/False)")
        self.question_number += 1
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your currect score is {self.score}/{self.question_number}\n")




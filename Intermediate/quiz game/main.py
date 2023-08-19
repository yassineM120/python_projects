from data import question_data
from quiz_brain import QuizBrain


class Quiz:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


question_bank = []
for item in question_data:
    question_bank.append(Quiz(item["question"], item["correct_answer"]))


new_brain_quiz = QuizBrain(question_bank)
while new_brain_quiz.still_has_questions():
    new_brain_quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was {new_brain_quiz.score}/{new_brain_quiz.question_number}")


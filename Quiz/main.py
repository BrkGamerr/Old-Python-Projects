from classes import Question, QuizBrain
from data import question_data

# Creates new objects from Question class, and adds them to the question_bank
question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the Quiz!")
print(f"Your final score: {quiz.score} / {quiz.question_number}")

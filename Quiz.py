"""
Quiz App
Questions stored as objects, tracks the user's score.
"""

class Question:
    def __init__(self, text, choices, correct_answer):
        self.text = text
        self.choices = choices  # list like ["A) ...", "B) ...", ...]
        self.correct_answer = correct_answer.upper()  # e.g. "A"

    def ask(self):
        print(self.text)
        for choice in self.choices:
            print(choice)
        answer = input("Your answer: ").strip().upper()
        return answer == self.correct_answer


class Quiz:
    def __init__(self):
        self.questions = []
        self.score = 0

    def add_question(self, question):
        self.questions.append(question)

    def run(self):
        for i, q in enumerate(self.questions, start=1):
            print(f"\nQuestion {i}:")
            if q.ask():
                print("Correct!")
                self.score += 1
            else:
                print(f"Wrong. Correct answer: {q.correct_answer}")

        print(f"\nFinal Score: {self.score}/{len(self.questions)}")


def main():
    quiz = Quiz()

    quiz.add_question(Question(
        "What is the capital of Pakistan?",
        ["A) Karachi", "B) Lahore", "C) Islamabad", "D) Peshawar"],
        "C"
    ))
    quiz.add_question(Question(
        "Which language is this code written in?",
        ["A) Java", "B) Python", "C) C++", "D) JavaScript"],
        "B"
    ))
    quiz.add_question(Question(
        "2 + 2 * 2 = ?",
        ["A) 8", "B) 6", "C) 4", "D) 2"],
        "B"
    ))
    quiz.add_question(Question(
        "In your first day of School which word become in your mind?",
        ["A) Become a doctor","B) Become an engineer","C) A Police man","D) A Business man"],"B"
    ))
    quiz.run()

if __name__ == "__main__":
    main()

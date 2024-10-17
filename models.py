class Question:
    def __init__(self, category, question, correct_answer, wrong_answer):
        self.category = category
        self.question = question
        self.correct_answer = correct_answer
        self.wrong_answer = wrong_answer

    def __str__(self):
        return f"{self.question} (True/False)"

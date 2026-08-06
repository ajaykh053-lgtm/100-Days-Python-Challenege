class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def next_question(self):
        next_q = True
        while next_q:
            self.current_question = self.question_list[self.question_number]
            self.correct_answer = self.current_question.answer.lower()
            self.question_number += 1
            self.user_answer = (
                input(
                    f"Q.{self.question_number}: {self.current_question.text} (True/False)? : "
                )
                .lower()
                .strip()
            )
            if self.user_answer == self.correct_answer:
                print("You got it right!")
                self.score += 1
            else:
                print("That's wrong.")
                print(f"The correct answer was: {self.correct_answer}.")
            if self.question_number == len(self.question_list):
                print("You've completed the quiz")
                print(f"Your final score was : {self.score}/{self.question_number}")
                next_q = False

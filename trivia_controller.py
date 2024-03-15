import html

class Trivia_Controller:

    def __init__(self, questions_list):
        
        self.question_number = 0
        self.score = 0
        self.current_question = None
        self.questions_list = questions_list
    
    def still_has_questions(self):
        if self.question_number < len(self.questions_list):
            return True
        else:
            return False

    def next_question(self):
        self.current_question = self.questions_list[self.question_number]
        self.question_number += 1
        question = html.unescape(self.current_question.text)
        return question

    def check_answer(self, user_answer):
        
        if user_answer == self.current_question.answer:
            self.score += 1
            return True
        else:
            return False
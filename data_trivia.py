import requests
from question_model import Question

TRIVIA_API_URL = "https://opentdb.com/api.php"

class Data_Trivia_Builder:

    def __init__(self, num_qs, category, difficulty):
        
        self.setup_parameter(num_qs, category, difficulty)

    def setup_parameter(self, num_qs, category, difficulty):

        self.num_qs = num_qs
        self.category = category
        self.difficulty = difficulty
        self.type = "boolean"

        self.parameters = {
            "amount": self.num_qs,
            "category": self.category,
            "difficulty": self.difficulty,
            "type": self.type
        }

    def get_trivia_questions(self):

        response = requests.get(TRIVIA_API_URL, params = self.parameters)
        response.raise_for_status()
        data = response.json()
        trivia_data = data['results']

        return self.format_trivia_questions(trivia_data)
    
    def format_trivia_questions(self, trivia_data):
        
        formatted_trivia_data = []
        
        for question in trivia_data:
            question_text = question['question']
            question_answer = question['correct_answer']
            formatted_trivia_data.append(Question(question_text, question_answer))
        
        return formatted_trivia_data




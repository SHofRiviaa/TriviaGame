import requests

TRIVIA_API_URL = "https://opentdb.com/api.php"

class Data_Trivia_Builder:

    def __init__(self, num_qs, category, difficulty, type):
        
        self.setup_parameter(num_qs, category, difficulty, type)

    def setup_parameter(self, num_qs, category, difficulty, type):

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

        return trivia_data



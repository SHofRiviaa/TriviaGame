class UserOptions:

    def __init__(self):

        self.user_options = {}

    def get_user_options_values(self):
        print("Welcome to the Trivia Game!")

        self.get_number_of_questions()
        self.get_category()
        self.get_difficulty()
        self.get_trivia_type()
        
    def get_number_of_questions(self):
        while True:
            try:
                num_qs = int(input("How many questions would you like? [Between 1 and 50] "))
                
                if num_qs > 0 and num_qs <= 50:
                    self.user_options['num_qs'] = num_qs
                    break
                else:
                    print("Please enter a number greater than 0")
            except ValueError:
                print("Please enter a number between 1 and 50")

    def get_category(self):
        while True:
            try:
                category = int(input("Select a category: [Between 9 and 19] \n" +
                                     "where 9 = General Knowledge, 10 = Books, " +
                                     "11 = Film, 12 = Music, 13 = Musicals & Theatres, " +
                                     "14 = Television, 15 = Video Games, 16 = Board Games, " +
                                     "17 = Science & Nature, 18 = Computers, 19 = Mathematics"))
                
                if category >= 9 and category <= 19:
                    self.user_options['category'] = category
                    break
                else:
                    print("Please enter a number greater than 9 and less than 50")
            except ValueError:
                print("Please enter a number")

    def get_difficulty(self):
        while True:
            difficulty = input("Select a difficulty: [easy, medium, hard] ")
            if difficulty in ['easy', 'medium', 'hard']:
                self.user_options['difficulty'] = difficulty
                break
            else:
                print("Please enter easy, medium or hard")
    
    def get_trivia_type(self):
        while True:
            type = input("Select a type: [multiple, boolean] ")
            if type in ['multiple', 'boolean']:
                self.user_options['type'] = type
                break
            else:
                print("Please enter multiple or boolean")

    def get_user_options(self):
        return self.user_options

    


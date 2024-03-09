class UserOptions:

    def __init__(self):

        self.user_options = {}

    def get_user_options(self):
        pass
        
    
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
                
                if category > 9 and category <= 50:
                    self.user_options['category'] = category
                    break
                else:
                    print("Please enter a number greater than 9 and less than 50")
            except ValueError:
                print("Please enter a number")

    


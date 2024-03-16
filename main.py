from game_gui import Trivia_GUI
from user_options import UserOptions
from data_trivia import Data_Trivia_Builder
from trivia_controller import Trivia_Controller


def main():

    user_options = UserOptions()
    user_options.get_user_options_values()
    data_trivia = Data_Trivia_Builder(user_options.user_options['num_qs'], 
                                      user_options.user_options['category'], 
                                      user_options.user_options['difficulty'])
    
    trivia_data = data_trivia.get_trivia_questions()
    trivia_controller = Trivia_Controller(trivia_data)

    game = Trivia_GUI(trivia_controller)
    

if __name__ == "__main__":
    main()
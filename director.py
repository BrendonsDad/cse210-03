from platform import libc_ver
from word import Word
from display import Display
from score import Score

class Director:
    
    def __init__(self, lives = 4):
        #stuff in there
        
        # self.display = Display()
        self._lives = lives

    def start_game(self):
        difficulty = input('Please select a difficulty: [E]asy, [M]edium, [H]ard: ')
        if difficulty.lower() == 'e':
            first_display = ['_',' _',' _',' _',' _']
            difficulty = 'e'
        elif difficulty.lower() == 'm':
            first_display = ['_',' _',' _',' _',' _',' _',' _']
            difficulty = 'm'
        elif difficulty.lower() == 'h':
            first_display = ['_',' _',' _',' _',' _',' _',' _',' _',' _']
            difficulty = 'h'
        else:
            print("Becuase you can't follow simple instructions, we'll put \n you on easy...")
            first_display = '_ _ _ _ _'
            difficulty = 'e'

        word = Word()
        random_word = word.get_word(difficulty)
        # player = Director(lives=4)
        lives = self._lives
        # lives = player.lives
        play = ''
        empty_spots = 0
        

        while play != 'done':
            for elem in first_display:
                print(elem, end=' ')
            print()
            self.display(lives)
            # self.guess(lives, random_word)
            letter_guess = input("Guess a letter from a - z: ")
            myscore = Score(lives, letter_guess, random_word)
            lives = myscore.total_score()
            first_display = myscore.return_progress(first_display, letter_guess)
            for i in range(len(first_display)):
                if first_display[i] == ' _' or first_display[i] == '_':
                    empty_spots += 1
                else:
                    empty_spots += 0
            if empty_spots == 0:
                for elem in first_display:
                    print(elem, end=' ')
                play = 'done'
                
            if lives == 0:
                play = 'done'

                
            
            empty_spots = 0


            if lives == 0:
                self.display(lives)
                print()
                print('Game Over')


    # def guess(self, lives, random_word):
    #     ##Asks the user for their guess
    #     letter_guess = input("Guess a letter from a - z: ")
    #     #Makes a new instance of score
    #     myscore = Score(lives, letter_guess, random_word)
    #     myscore.total_score()
    #     myscore.letter_index()
        

    def display(self, lives):
        screen = Display(lives)
        screen.display_screen(lives)







                                                                                                                                                                                                                                            

        
        


from word import Word
from display import Display
from score import Score

class Director:
    
    def __init__(self, word, play, lives):
        #stuff in there
        
        self.word = word
        # self.display = Display()
        self.lives = lives

    def start_game(self):
        difficulty = input('Please select a difficulty: [E]asy, [M]edium, [H]ard: ')
        if difficulty.lower() == 'e':
            first_display = '_ _ _ _ _'
            difficulty = 'e'
        elif difficulty.lower() == 'm':
            first_display = '_ _ _ _ _ _ _'
            difficulty = 'm'
        elif difficulty.lower() == 'h':
            first_display = '_ _ _ _ _ _ _ _ _'
            difficulty = 'h'
        else:
            print("Becuase you can't follow simple instructions, we'll put \n you on easy...")
            first_display = '_ _ _ _ _'
            difficulty = 'e'
        print(first_display)

        word = Word(difficulty= difficulty)
        random_word = word.word
        player = Director(word=word, lives=4)

        while player.lives > 0:
            self.display(player.lives, )
            self.guess(player.lives, random_word)


    def guess(lives, random_word):
        ##Asks the user for their guess
        letter_guess = input("Guess a letter from a - z: ")
        #Makes a new instance of score
        myscore = Score(lives, letter_guess, random_word)
        lives = myscore.calculate_lives(myscore.lives)

    def display(lives, lines):
        screen = Display(lives, lines)
        screen.showscreen()







                                                                                                                                                                                                                                            

        
        


import json
import random






class Word:
    '''A code template for the program to access an external file and randomly
     select a word to use for the game.
    Stereotype:
        Information Holder
    Attributes:
       word (string): The word randomly selected that the player tries to guess.
    '''
    def __init__(self):
        self.list = {
  'word_list_easy': [
    'which',
    'there',
    'their',
    'about',
    'would',
    'these',
    'other',
    'words',
    'could',
    'write',
    'first',
    'water',
    'after',
    'where',
    'right',
    'think',
    'three',
    'years',
    'place',
    'sound',
    'great',
    'again',
    'still',
    'every',
    'small',
    'found',
    'those',
    'never',
    'under',
    'might',
    'while',
    'house',
    'world',
    'below',
    'asked',
    'going',
    'large',
    'until',
    'along',
    'shall',
    'being',
    'often',
    'earth',
    'began',
    'since',
    'study'
  ],
  'word_list_medium': [
    'ability',
    'absence',
    'academy',
    'account',
    'accused',
    'achieve',
    'acquire',
    'address',
    'advance',
    'adverse',
    'advised',
    'adviser',
    'against',
    'airline',
    'airport',
    'alcohol',
    'alleged',
    'already',
    'analyst',
    'ancient',
    'another',
    'anxiety',
    'anxious',
    'anybody',
    'applied',
    'arrange',
    'arrival',
    'article',
    'assault',
    'assumed',
    'assured',
    'attempt',
    'attract',
    'auction',
    'average',
    'backing',
    'balance',
    'banking',
    'barrier',
    'battery',
    'bearing',
    'beating',
    'because',
    'bedroom',
    'believe',
    'beneath',
    'benefit',
    'besides',
    'between',
    'billion',
    'binding'
  ],
  'word_list_hard': [
    'abhorrent',
    'abilities',
    'abrasions',
    'acquitted',
    'adulthood',
    'bleachers',
    'drizzling',
    'embezzles',
    'expertise',
    'hijackers',
    'lifehacks',
    'newlyweds',
    'orthodoxy',
    'paralyzed',
    'recognize',
    'reflexive',
    'technique',
    'unplugged',
    'whichever',
    'yellowish'
  ]
}
    def get_word(self, difficulty):
        list = self.list
        easy_list = list['word_list_easy']
        med_list = list['word_list_medium']
        hard_list = list['word_list_hard']
        if difficulty == 'e':
            self.word = random.choice(easy_list)
        elif difficulty == 'm':
            self.word = random.choice(med_list)
        elif difficulty == 'h':
            self.word = random.choice(hard_list)
        else:
            print('Invalid difficulty input assigned difficulty easy.')
            self.word = easy_list[random.randint(0, 45)]
        return self.word
# class Word:

    # def __init__(self, difficulty):
    #     with open("word_bank.json","r") as file:
    #         word_bank = json.load(file)
    #         input_from_file = file.read()
    #     json.object = json.load(input_from_file)
    #     easy_list = json.object["word_list_easy"]
    #     medium_list = json.object["word_list_medium"]
    #     hard_list = json.object["word_list_hard"]

#         if difficulty == "e":
#             self.word = easy_list(random.randint(0,50))
#         elif difficulty == "m":
#             self.word = medium_list(random.randint(51,102))
#         elif difficulty == "h":
#             self.word = hard_list(random.randint(103,125)) 
#         return self.word

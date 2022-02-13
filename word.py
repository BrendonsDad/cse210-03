import json
import random

class Word:

    def __init__(self, difficulty):
        with open("word_bank.json","r") as file:
            word_bank = json.load(file)
            input_from_file = file.read()
        json.object = json.load(input_from_file)
        easy_list = json.object["word_list_easy"]
        medium_list = json.object["word_list_medium"]
        hard_list = json.object["word_list_hard"]

        if difficulty == "e":
            self.word = easy_list(random.randint(0,50))
        elif difficulty == "m":
            self.word = medium_list(random.randint(51,102))
        elif difficulty == "h":
            self.word = hard_list(random.randint(103,125)) 
        return self.word

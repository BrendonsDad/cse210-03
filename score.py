from word import Word


class Score:
    def __init__(self,score,letter,word):
        self._score = score
        self.current_score = 4
        self.sub_lives = -1
        self.letter = letter
        self.word = word
        self.index = []

    def total_score(self):
        if self.check_letter():
            return self.current_score
        else:
            return self.sub_lives + self.current_score 


    ## check if a letter is in the word class
    def check_letter(self):
        for i in self.word:
           if i == self.letter:
               return True
        return False

    ## tell which index of the letters
    def letter_index(self):
        for i in range(len(self.word)):
            if self.word[i] == self.letter:
                self.index.append(i)
        return self.index
from word import Word


class Score:
    def __init__(self,score,letter,word):
        self._score = score
        self.current_score = score
        self.sub_lives = -1
        self.letter = letter
        self.word = word
        self.index = []

    def total_score(self):
        if self.check_letter():
            return self.current_score
        else:
            return self.sub_lives + self.current_score 


    def check_letter(self):
        for i in self.word:
           if i == self.letter:
               return True
        return False

    def letter_index(self):
        for i in range(len(self.word)):
            if self.word[i] == self.letter:
                self.index.append(i)
        return self.index

    def return_progress(self, progress, letter):
        for i in range(len(self.word)):
            if self.word[i] == letter:
                progress[i] = letter
        return progress


        # check a letter to see if its in word class
        # pass in get the letter and the word
        # which index of the letter
        # guess is connected to score
        # score is connected to display

        # 5 lives

        # if guess is correct the letter is revealed.

        #if guess is incorrect, a line on a player parachute is cut.

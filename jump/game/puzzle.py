import random

class Puzzle:

    #Makes a list of four potential answers and chooses one of them.
    def __init__(self):
        self.possibleWords= ["aide", "bath", "care", "doll"]
        self.chosenWord = random.choice(self.possibleWords)

        #Hint that creates single underlines for unguessed letters.
        self._wordHint = '_'*4
    
    #Changes an underline to a correctly guessed letter
    def Puzzle_wordAnswer(self, _wordAnswer):
        i = 0
        if _wordAnswer in self.chosenWord:
            while self.chosenWord.find(_wordAnswer, i) != -1:
                i = self.chosenWord.find(_wordAnswer, i)
                self._wordHint = self._wordHint[:i] + _wordAnswer + self._wordHint[i + 1:]
                i += 1

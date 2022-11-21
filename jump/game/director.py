from game.terminal_service import TerminalService
from game.parachute import Parachute
from game.puzzle import Puzzle


class Director:

    def __init__(self):

        self._jumpPara = Parachute()
        self._wordPuzzle = Puzzle()
        self._isPlaying = True
        self._terminalService = TerminalService()
        
    def Start(self):

        while self._isPlaying:
            self.Inputs()
            self.Updates()
            self.Outputs()

    def Inputs(self):

        #Prompts the player to guess a letter
        print(self._wordPuzzle._wordHint)
        _answer = self._terminalService.read_word("\nGuess a letter [a-z]: ")
        
        #Determines if the player is right or wrong.
        if _answer in self._wordPuzzle.chosenWord:
            print("Correct!")
        else:
            print("Wrong!")
            self._jumpPara._linesLeft -= 1 #Reduces a line from the jumper's parachute.
        self._wordPuzzle.Puzzle_wordAnswer(_answer)

     
    def Updates(self):

        #Updates the jumper drawing based on how many lives the player has left.
        self._jumpPara.ParachuteLines()
        print(self._jumpPara._jumperDraw)
        
    def Outputs(self):       

        #Game Over Conditions

        #Player is out lives.
        if self._jumpPara._linesLeft == 0:
            print("The jumper has fallen.")
            print(f"The word was {self._wordPuzzle.chosenWord}")
            print()
            print('Game Over.')
            self._isPlaying = False
        
        #Player guessed the word.
        if self._wordPuzzle.chosenWord == self._wordPuzzle._wordHint:
            print('You win!')
            print("Thank you for playing!")
            self._isPlaying = False
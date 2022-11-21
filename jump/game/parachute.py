class Parachute:

    def __init__(self):

        #Player has five lives and the parachute has five lines
        self._linesLeft = 5

        #Shows a full parachute as the game begins
        self._jumperDraw = ("\n"
            "		  ___\n"
            "		 /   \ \n"
            "		/_____\ \n"
            "		\     / \n"
            "		 \   / \n"
            "		   O \n"
            "		  /|\ \n"
            "		  / \ \n"
            "		^^^^^^^^\n"
        )
        print(self._jumperDraw)

    #Parachute Lines depending on how many the player has left.
    def ParachuteLines(self):
        if self._linesLeft == 5:
            self._jumperDraw = ("\n"
            "		  ___ \n"
            "		 /   \ \n"
            "		/_____\ \n"
            "		\     / \n"
            "		 \   / \n"
            "		   O \n"
            "		  /|\ \n"
            "		  / \ \n"
            "		^^^^^^^^\n"
            )

        elif self._linesLeft == 4:
            self._jumperDraw = ("\n"
            "		 /   \ \n"
            "		/_____\ \n"
            "		\     / \n"
            "		 \   / \n"
            "		   O \n"
            "		  /|\ \n"
            "		  / \ \n"
            "		^^^^^^^^\n"
            )

        elif self._linesLeft == 3:
           self._jumperDraw = ("\n"
            "		/_____\ \n"
            "		\     / \n"
            "		 \   / \n"
            "		   O \n"
            "		  /|\ \n"
            "		  / \ \n"
            "		^^^^^^^^\n"
            )

        elif self._linesLeft == 2:
            self._jumperDraw = ("\n"
            "		\     / \n"
            "		 \   / \n"
            "		   O \n"
            "		  /|\ \n"
            "		  / \ \n"
            "		^^^^^^^^\n"
             )

        elif self._linesLeft == 1:
            self._jumperDraw = ("\n"
            "		 \   / \n"
            "		   O \n"
            "		  /|\ \n"
            "		  / \ \n"
            "		^^^^^^^^\n"
             )


        elif self._linesLeft == 0:
            self._jumperDraw = ("\n"
            "		   x\n"
            "		  /|\ \n"
            "		  / \ \n"
            "		^^^^^^^^\n"
             )
            return self._jumperDraw
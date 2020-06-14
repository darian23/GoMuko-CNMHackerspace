import Game
class GoMokuConsole(object):

    """Console UI to interact with gomoku Game() engine object"""


    def __init__(self):
        self.game = Game.Game()

    def drawBoard(self):

        """Draw the game board on the console with B, W and . representing
           black pieces, white pieces, and empty spaces respectively"""

        # Merge the two board representations so that black pieces are 1, white is -1, empty is 0
        board = self.game.BBoard - self.game.WBoard
        print()
        for row in board:
            for col in row:
                if col == 1:
                    print("B", end="")
                elif col == -1:
                    print("W", end="")
                elif col == 0:
                    print(".", end="")
                else:
                    print("?", end="") # should not happen unless boards are corrupted
            print()

    def placePiece(self, x, y):
        """Place piece of current player in column x of row y"""
        self.game.place_piece(x, y)

    def getMove(self):
        """Prompt current player for x and y coordinate to place a piece"""
        player = self.game.player

        # TODO DR method to express player as a string should be added to Game
        if player == self.game.BLACK:
            P = "Black"
        else:
            P = "White"
        print("\nMove {0} ({1})".format(self.game.move, P))
        x = int(input("X: "))
        y = int(input("Y: "))
        self.placePiece(y,x)


# TODO DR I suppose what we really need is a PlayGame() method
if __name__ == "__main__":
    g = GoMokuConsole()
    gameloop = True
    while gameloop:
        g.drawBoard()
        g.getMove()

        # TODO DR if the game is a win for one player or a draw the game should end
        g.game.check_win()









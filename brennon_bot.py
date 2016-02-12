# Tic Tac Toe Bots - tiy extra credit *= 0
import sys
import random


class Game:

    def __init__(self):
        self.get_inputs()
        temp_board = [list(row) for row in self.board]
        print("DEBUG temp_board", temp_board, file=sys.stderr)
        empty = "_"
        valid_moves = [(i, j) for j in range(3) for i in range(3) if temp_board[i][j] == empty]
        print("DEBUG valid moves", valid_moves, file=sys.stderr)
        locations = {
                "center": (1, 1),
                "corners": [(0, 0), (0, 2), (2, 0), (2, 2)],
                "sides": [(0, 1), (1, 0), (1, 2), (2, 1)]
            }
        move = ()
        if locations["center"] in valid_moves:
            move = locations["center"]
        else:
            valid_move = False
            while not valid_move:
                move = random.choice(valid_moves)
                if move in locations["corners"]:
                    valid_move = True
                elif len(valid_moves) <= 4:
                    move = random.choice(valid_moves)
                    valid_move = True

        print("{} {}".format(move[0], move[1]))

    def get_inputs(self):
        self.me = input()
        if self.me == "X":
            self.you = "O"
        else:
            self.you = "X"

        row_one = input()
        row_two = input()
        row_three = input()
        self.board = self.create_board(row_one, row_two, row_three)

    def create_board(self, row_one, row_two, row_three):
        return [row_one, row_two, row_three]

game = Game()

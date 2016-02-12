# Tic Tac Toe Bots - tiy extra credit *= 0
import random


class Game:

    def __init__(self):
        self.get_inputs()
        temp_board = [list(row) for row in self.board]

        move = ()
        for row in temp_board:
            for elem in row:
                if elem != self.me and elem != self.you:
                    move = (temp_board.index(row), row.index(elem))
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

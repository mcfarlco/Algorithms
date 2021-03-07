# Author: Corey McFarland
# Date: 03/08/2021
# Desc: Portfolio assignment.

import numpy
import random
import os


class ImmovableTile(Exception):
    pass


class InvalidTile(Exception):
    pass


class Puzzle:

    """
    This represents the current board and tile positions of the n-Puzzle
    """

    def __init__(self, size=8, pregen=None):

        """
        Function to initialize the board
        """

        self.board = []
        self.n = size
        self.dim = int(numpy.sqrt(size + 1))
        self.moves = []

        # Check if user provided a pre-made board
        if pregen is not None:
            if len(pregen) == self.dim:
                if len(pregen[0]) == self.dim:
                    self.board = pregen

        # Create empty board if not
        else:
            for columns in range(self.dim):

                row = []

                for rows in range(self.dim):
                    row.append(None)

                self.board.append(row)

        return

    def output_board(self):
        """
        Function to output the current board state
        """

        print("   Board")
        print("=============")

        for rows in self.board:

                row = ""

                if self.dim < 5:
                    for s in range(5 - self.dim):
                        row += " "

                row += "| "
                for cols in rows:
                    if cols is None:
                        row += "  "

                    else:
                        row += str(cols) + " "

                row += "|"
                print(row)

        print("=============")

        return

    def gen_board(self):

        """
        Function to randomly generate tiles on the board
        """

        # Create random order of tiles
        num_order = []

        while len(num_order) != self.n + 1:

            num = random.randint(1, self.n + 1)

            if num in num_order:
                continue

            else:
                num_order.append(num)

        # Insert tiles into the board
        for row_i in range(self.dim):
            for col_i in range(self.dim):
                if len(num_order) == 0:
                    continue

                num = num_order.pop(0)

                if num > self.n:
                    self.board[row_i][col_i] = None

                else:
                    self.board[row_i][col_i] = num

        return

    def move_tile(self, tile):

        """
        Function to move a tile into empty space

        :type tile: list
        :param tile: [row, column] of tile to move.
        """

        # Check for tile to be on board
        if tile[0] > self.dim - 1 or tile[0] < 0 or tile[1] > self.dim - 1 or tile[1] < 0:
            print("Invalid Tile provided")
            raise InvalidTile

        # Check for empty space adjacent to tile
        row_i = tile[0]
        col_i = tile[1] - 1
        for m in range(2):
            try:
                if self.board[row_i][col_i] is None:
                    self.board[row_i][col_i] = self.board[tile[0]][tile[1]]
                    self.moves.append(self.board[tile[0]][tile[1]])
                    self.board[tile[0]][tile[1]] = None
                    return

                else:
                    col_i += 2

            except IndexError:
                continue

        row_i = tile[0] - 1
        col_i = tile[1]
        for m in range(2):
            try:
                if self.board[row_i][col_i] is None:
                    self.board[row_i][col_i] = self.board[tile[0]][tile[1]]
                    self.board[tile[0]][tile[1]] = None
                    return

                else:
                    row_i += 2

            except IndexError:
                continue

        print("Tile cannot be moved")
        raise ImmovableTile

    def verify(self, moves):
        """
        Function to verify moves provided make a solution
        :param moves: array of tiles sorted by move order.
        """

        cur_mov = 0

        for move in moves:
            try:
                cur_mov += 1
                tile = [-1, -1]
                for row_i in range(self.dim):
                    for col_i in range(self.dim):
                        if self.board[row_i][col_i] == move:
                            tile = [row_i, col_i]
                            break

                self.move_tile(tile)

            except InvalidTile or ImmovableTile:
                print("Move #" + str(cur_mov) + " for tile #" + str(move) + "is invalid, no solution found.")
                return False

        # Evaluate board state after moves have been completed
        solution = 0
        for row_i in range(self.dim):
            for col_i in range(self.dim):
                solution += 1
                if solution == self.n + 1:
                    continue
                if self.board[row_i][col_i] != solution:
                    return False

        return True


if __name__ == '__main__':
    pregen = input("Have your own board or verifying a solution? (Y/N): ")
    pregen = pregen[0]

    if pregen.lower() == "y":
        verify = input("Verifying a solution? (Y/N): ")
        verify = verify[0]
        b_import = input("Enter filename: ")
        print()

        with open(b_import, "r") as inp:
            lines = inp.readlines()
            lines = [s.strip('\n') for s in lines]

            n_size = int(lines[0])
            n_dim = int(numpy.sqrt(n_size+1))
            n_board = []
            lines = lines[1:]

            for row_i in range(n_dim):
                temp = lines[0].split()
                row = []
                for col in temp:
                    if col == "e":
                        row.append(None)

                    else:
                        row.append(int(col))

                n_board.append(row)
                lines = lines[1:]
                game = Puzzle(n_size, n_board)

        if verify.lower() == "y":
            n_num_moves = int(lines[0])
            n_moves = []
            lines = lines[1:]

            for m in range(n_num_moves):
                n_moves.append(int(lines[0]))
                lines = lines[1:]

            if game.verify(n_moves):
                print("Solution is valid")

            else:
                print("Moves complete, solution not found.")

    else:
        game = Puzzle()

    response = [""]

    while response[0].lower() != "exit":
        print()
        game.output_board()
        response = input("What would you like to do? (Move #, New, Exit): ").split()

        if response[0].lower() == "move":
            move = int(response[1])

            if move > game.n:
                move = [-1, -1]

            else:
                for row_i in range(game.dim):
                    for col_i in range(game.dim):
                        if game.board[row_i][col_i] == move:
                            move = [row_i, col_i]
                            break

            game.move_tile(move)
            continue

        if response[0].lower() == "new":
            game.gen_board()
            continue






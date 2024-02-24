#!/usr/bin/python3
"""

The N queens puzzle is the challenge of placing N non-attacking queens on an NxN chessboard. Write a program that solves the N queens problem.

    Usage: nqueens N
        If the user called the program with the wrong number of arguments, print Usage: nqueens N, followed by a new line, and exit with the status 1
    where N must be an integer greater or equal to 4
        If N is not an integer, print N must be a number, followed by a new line, and exit with the status 1
        If N is smaller than 4, print N must be at least 4, followed by a new line, and exit with the status 1
    The program should print every possible solution to the problem
        One solution per line
        Format: see example
        You don't have to print the solutions in a specific order
    You are only allowed to import the sys module

Read: Queen, Backtracking

./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
./0-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]


"""
import sys

def out(e):
    print(e)
    sys.exit(1)

if len(sys.argv) != 2:
    out("Usage: nqueens N")

try:
    N = int(sys.argv[1])
except ValueError:
    out("N must be a number")

if N < 4:
    out("N must be at least 4")


class ChessBoard:

    N = 4
    danger = []
    def __init__(self, num) -> None:
        self.N = num
        self.board = []
        self.start_y = 0
        # self.empty_board()
        self.placequenns(0, self.start_y, Board(self.N))

    # def empty_board(self):
    #     for i in range(self.N):
    #         self.board.append(["" for j in range(self.N)])

    def placequenns(self, x=0, y=0, board=None):
        np = ""
        if x == self.N:
            print(board.board)
            self.board.append(self.queen_position(board.board))
            self.danger = []
            self.start_y += 1
            if self.start_y > self.N:
                return
            self.placequenns(0, self.start_y, Board(self.N))
        elif y == self.N:
            if 'Q' not in board.board[x]:
                tmp = self.danger
                self.danger = []
                self.start_y += 1
                if self.start_y > self.N:
                    return
                self.placequenns(0, self.start_y, Board(self.N))
                self.danger = tmp
                return "void"
            self.placequenns(x+1, 0, board)
        elif (x, y) not in self.danger:
            board.board[x][y] = 'Q'
            self.make_danger(x, y)
            y += 1
            if y > self.N:
                return
            np = self.placequenns(x, y, board)
        else:
            y += 1
            if y > self.N:
                return
            np = self.placequenns(x, y, board)
        if np == "void":
            y += 1
            if y > self.N:
                return "void"
            np = self.placequenns(x, y, board)
            return np


    def make_danger(self, x, y):
        j = x
        for i in range(0, self.N):
            self.danger.append((x, i))
            self.danger.append((i, y))
            self.danger.append((j, y-i))
            self.danger.append((j, y+i))
            j += 1

    def queen_position(self, board):
        pos = []
        for i in range(len(board)):
            if 'Q' not in board[i]:
                return None
            for j in range(len(board[i])):
                if board[i][j] == 'Q':
                    pos.append([i, j])
        return pos


class Board():
    def __init__(self, N) -> None:
        self.N = N
        self.board = []
        self.empty_board()

    def empty_board(self):
        for i in range(self.N):
            self.board.append(["" for j in range(self.N)])


chess = ChessBoard(N)
for ch in chess.board:
    if ch is not None:
        print(ch)

"""
[
    ['', '', '', '', '', 'Q'],
    ['Q', '', '', '', '', ''],
    ['', '', 'Q', '', '', ''],
    ['', '', '', '', 'Q', ''],
    ['', '', '', '', '', 'Q'],
    ['Q', '', '', '', '', '']
]
"""

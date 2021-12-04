from typing import List


class Board:

    def __init__(self, board: List[List[int]]):
        self.board = board
        self.marked = []
        for r in range(len(self.board)):
            temp = []
            for c in range(len(self.board)):
                temp.append(1)
            self.marked.append(temp)

    def mark(self, lotto_number: int):
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                self.marked[r][c] = 0 if self.board[r][c] == lotto_number else self.marked[r][c]

    def check_for_win(self) -> bool:
        return self.check_rows() or self.check_cols()

    def check_rows(self) -> bool:
        for r in range(len(self.board)):
            if sum(self.marked[r]) == 0:
                return True
        return False

    def check_cols(self) -> bool:
        for c in range(len(self.board[0])):
            count = len(self.board[0])
            for r in range(len(self.board)):
                count -= self.marked[r][c]
            if count == len(self.board[0]):
                return True
        return False

    def __len__(self) -> int:
        out = 0
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                out += self.marked[r][c] * self.board[r][c]
        return out

    def __str__(self):
        out = ''
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                out += str(self.board[r][c]) + ' '
            out += '\n'
        return out

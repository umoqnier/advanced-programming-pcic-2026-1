"""
Tarea 1
Equipo: Abril Reyes Flores y Diego Alberto Barriga Martínez

Lenguaje: Python 3.10 o superior 
Instrucciones para ejecutar: Abrir una terminal directorio donde se haya guardado magic_square.py y ejecutar con la sentencia python magic_square.py

"""
class MagicSquare:
    def __init__(self, n: int) -> None:
        self.n = n
        self.n_square = n * n
        self.magic_number = n * (self.n_square + 1) // 2
        self.board = [[0 for _ in range(n)] for _ in range(n)]
        self.solutions = []

    def is_complete(self) -> bool:
        return all(i != 0 for row in self.board for i in row)

    def is_valid(self) -> bool:
        used_numbers = [i for row in self.board for i in row if i != 0]
        if len(used_numbers) != len(set(used_numbers)):
            return False
        for row in self.board:
            if 0 not in row and sum(row) != self.magic_number:
                return False
        for col in range(self.n):
            col_vals = [self.board[row][col] for row in range(self.n)]
            if 0 not in col_vals and sum(col_vals) != self.magic_number:
                return False
        main_diag = [self.board[i][i] for i in range(self.n)]
        if 0 not in main_diag and sum(main_diag) != self.magic_number:
            return False
        anti_diag = [self.board[i][self.n - 1 - i] for i in range(self.n)]
        if 0 not in anti_diag and sum(anti_diag) != self.magic_number:
            return False
        return True

    def backtrack(self, row=0, col=0, used=None):
        if used is None:
            used = set()
        if row == self.n:
            if self.is_valid() and self.is_complete():
                solution = [r[:] for r in self.board]
                self.solutions.append(solution)
            return
        next_row, next_col = (row, col + 1) if col + 1 < self.n else (row + 1, 0)
        for num in range(1, self.n_square + 1):
            if num not in used:
                self.board[row][col] = num
                used.add(num)
                if self.is_valid():
                    self.backtrack(next_row, next_col, used)
                self.board[row][col] = 0
                used.remove(num)

    def print_solutions(self):
        for idx, sol in enumerate(self.solutions, 1):
            print(f"Solution {idx}:")
            for row in sol:
                print(row)
            print()


if __name__ == "__main__":
    n = 3
    ms = MagicSquare(n)
    ms.backtrack()
    ms.print_solutions()

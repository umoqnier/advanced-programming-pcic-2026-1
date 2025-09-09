"""
Tarea 1
Equipo: Abril Reyes Flores y Diego Alberto Barriga Martínez
"""


class MagicSquare:
    """Magic Square for 3x3"""

    def __init__(self, n: int = 3) -> None:
        self.n = n
        self.n_square = n * n
        self.magic_number = n * (self.n_square + 1) // 2
        self.board = [[0 for _ in range(n)] for _ in range(n)]
        self.solutions = []

    def is_complete(self) -> bool:
        """Checa si el cuadro está completado

        Un cuadro estará completo si tiene números diferentes
        de cero en todas sus entradas.
        """
        return all(i != 0 for row in self.board for i in row)

    def is_valid(self) -> bool:
        """Checa si el cuadro es mágico

        Un cuadro será mágico si la suma de sus filas, columnas
        y diagonales principales es igual a self.magic_number
        """
        # Obtener los números que sean diferentes de 0
        used_numbers = [i for row in self.board for i in row if i != 0]
        # Si hay repetidos, no es válido
        if len(used_numbers) != len(set(used_numbers)):
            return False
        # Checamos las filas
        for row in self.board:
            # Si la suma de la fila es diferente de magic_number no es válido
            if 0 not in row and sum(row) != self.magic_number:
                return False
        # Checamos la columnas
        for col in range(self.n):
            # Obtenemos los valores de las columnas
            col_vals = [self.board[row][col] for row in range(self.n)]
            # Si la suma de la columna no es un magic number no es válido
            if 0 not in col_vals and sum(col_vals) != self.magic_number:
                return False
        # Checamos diagonal principal
        main_diag = [self.board[i][i] for i in range(self.n)]
        # Si la suma no es numero mágico, no es válido
        if 0 not in main_diag and sum(main_diag) != self.magic_number:
            return False
        # Checamos anti diagonal
        anti_diag = [self.board[i][self.n - 1 - i] for i in range(self.n)]
        # Si la suma no es numero mágico, no es válido
        if 0 not in anti_diag and sum(anti_diag) != self.magic_number:
            return False
        return True

    def backtrack(self, row: int = 0, col: int = 0, used=None) -> None:
        """Realiza el backtrack

        Parameters
        ----------
        row: int
            fila a analizar, default 0
        col: int
            Columna a analizar, default 0
        used: set | None
            Conjunto de números probados en el cuadro

        Return
        ------
        None:
            La solución será almacenada en self.solutions
        """
        if used is None:
            used = set()
        if row == self.n:
            if self.is_valid() and self.is_complete():
                solution = [r[:] for r in self.board]
                self.solutions.append(solution)
            return
        # Selección de la columna y fila a analizar
        next_row, next_col = (row, col + 1) if col + 1 < self.n else (row + 1, 0)
        for num in range(1, self.n_square + 1):
            if num not in used:
                # Si no fue usado, lo agregamos al cuadro
                self.board[row][col] = num
                # Lo agregamos a los numeros que aun no se usan
                used.add(num)
                # Si es una solución parcial, continua
                if self.is_valid():
                    # Llamada recursiva con las siguientes columnas/filas/numeros usados
                    self.backtrack(next_row, next_col, used)
                # Si no es válido, backtrackeamos
                self.board[row][col] = 0
                # Quitamos número no válido de los usados
                used.remove(num)

    def print_solutions(self) -> None:
        """Imprime el cuadro que es solución"""
        for idx, sol in enumerate(self.solutions, 1):
            print(f"Solution {idx}:")
            for row in sol:
                print(row)
            print()


if __name__ == "__main__":
    n = 3
    expected_solutions = [
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
    ]
    ms = MagicSquare(n)
    ms.backtrack()
    assert ms.solutions == expected_solutions, (
        "Error, no se encontraron las soluciones esperadas"
    )
    ms.print_solutions()

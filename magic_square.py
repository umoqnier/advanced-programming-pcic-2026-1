class MagicSquare:
    def __init__(self, n: int) -> None:
        self.n = n
        self.n_square = n * n
        self.magic_number = n * (self.n_square + 1) / 2
        self.board = [[0 for _ in range(n)] for _ in range(n)]

    def is_complete(self) -> bool:
        return not any(i for row in self.board for i in row) == 0

    def is_valid(self) -> bool:
        # Los numeros de 1-9 son usados exactamente una vez
        once_condition = {i for row in self.board for i in row} == {
            i for i in range(1, self.n**2 + 1)
        }
        # La suma de los numeros en cada fila es = self.magicnumber
        row_condition = True
        for row in self.board:
            if sum(row) != self.magic_number:
                row_condition = False
                break
        # La suma de los numeros en cada columna es self.magic_numer

        # La suma de los numeros en las dos diagonales es, en cada una, = self.magic_number
        return all([once_condition, row_condition])

    def backback(self, board: list[list]):
        pass

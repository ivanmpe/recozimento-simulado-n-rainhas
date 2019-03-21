import random

class Board:
    def __init__(self, queen_count=8):
        self.queen_count = queen_count
        self.perturbation()
        
    #gera novo estado do tabuleiro
    def perturbation(self):
        self.queens = [-1 for i in range(0, self.queen_count)]

        for i in range(0, self.queen_count):
            self.queens[i] = random.randint(0, self.queen_count - 1)

    #calcula a quantidade das ameaças
    def calculateTreats(queens):
        threat = 0
        queen_count = len(queens)

        for queen in range(0, queen_count):
            for next_queen in range(queen+1, queen_count):
                #Verifica se existe ataque entre as rainhas nivel de coluna ou diagonal
                if queens[queen] == queens[next_queen] or abs(queen - next_queen) == abs(queens[queen] - queens[next_queen]):
                    threat += 1

        return threat

    def show(queens):
        board_string = ""

        for row, col in enumerate(queens):
            board_string += "(%s, %s)\n" % (row, col)

        return board_string

    def __str__(self):
        board_string = ""

        for row, col in enumerate(self.queens):
            board_string += "(%s, %s)\n" % (row, col)

        return board_string
    
    
    
    
    

import random
from board import Board

class SimulatedAnnealing:
   
    
    def __init__(self, board):
        self.board = board
        self.temperature = 2000
        self.a = 0.99


    def run(self):
        board = self.board
        board_queens_current = self.board.queens[:] 
        solution = False
        
        for k in range(0, 10000000):
            
            #Redução geometrica da Temperatura
            self.temperature *= self.a
            
            #Realiza a pertubação em uma iteração
            board.perturbation()
            successor_queens = board.queens[:]
            
            delta = Board.calculateTreats(successor_queens) - Board.calculateTreats(board_queens_current)
            exp = (-delta) / (self.temperature)

            #Teste de aceitação de uma nova solução
            # Tomada de decisao com base na variacao de energia e na probabilidade
            if delta > 0 or random.uniform(0, 1) < exp:
                board_queens_current = successor_queens[:]
                
            #Testa se não existem ataques entre as rainhas, solução encontrada! 
            if Board.calculateTreats(board_queens_current) == 0:
                #print Solução
                print("Solução:")
                print(Board.show(board_queens_current))
                solution = True
                break

        #caso ao final de todo o Loop principal se encerre sem solução
        if solution == False:
            print("Não foi possivel encontrar solução.")


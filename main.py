from board import Board
from simulated_annealing import SimulatedAnnealing
import time

if __name__ == '__main__':
    
    startTime = time.time()
   
    for i in range(0,5):
        print("i: {}" .format(i))
        board = Board()
        print("Rainhas:")
        print(board)
        SimulatedAnnealing(board).run() 
    
    endTime = time.time() 
    elapsedTime = (endTime - startTime)
    average = elapsedTime / 10
    print("Tempo total: {} " .format(elapsedTime))
    print("Tempo médio: {}" .format(average))
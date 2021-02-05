import PrintSudoku
import SolveSudoku
import pprint as pp

def take_input():
    puzzle=[]
    for _ in range(9):
        lis=[]
        s=input()
        for j in s:
            lis.append(int(j))
        puzzle.append(lis)
    print ("\nInput Given....")
    PrintSudoku.printPuzzle(puzzle,"")
    return puzzle

puzzle = take_input()


'''
puzzle = [[0, 0, 7, 0, 1, 3, 0, 0, 0],
          [0, 0, 0, 2, 0, 6, 5, 4, 7],
          [6, 4, 2, 9, 5, 0, 3, 0, 1], 
          [8, 1, 0, 0, 0, 0, 0, 0, 0], 
          [0, 2, 0, 0, 0, 0, 0, 3, 0], 
          [0, 0, 0, 0, 0, 0, 0, 6, 5], 
          [2, 0, 1, 0, 3, 8, 9, 5, 4], 
          [7, 9, 3, 5, 0, 2, 0, 0, 0], 
          [0, 0, 0, 6, 9, 0, 7, 0, 0]]

puzzle = [[0, 0, 0, 0, 0, 0, 6, 8, 0],
          [0, 0, 0, 0, 7, 3, 0, 0, 9],
          [3, 0, 9, 0, 0, 0, 0, 4, 5],
          [4, 9, 0, 0, 0, 0, 0, 0, 0], 
          [8, 0, 3, 0, 5, 0, 9, 0, 2], 
          [0, 0, 0, 0, 0, 0, 0, 3, 6], 
          [9, 6, 0, 0, 0, 0, 3, 0, 8], 
          [7, 0, 0, 6, 8, 0, 0, 0, 0], 
          [0, 2, 8, 0, 0, 0, 0, 0, 0]]
'''
initial = SolveSudoku.computePossibilities(puzzle)
print("Initial Possibilities are :\n")
pp.pprint(initial)
SolveSudoku.solveSudoku(puzzle,0)

    



                
            



        
    

 





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



initial = SolveSudoku.computePossibilities(puzzle)
print("Initial Possibilities are :\n")
pp.pprint(initial)
SolveSudoku.solveSudoku(puzzle,0)

    



                
            



        
    

 





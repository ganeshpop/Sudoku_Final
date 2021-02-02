import pprint as pp
import PrintSudoku
def getPossibilities(loc,puzzle):
            possibilities=[1,2,3,4,5,6,7,8,9]
            i=0
            j=0
            x = int(loc[0])
            y = int(loc[1])
            for _ in range(9):
                if i < 9:
                    if puzzle[i][y] in possibilities:
                        possibilities.remove(puzzle[i][y])
                
                    i+=1
            for _ in range(9):
                if j < 9:
                    if puzzle[x][j] in possibilities:
                        possibilities.remove(puzzle[x][j])
                    j+=1
            
            box=[int(x/3)*3,int(y/3)*3]
            i = box[0]
            j = box[1]
            for _ in range(3):
                for _ in range(3):
                    if j == 3 + box[1]:
                        i+=1
                        j = box[1]
                    
                    if puzzle[i][j] in possibilities:
                            
                        possibilities.remove(puzzle[i][j])
                        
                    j+=1
            
            return possibilities



def computePossibilities(puzzle):
    possibilities = {}
    for i in range(9):
        for j in range(9):
            loc=(i,j)
            if puzzle[i][j] == 0:
                poss=getPossibilities(loc,puzzle)
                if len(poss) in possibilities:
                    possibilities[len(poss)][loc]=poss

                else:
                    possibilities[len(poss)] =  { loc : poss }    
    return possibilities
def copyPuzzle(puzzle):
    puzzle2 = []
    for i in puzzle:
        lis=[]
        for j in i:
            lis.append(j)
        puzzle2.append(lis)
    return puzzle2



def isSolved(puzzle):
    if sum([row.count(0) for row in puzzle]) == 0:
        return True
    else:
        return False



def solveSudoku(puzzle,level):
    pref = " " * (level * 4)
    print(pref, "Entring Solve Sudoku.....\n")
    PrintSudoku.printPuzzle(puzzle, pref)
    possibilities = computePossibilities(puzzle)
    if 0 in possibilities :
        return False
    while 1 in possibilities:
        for possibility in possibilities[1]:
                print(pref,"Setting {} at location {}".format(possibilities[1][possibility][0],possibility))
                puzzle[possibility[0]][possibility[1]]=possibilities[1][possibility][0]
                possibilities = computePossibilities(puzzle)
                if 0 in possibilities :
                    return False
       #PrintSudoku.printPuzzle(puzzle, pref)
        
    print(pref, "No of cells left to fill : ",sum([row.count(0) for row in puzzle]))
        
        


    if isSolved(puzzle):
        print("\n",pref,"Puzzle Solved!")
        PrintSudoku.printPuzzle(puzzle,pref)
        return True
    else:
        for i in range(2,10):
            if i in possibilities:
                for loc in possibilities[i]:
                    print("\n",pref,"Trying {} possibilities at location {}".format(possibilities[i][loc][0],loc))
                    for p in possibilities[i][loc]:
                        print(pref,"Setting {} at location {}".format(p,loc))
                        puzzle2 = copyPuzzle(puzzle)
                        puzzle2[loc[0]][loc[1]]=p
                        if solveSudoku(puzzle2,level+1):
                            return True
                        else:
                            print(pref,"I tried {} at location {}, it didnt work. ".format(p,loc))
                            pass
                    
                    return False
        

                        







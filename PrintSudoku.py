def printPuzzle(puzzle,pref):
    single_line = "++---+---+---++---+---+---++---+---+---++"
    double_line="++===+===+===++===+===+===++===+===+===++"
    row_count=0
    count=0
    for i in puzzle:
        if row_count%3==0:
            print(pref,double_line)
        else:
            print(pref,single_line)
        string="||"
        for j in i:
            if j == 0:
                j = " "
            count+=1
            string+=" {} ".format(j)
            if count%3==0:
                string+="||"
            else:
                string+="|"
        row_count+=1
        print(pref,string)
    print(pref, double_line) 

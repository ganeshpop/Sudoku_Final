matrix=[]
for i in range(9):
    lis=[]
    s=input("Enter row {} : ".format(i))
    for j in s:
        lis.append(int(j))
    matrix.append(lis)
print ("\nInput Given....")

for i in matrix:
    print(i)

while 0 in matrix[0]:           
    def find(loc):
        arr=[1,2,3,4,5,6,7,8,9]
        i=0
        j=0
        x = int(loc[0])
        y = int(loc[1])
        for _ in range(9):
            if i < 9:
                if matrix[i][y] in arr:
                    arr.remove(matrix[i][y])
            
                i+=1
        for _ in range(9):
            if j < 9:
                if matrix[x][j] in arr:
                    arr.remove(matrix[x][j])
                j+=1
        
        box=[int(x/3)*3,int(y/3)*3]
        i = box[0]
        j = box[1]
        for _ in range(3):
            for _ in range(3):
                if j == 3 + box[1]:
                    i+=1
                    j = box[1]
                if matrix[i][j] in arr:
                    arr.remove(matrix[i][j])
                    
                j+=1
        return arr
    index =[]
    value=[]
    for i in range(9):
        for j in range(9):
            loc=[i,j]
            if matrix[i][j] == 0:
                possibilities=find(loc)
                if len(possibilities) == 1:
                    print(loc)
                    print(possibilities[0])
                    index.append(loc)
                    value.append(possibilities[0])


    for i in index:
        matrix[i[0]][i[1]]=value[0]
        value.remove(value[0])
s = "++---+---+---++---+---+---++---+---+---++"
s1 ="++===+===+===++===+===+===++===+===+===++"
row_count=0
count=0
print("Solution....")
for i in matrix:
    if row_count%3==0:
        print(s1)
    else:
        print(s)
    string="||"
    for j in i:
        count+=1
        string+=" {} ".format(j)
        if count%3==0:
            string+="||"
        else:
            string+="|"
    row_count+=1
    print(string)
print(s1)   
        
        



        


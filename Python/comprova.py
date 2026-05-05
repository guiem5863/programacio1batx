
def comprovaGrup(grup):
    tots = [1,2,3,4,5,6,7,8,9]

    for i in range(len(grup)):
        #print("El valor de tots és ", grup[i])
        if (grup[i] in tots):
            tots.remove(grup[i])
        #print("Llista grup:", grup )
        #print("Llista tots:", tots )

    if len(tots) == 0:
        return True
    else:
        return False

fila = []
columna = [] 
grup = []

sudoku =[   [9,6,3,1,7,4,2,5,8],
            [1,7,8,3,2,5,6,4,9],
            [2,5,4,6,8,9,7,3,1],
            [8,2,1,4,3,7,5,9,6],
            [4,9,6,8,5,2,3,1,7],
            [7,3,5,9,6,1,8,2,4],
            [5,8,9,7,1,3,4,6,2],
            [3,1,7,2,4,6,9,8,5],
            [6,4,2,5,9,8,1,7,3]
            ]

print("COMPROVANT COLUMNES")
for i in range(9):
    for j in range(9):
        columna.append(sudoku[j][i])
    print("columna ", i, ": ",columna)
    comprovaGrup(columna)
    columna=[]

print("COMPROVANT FILES")
for i in range(9):
    for j in range(9):
        fila.append(sudoku[i][j])
    print("fila ", i, ": ",fila)
    comprovaGrup(fila)
    fila=[]

print("COMPROVANT GRUPS DE 3x3")
for i in range(3):
    for j in range(3):
        grup.append(sudoku[i][j])
    print("grup ", i, ": ",grup)
    comprovaGrup(grup)
    grup=[]

for n in range(9):

    for i in range(3):
        for j in range(3):
            fila.append(sudoku[i][j])
            y = 0
            l = 0
            if(n>=3):
                y=(n%1)+1
            if(n>=6):
                l=(n%1)+1

            #print("fila", i, ": ", fila, "columna", j, ": ")
            #print(i+3*(y+l),j+3*(n%3))

#i+3*IF(n>=3;(n%1)+1;0)+IF(n>=6;(n%1)+3;0)       
# =D6 + 3*IF(C6>=3; MOD(C6;1)+1; 0) + IF(C6>=6; MOD(C6;1)+3; 0)     

def comprovaGrup(grup):
    for n in range(9):

        for i in range(3):
            for j in range(3):
                fila.append(sudoku[i][j])
                y = 0
                l = 0
                if(n>=3):
                    y=(n%1)+1
                if(n>=6):
                    l=(n%1)+1
                #print(i+3*(y+l),j+3*(n%3))




grup.append(sudoku[0][0])
grup.append(sudoku[0][1])
grup.append(sudoku[0][2])
grup.append(sudoku[1][0])
grup.append(sudoku[1][1])
grup.append(sudoku[1][2])
grup.append(sudoku[2][0])
grup.append(sudoku[2][1])
grup.append(sudoku[2][2])

#print("grup 0: ",grup)
comprovaGrup(grup)
grup=[]

grup.append(sudoku[0][3])
grup.append(sudoku[0][4])
grup.append(sudoku[0][5])
grup.append(sudoku[1][3])
grup.append(sudoku[1][4])
grup.append(sudoku[1][5])
grup.append(sudoku[2][3])
grup.append(sudoku[2][4])
grup.append(sudoku[2][5])

#print("grup 1: ",grup)
comprovaGrup(grup)
grup=[]

grup.append(sudoku[0][6])
grup.append(sudoku[0][7])
grup.append(sudoku[0][8])
grup.append(sudoku[1][6])
grup.append(sudoku[1][7])
grup.append(sudoku[1][8])
grup.append(sudoku[2][0])
grup.append(sudoku[2][7])
grup.append(sudoku[2][8])

#print("grup 2: ",grup)
comprovaGrup(grup)
grup=[]

grup.append(sudoku[3][0])
grup.append(sudoku[3][1])
grup.append(sudoku[3][2])
grup.append(sudoku[4][0])
grup.append(sudoku[4][1])
grup.append(sudoku[4][2])
grup.append(sudoku[5][0])
grup.append(sudoku[5][1])
grup.append(sudoku[5][2])

#print("grup 3: ",grup)
comprovaGrup(grup)
grup=[]

grup.append(sudoku[3][3])
grup.append(sudoku[3][4])
grup.append(sudoku[3][5])
grup.append(sudoku[4][3])
grup.append(sudoku[4][4])
grup.append(sudoku[4][5])
grup.append(sudoku[5][3])
grup.append(sudoku[5][4])
grup.append(sudoku[5][5])

#print("grup 4: ",grup)
comprovaGrup(grup)
grup=[]

grup.append(sudoku[3][6])
grup.append(sudoku[3][7])
grup.append(sudoku[3][8])
grup.append(sudoku[4][6])
grup.append(sudoku[4][7])
grup.append(sudoku[4][8])
grup.append(sudoku[5][6])
grup.append(sudoku[5][7])
grup.append(sudoku[5][8])

#print("grup 5: ",grup)
comprovaGrup(grup)
grup=[]

grup.append(sudoku[6][0])
grup.append(sudoku[6][1])
grup.append(sudoku[6][2])
grup.append(sudoku[7][0])
grup.append(sudoku[7][1])
grup.append(sudoku[7][2])
grup.append(sudoku[8][0])
grup.append(sudoku[8][1])
grup.append(sudoku[8][2])

#print("grup 6: ",grup)
comprovaGrup(grup)
grup=[]


grup.append(sudoku[6][3])
grup.append(sudoku[6][4])
grup.append(sudoku[6][5])
grup.append(sudoku[7][3])
grup.append(sudoku[7][4])
grup.append(sudoku[7][5])
grup.append(sudoku[8][3])
grup.append(sudoku[8][4])
grup.append(sudoku[8][5])

#print("grup 7: ",grup)
comprovaGrup(grup)
grup=[]

grup.append(sudoku[6][6])
grup.append(sudoku[6][7])
grup.append(sudoku[6][8])
grup.append(sudoku[7][6])
grup.append(sudoku[7][7])
grup.append(sudoku[7][8])
grup.append(sudoku[8][6])
grup.append(sudoku[8][7])
grup.append(sudoku[8][8])

#print("grup 8: ",grup)
comprovaGrup(grup)
grup=[]



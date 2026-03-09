
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

fila = [1,4,4,5,6,7,8,9]
columna = [] 

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


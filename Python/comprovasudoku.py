def comprovaGrup(quadrat):

    tots = [1,2,3,4,5,6,7,8,9]

    for i in range(len(quadrat)):
        #print("El valor de tots és ", grup[i])
        if (quadrat[i] in tots):
            tots.remove(quadrat[i])
        #print("Llista grup:", grup )
        #print("Llista tots:", tots )

    if len(tots) == 0:
        return True
    else:
        return False



def quifalta(llista):
    #funció que ens retorna els nombres que falten d'una llista de 1 a 9

    r = []

    for i in range(1,10):
        try:
            llista.index(i)
            #print(i, "present")
        except ValueError:
            #print(i, "no present")
            r.append(i)
            #print(r)
    return r

def troba(e1,e2,e3):
    #funció que cerca el nombre repetit en les tres llistes

    t = []
    
    for j in range(1,10):
        if(j in e1) & (j in e2) & (j in e3):
            t.append(j)
            #print(t)
    return t



sudoku =[   [0,7,9,0,6,0,0,0,0],
            [0,0,5,9,8,4,0,2,0],
            [0,0,0,0,0,0,4,3,0],
            [9,0,0,0,0,0,0,0,0],
            [5,3,0,0,0,0,0,0,0],
            [0,4,0,0,0,0,0,0,0],
            [0,0,4,0,0,0,0,0,0],
            [0,0,0,8,0,0,0,0,0],
            [0,0,0,7,0,0,9,4,0]
            ]


    
fila =  []
columna =  []
grup =  []

quadrat = []

quadrat = comprovaGrup(quadrat)



sudoku =[   [0,7,9,0,6,0,0,0,0],
            [0,0,5,9,8,4,0,2,0],
            [0,0,0,0,0,0,4,3,0],
            [9,0,0,0,0,0,0,0,0],
            [5,3,0,0,0,0,0,0,0],
            [0,4,0,0,0,0,0,0,0],
            [0,0,4,0,0,0,0,0,0],
            [0,0,0,8,0,0,0,0,0],
            [0,0,0,7,0,0,9,4,0]
            ]


for i in range(9):
    for j in range(9):
        fila.append(sudoku[i][j])
    print("fila ", i, ": ",fila)
    comprovaGrup(fila)
    quifalta(fila)
    fila=[]
    
    
for i in range(9):
    for j in range(9):
        columna.append(sudoku[j][i])
    print("columna ", i, ": ",columna)
    comprovaGrup(columna)
    columna=[]


e1 = quifalta(fila)
e2 = quifalta(columna)
e3 = quifalta(grup)

n = troba(e1,e2,e3)

print("falten els elements: ", "fila: ", e1, "/ columna: ", e2, "/ grup: ", e3)
print("el nombre comú és: ", n)
import requests

def llegeixSudoku():
    x = requests.get('https://sudoku-api.vercel.app/api/dosuku')
    #print(x.text)
    dades = x.json()
    print(dades["newboard"]["grids"][0]["solution"])
    return dades

def llegeixSudokuN():
    x = requests.get('https://sudoku-api.vercel.app/api/dosuku')
    print(x.text)
    dades = x.json()
    print(dades["newboard"]["grids"][0]["value"])
    return dades["newboard"]["grids"][0]["value"]

def imprimeixSudoku(s):
    for i in s:
        print(i)

def comprovaSudoku():
    #retorna true si el valor és un grup de sudoku és correcte
    #grup: linia, columna, quadrat
    #El grup ha de tenir tots els nombres i no repetirne cap.
    print("S'ha de fer el algoritme.")

    
    for i in range(len(sudoku)):
        tot = {1,2,3,4,5,6,7,8,9}
        #print("fila", i, "té", len(sudokuN[i]), "columnes")
        for j in range(len(sudoku[i])):
            print(sudoku[i][j])
            tot.remove(sudoku[i][j])

        if(len(tot) == 0):
            print("La fila està bé")
        else:
            print("La fila no està bé")



def contarZeros():
    print("contaré zeros")
    n = 0
    for i in range(len(sudokuN)):
        #print("fila", i, "té", len(sudokuN[i]), "columnes")
        for j in range(len(sudokuN[i])):
            if(sudokuN[i][j] == 0):
                n= n + 1
            #print("ha trobat ", n, "zeros")
    print("ha trobat ", n, "zeros")
    return n

sortir=False

sudoku=[]
sudokuN=[]

while not sortir:   
    print("*************************************")
    print("BENVINGUDES AL COMPROVADOR DE SUDOKUS")
    print("*************************************")
    print("1. Comprovar el sudoku")
    print("2. Mostrar el sudoku")
    print("3. Llegir el sudoku")
    print("4. Contar Zeros")
    print("0. Sortir")
    print("*************************************")
    opcio = input("Introdueix una opció: ")
    if opcio == "1":
        comprovaSudoku()
    elif opcio == "2":
        print("SUDOKU NO RESOLT")
        imprimeixSudoku(sudokuN)
        print("SUDOKU RESOLT")
        imprimeixSudoku(sudoku)
    elif opcio == "3":
        dades = llegeixSudoku()
        sudoku=dades["newboard"]["grids"][0]["solution"]
        sudokuN = dades["newboard"]["grids"][0]["value"]
        print("S'ha llegit un nou sudoku resolt")
    elif opcio == "4":
        zeros = contarZeros()
    elif opcio == "0":
        sortir=True

print("Fins aviat!")
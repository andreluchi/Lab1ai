from collections import deque 
import print as pr
import discretizar as disc

def findStart(matriz):
    for y in range(matriz.shape[0]):
        for x in range(matriz.shape[1]):
            if(matriz[y][x] == 2):
                return y,x

def end(matriz):
    res = []
    for y in range(matriz.shape[0]):
        for x in range(matriz.shape[1]):
            if(matriz[y][x] == 3):
                temp = []
                temp.append(y)
                temp.append(x)
                res.append(temp)
    return res

def dfs(x,y,matriz):
    frontera.append((y,x))
    solution[y,x] = y,x
    while len(frontera) > 0:
        ccell = (y,x)
        
        if(x-1 >= 0  and (int(matriz[y][x-1]) == 0 or int(matriz[y][x-1]) == 2 or int(matriz[y][x-1]) == 3) and (y,x-1) not in visitadas):
            cellizq = (y,x-1)
            solution[cellizq] = y,x
            frontera.append(cellizq)
           
        if(y-1 >= 0  and (int(matriz[y-1][x]) == 0 or int(matriz[y-1][x]) == 2 or int(matriz[y-1][x]) == 3) and (y-1,x) not in visitadas):
            cellabajo = (y-1,x)
            solution[cellabajo] = y,x
            frontera.append(cellabajo)
                
        if(x+1 < matriz.shape[0]  and (int(matriz[y][x+1]) == 0 or int(matriz[y][x+1]) == 2 or int(matriz[y][x+1]) == 3  ) and (y,x+1) not in visitadas):
            cellderech = (y,x+1)
            solution[cellderech] = y,x
            frontera.append(cellderech)
           
        if(y+1 < matriz.shape[0]  and (int(matriz[y+1][x]) == 0 or int(matriz[y+1][x]) == 2 or int(matriz[y+1][x]) == 3) and (y+1,x) not in visitadas):
            cellarriba = (y+1,x)
            solution[cellarriba] = y,x
            frontera.append(cellarriba)
            
        y, x = frontera.pop()           
        visitadas.append(ccell)    
        

def dfsinv(matriz, startY,startX,ends, size):
    orgArr = []

    for end in ends:
        y = end[0]
        x = end[1]
        cont = 0
        if (y,x) in solution:
            while (y, x) != (startY, startX):
                y, x = solution[y, x]
                cont = cont + 1
            temp = []
            temp.append(end[0])
            temp.append(end[1])
            temp.append(cont)
            orgArr.append(temp)
    lowest = orgArr[0]
    for exits in orgArr:
        if(lowest[2] > exits[2]):
            lowest = exits
    while (lowest[1], lowest[0]) != (startX, startY): 
        matriz[lowest[0]][lowest[1]] = 4
        lowest[0], lowest[1] = solution[lowest[0], lowest[1]]

    pr.showFinal(matriz,1000,1000,size)
    

visitadas = []
frontera = []
solution = {}


def correr(matriz,size):
    ends = end(matriz.astype(int))
    startY,startX = findStart(matriz.astype(int))
    dfs(startX,startY, matriz.astype(int))
    dfsinv(matriz.astype(int), startY, startX, ends, size)
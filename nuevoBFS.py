from collections import deque
import print as pr

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
    print(res)
    return res

def search(x,y,matriz):
    frontier.append((y, x))
    solution[y,x] = y,x

    while (len(frontier) > 0):          
        y, x = frontier.popleft()     

        if(x-1 >= 0  and (int(matriz[y][x-1]) == 0 or int(matriz[y][x-1]) == 2 or int(matriz[y][x-1]) == 3) and (y,x-1) not in visited):
            cell = (y, x-1)
            solution[cell] = y, x    
            frontier.append(cell)   
            visited.add((y, x - 1))  

        if(y-1 >= 0  and (int(matriz[y-1][x]) == 0 or int(matriz[y-1][x]) == 2 or int(matriz[y-1][x]) == 3) and (y-1,x) not in visited):
            cell = (y - 1, x)
            solution[cell] = y, x
            frontier.append(cell)
            visited.add((y - 1, x))

        if(x+1 < matriz.shape[0]  and (int(matriz[y][x+1]) == 0 or int(matriz[y][x+1]) == 2 or int(matriz[y][x+1]) == 3) and (y,x+1) not in visited):
            cell = (y, x + 1)
            solution[cell] = y, x
            frontier.append(cell)
            visited.add((y, x + 1))

        if(y+1 < matriz.shape[0]  and (int(matriz[y+1][x]) == 0 or int(matriz[y+1][x]) == 2 or int(matriz[y+1][x]) == 3) and (y+1,x) not in visited): 
            cell = (y + 1, x)
            solution[cell] = y, x
            frontier.append(cell)
            visited.add((y + 1, x))

def backRoute(matriz,startY,startX,ends,size):
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

visited = set()
frontier = deque()
solution = {}  

def magia(matriz,size):
    ends = end(matriz)                         
    startY,startX = findStart(matriz)
    search(startX,startY, matriz)
    backRoute(matriz,startY,startX, ends,size)
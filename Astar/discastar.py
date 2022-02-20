from PIL import Image, ImageDraw
import math
import numpy as np
images = []

zoom = 20
borders = 6 #Variables para la im

def disc(imagen):
    image = Image.open(imagen)
    new_image = image.resize((25, 25))
    temp = np.array(new_image)
    listd = []
    media = 0 
    diff = 0 
    nmax = 0
    nmin = 0
    r = 0
    g = 0
    b = 0
    new_size = math.sqrt(temp.size/3)
    new_size = int(new_size)
    a = np.zeros(shape=(new_size,new_size)) 
    for i in range(len(temp)):
        for j in range(len(temp[i])):
            listd = temp[i][j]
            r = listd[0]
            g = listd[1]
            b = listd[2]
            media = sum(listd)/3
            nmax = max(listd)
            nmin = min(listd)
            diff = nmax - nmin
            if(diff<15):
                if media>200:
                    a[i][j] = 0 #blanco
                else:
                    a[i][j] = 1 #negro
            else:
                if((r>g) and (r>b)):
                    a[i][j] = 2 #rojo
                else:
                    if((g>r) and (g>b)):
                        a[i][j] = 3 #verde
                    else:
                        a[i][j] = 4 #azul
                    

        listd = []
        r = 0
        g = 0
        b = 0
        media = 0
    with open('outfile.txt','wb') as f:
        np.savetxt(f, a, fmt='%.2f')            
    #Area caminar
    r2 = np.where(a == 2)
    listOfCoordinates= list(zip(r2[0], r2[1]))
    start = []
    for pnts in listOfCoordinates:
        start= pnts
    v2 = np.where(a == 3)
    listOfCoordinates= list(zip(v2[0], v2[1]))
    cdtd=[]
    for pnts in listOfCoordinates:
        cdtd.append(pnts)
    p = np.zeros(shape=(new_size,new_size))
    for i in range(len(temp)):
        for j in range(len(temp[i])):
            listd = temp[i][j]
            r = listd[0]
            g = listd[1]
            b = listd[2]
            media = sum(listd)/3
            nmax = max(listd)
            nmin = min(listd)
            diff = nmax - nmin
            if(diff<15):
                if media>200:
                    p[i][j] = 0 #blanco
                else:
                    p[i][j] = 1 #negro
            else:
                p[i][j] = 0 #blanco
                               

        listd = []
        r = 0
        g = 0
        b = 0
        media = 0
    p= p.astype(int)
    return p,start,cdtd
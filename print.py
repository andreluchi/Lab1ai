import contextlib
from PIL import Image

def showDiscrete(mainMatrix, imagen):
    

    for y in range(mainMatrix.shape[0]):
        for x in range(mainMatrix.shape[1]):
            imagen.putpixel((x,y),(tuple(mainMatrix[y][x])))

    imagen.show()
  

def showFinal(newMatrix, height,width,disc):
    final = Image.new('RGBA',(height,width),'white')
    newX = 0
    newY = 0
    contB = 0
    contW = 0
    for y in range(newMatrix.shape[0]):
        newX = 0
        for x in range(newMatrix.shape[1]):
            if(newMatrix[y][x] == 0):
                r = 255
                b = 255
                g = 255
            elif(newMatrix[y][x] == 1):
                r = 0
                g = 0
                b = 0
            elif(newMatrix[y][x] == 2):
                r = 255
                g = 0
                b = 0
            
            elif(newMatrix[y][x] == 3):
                r = 0
                g = 255
                b = 0
                
            elif(newMatrix[y][x] == 4):
                r = 255
                g = 0
                b = 255
                
            newlimitY = 0
            newlimitX = 0
            while(newlimitY < disc):
                newlimitX = 0
                while(newlimitX < disc):
                    if(newX + newlimitX < width and newY + newlimitY < height):
                        final.putpixel((newX + newlimitX,newY + newlimitY),(r,g,b))
                    newlimitX = newlimitX + 1
                newlimitY = newlimitY + 1
            newX = newX + disc
        newY = newY + disc
    final.show()

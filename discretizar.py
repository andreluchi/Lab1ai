from selectors import EVENT_READ
from PIL import Image
import numpy
import print as final



def disc(mainMatrix, disc):
    width = mainMatrix.shape[1]
    height = mainMatrix.shape[0]
    currentPosX = 0
    currentPosY = 0
    limitX = 0
    limitY = 0
    newMatrix = numpy.zeros((int(height/disc),int(width/disc)))
    while(currentPosY <= height):
        currentPosX = 0
        limitX = 0
        limitY = currentPosY + disc
        while(currentPosX <= width):
            limitX = currentPosX + disc
            blanco = 0
            negro = 0
            rojo = 0
            verde = 0

            if(limitY <= height and limitX <= width):
                for y in range(0,disc):
                    for x in range(0,disc):
                        color = mainMatrix[currentPosY + y][currentPosX + x]
                        if (color[0] >= 150 and color[1] >= 150 and color[2] >= 150):
                            blanco = blanco + 1
                        elif(color[0] <= 149 and color[1] <= 149 and color[2] <= 149):
                            negro = negro + 1
                        elif(color[0] <= 100 and color[1] >= 150 and color[2] <= 100):
                            verde = verde + 1
                        elif(color[0] >= 200 and color[1] <= 100 and color[2] <= 100):
                            rojo = rojo + 1

                if(blanco > negro and blanco > rojo and blanco > verde):
                    newMatrix[int(currentPosY/disc)][int(currentPosX/disc)] = int(0)
                    

                elif(negro > blanco and negro > rojo and negro > verde):
                    newMatrix[int(currentPosY/disc)][int(currentPosX/disc)] = int(1)
                    
                
                elif(rojo > blanco and rojo > negro and rojo > verde):
                    newMatrix[int(currentPosY/disc)][int(currentPosX/disc)] =int(2)
        

                elif(verde > blanco and verde > negro and verde > rojo):
                    newMatrix[int(currentPosY/disc)][int(currentPosX/disc)] = int(3)
                    

            currentPosX = currentPosX + disc
        currentPosY = currentPosY + disc
    
    return newMatrix

    #final.showFinal(newMatrix,height,width)
    #xd = Image.open('prueba2.bmp')
    #final.showDiscrete(newMatrix, imagen)


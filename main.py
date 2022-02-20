from PIL import Image
import numpy
import discretizar as disc
import print as pr
import nuevoBFS as bfs
import dfs as dfs

imagen = Image.open('lol2.png')
mainMatrix =  numpy.asarray(imagen.convert('RGB'))

size = 2

matrizPeque = disc.disc(mainMatrix,size)
#pr.showFinal(matrizPeque,1000,1000,size)
dfs.correr(matrizPeque,size)
bfs.magia(matrizPeque,size)
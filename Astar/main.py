from discastar import* 
from astarm  import*
from PIL import Image, ImageDraw
import numpy as np


img = input("Escribir la imagen a procesar (ej:prueba2.bmp):")
img2= Image.open(img)
a = disc(img)[0]
start = disc(img)[1]
end_l = disc(img)[2]
astarf(a,start,end_l[len(end_l)-1])
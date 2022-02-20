#G cost distancia entre current y start
#H cost es distancia entre current y end
#F es G + H
import numpy as np
from PIL import Image, ImageDraw
import math

images = []

zoom = 20
borders = 6 #Variables para la im

def astarf(a,starts,ends):
    def draw_matrix(a,start_i,start_j,end_i,end_j, the_path=[]): #graficar solucion para maze con maze previa
        im = Image.new('RGB', (zoom * len(a[0]), zoom * len(a)), (255, 255, 255))
        draw = ImageDraw.Draw(im)
        for i in range(len(a)):
            for j in range(len(a[i])):
                color = (255, 255, 255)
                r = 0
                if a[i][j] == 1:
                    color = (0, 0, 0)
                if i == start_j and j == start_j:
                    color = (0, 255, 0)
                    r = borders
                if i == end_i and j == end_j:
                    color = (0, 255, 0)
                    r = borders
                draw.rectangle((j*zoom+r, i*zoom+r, j*zoom+zoom-r-1, i*zoom+zoom-r-1), fill=color)
                if a[i][j] == 2:
                    r = borders
                    draw.ellipse((j * zoom + r, i * zoom + r, j * zoom + zoom - r - 1, i * zoom + zoom - r - 1),
                                   fill=(128, 128, 128))
        for u in range(len(the_path)-1):
            y = the_path[u][0]*zoom + int(zoom/2)
            x = the_path[u][1]*zoom + int(zoom/2)
            y1 = the_path[u+1][0]*zoom + int(zoom/2)
            x1 = the_path[u+1][1]*zoom + int(zoom/2)
            draw.line((x,y,x1,y1), fill=(255, 0, 255), width=5)
        draw.rectangle((0, 0, zoom * len(a[0]), zoom * len(a)), outline=(0, 255, 0), width=2)
        images.append(im)

                                                                 
    class Node(): #clase de nodo 
        

        def __init__(self, parent=None, position=None):
            self.parent = parent
            self.position = position

            self.g = 0 #valor distancia entre curr y start
            self.h = 0 #valor distancia entre curr y end
            self.f = 0 #valor G+H

        def __eq__(self, other):
            return self.position == other.position


    def astard(maze, start, end):#retorna una lista de tuplas como un path del comienzo al fin

        # Creacion de nodos de inicio y fin
        start_node = Node(None, start)
        start_node.g = start_node.h = start_node.f = 0
        end_node = Node(None, end)
        end_node.g = end_node.h = end_node.f = 0

        # Se crean las listas de abierto y cerrado
        open_list = []
        closed_list = []

        # Se hace append al nodo de inicio oara agregarlo a la lista abierta
        open_list.append(start_node)

        
        while len(open_list) > 0: #se inicia el loop hasta que se encuentra el final
            
            # como el nodo inicial esta ya en la lista se define como current node 
            current_node = open_list[0]
            current_index = 0 #posicion 0 del index
            for index, item in enumerate(open_list):
                if item.f < current_node.f: 
                    current_node = item
                    current_index = index

            # Pop current de open list, agregar a closed list
            open_list.pop(current_index) 
            closed_list.append(current_node)

            # Se encontro el final por lo que se retorna el camino inverso
            if current_node == end_node:
                path = []
                current = current_node
                while current is not None:
                    path.append(current.position)
                    current = current.parent
                return path[::-1] 

            # Se generan los nodos hijos
            children = []
            for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: #representan las posiciones adyacentes

                # Get de la posicion 
                node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

                # Se verifica que esta dentro del rango de la maze
                if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                    continue

                # Se verifica que sean posiciones permitidas 
                if maze[node_position[0]][node_position[1]] != 0:
                    continue

                # Se crea nodo nuevo
                new_node = Node(current_node, node_position)

                # Append al nodo nuevo
                children.append(new_node)

            #Loop de los hijos
            for child in children:

                # El hijo se encuentra en la closed list
                for closed_child in closed_list:
                    if child == closed_child:
                        continue

                # Se crean los valores g h y f 
                child.g = current_node.g + 1
                child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
                child.f = child.g + child.h

                
                for open_node in open_list:
                    if child == open_node and child.g > open_node.g:
                        continue

                # Se agrega hijo a openlist
                open_list.append(child)
                print(open_list)



    maze = a

    start = starts
    end = ends

    path = astard(maze, start, end)
    draw_matrix(maze,start[0],start[1],end[0],end[1],path)


    images[0].save('mazeastar.gif',
       save_all=True, append_images=images[1:],
       optimize=False, duration=1, loop=0)
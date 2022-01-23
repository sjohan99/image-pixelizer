import math
from random import randint

import numpy as np

from PIL import Image

SIZE = 500
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
AMOUNT_OF_SEEDS = 15

new_image = Image.new('RGB', (SIZE, SIZE), (255, 255, 255))


def random_color():
    return randint(0, 255), randint(0, 255), randint(0, 255)


def color_dict(amount):
    return {i: random_color() for i in range(1, amount+1)}


d = color_dict(AMOUNT_OF_SEEDS)

original_seeds = []
for i in range(AMOUNT_OF_SEEDS):
    original_seeds.append((randint(0, SIZE-1), randint(0, SIZE-1)))


def JFA_Voronoi(row, col, seedlist):
    """

    author: bentdough @ github, modified by sjohan99

    Create Voronoi Diagram Utalizing an implementation
    of the Jump Flood Algorithm that does not use GPU

    row:
        x-axis resolution (how many points desired in x-axis)
    col:
        y-axis resolution (how many points desired in y-axis)
    seedlist:
        list of seed points [[x-coord, ycoord]]

    """

    # Dictionary = Key: Value of a point in arr1 (Corresponding to Color) ->
    # Value: Origin point of that color value (Original Voronoi Site)
    seeds = {}

    # graph to be filled in with Voronoi Diagram
    arr1 = np.zeros((row, col))

    # list of already filled points (Current Voronoi Sites)
    arrlisted = []

    # setting initial step length to half the dimensions of the grid
    step = col // 2

    # divides the color limit of the graph by the number of intial seeds (Voronoi Sites)
    # this is the distance between each color value
    numpoint = 1

    # Filling arrlisted, calculates and assigns color value, inputs this data to
    # seeds and arr1
    for i, point in enumerate(seedlist):
        arrlisted.append(point)
        value = numpoint
        seeds.update({value: point})
        numpoint += 1
        arr1[point[0], point[1]] = value

    # array used to efficiently look at a points neighbors
    moves = [1, -1, 0]

    # JFA adapted to create Voronoi Diagrams
    while step > 0:

        # loop through each filled site (Voronoi Sites)
        for seed in arrlisted:
            x = seed[0]
            y = seed[1]
            val = arr1[x, y]

            # loop through each of this points 8 neighbors at a certain distance away
            for i in moves:
                for j in moves:
                    a = x + (step * i)
                    b = y + (step * j)

                    # if this neighbor point is within the bounds of the graph
                    if 0 <= a < row and 0 <= b < col:

                        # if this neighbor point is not equal to the Voronoi Site it is
                        # the neighbor of
                        if arr1[a, b] != val:

                            # if this neighbor point is empty -> fill and add to arrlisted
                            if arr1[a, b] == 0:
                                arr1[a, b] = val
                                arrlisted.append([a, b])

                            # else -> compute the distances from this neighbor point and
                            # its current origin point as well as from this neighbor point
                            # to the current Voronoi Site's origin point (in dictionary; seeds)
                            else:
                                #location of seed associated with this points value
                                loc1 = seeds[arr1[a, b]]
                                #location of the seed trying to replace this points value
                                loc2 = seeds[val]
                                #Calculating Distances
                                #distance from seed already connected to this point to the point
                                dist1 = math.sqrt(((loc1[0] - a) ** 2) + ((loc1[1] - b) ** 2))
                                #distance  from seed trying to replace previous to this point
                                dist2 = math.sqrt(((loc2[0] - a) ** 2) + ((loc2[1] - b) ** 2))
                                #if dist2 is less than dist1, change the points value to that new seeds value
                                #else do nothing at this point
                                if dist2 < dist1:
                                    arr1[a, b] = val

        step //= 2

    # Create image
    for x, arr in enumerate(arr1):
        for y, val in enumerate(arr):
            new_image.putpixel((x, y), d[val])

JFA_Voronoi(SIZE, SIZE, original_seeds)
new_image.show()
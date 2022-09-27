
import numpy as np
from typing import List,Tuple
import pygame as pg
import copy
import enum
import random
import matplotlib.pyplot as plt
import scipy.signal
width = 450


def start_window():
    pg.init()
    win = pg.display.set_mode((500,500))
    pg.display.set_caption("Dot sampling window")
    run = True
    lst_of_objects = []
    while run:
        # obsługa zdarzeń 
        for event in pg.event.get():
            # print(event)
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.MOUSEBUTTONDOWN:
                t = True
                x = pg.mouse.get_pos()
                for n,i in enumerate(lst_of_objects):
                    if np.sqrt((i[0]-x[0])**2 + (i[1] - x[1])**2) < 6:
                        lst_of_objects.pop(n)
                        t = False
                if t:
                    lst_of_objects.append(pg.mouse.get_pos())
        #############Obiekty 
        win.fill((0,0,0))
        ############ display
        for i in lst_of_objects:
            pg.draw.circle(win,(255,0,0),i,5)
        pg.display.update()
    pg.quit()
    res = [(x-250)+(1j*(y-250)) for x,y in lst_of_objects]
    return res

if __name__ == '__main__':
    start_window()
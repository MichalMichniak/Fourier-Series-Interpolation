import pygame as pg



import numpy as np
from typing import List,Tuple
import pygame as pg
import copy
import enum
import random
import matplotlib.pyplot as plt
import scipy.signal
width = 450

class Part:
    def __init__(self, amplitude_, omega_, angle_) -> None:
        self.amplitude = amplitude_
        self.omega = omega_
        self.angle = angle_
        pass

    def update(self,d):
        self.angle += self.omega*d

    def get_vect(self):
        return self.amplitude*np.cos(self.angle),self.amplitude*np.sin(self.angle)
    
class Body:
    def __init__(self,x_,y_) -> None:
        self.part_lst : List[Part]= []
        self.x = x_
        self.y = y_
        pass

    def add_part(self, part : Part):
        self.part_lst.append(part)
        pass

    def add_part(self, amplitude_,omega_,angle_):
        self.part_lst.append(Part(amplitude_,omega_,angle_))

    def update(self, d):
        for i in self.part_lst: i.update(d)

    def get_coords(self):
        temp = []
        temp.append((self.x,self.y))
        for i in self.part_lst:
            t = i.get_vect()
            temp.append((temp[-1][0]+t[0],temp[-1][1]+t[1]))
        return temp
def DFT(x: np.array, w0: float):
    result = []
    x_len = len(x)
    for k in range(x_len):
        result.append(np.sum(x[:,1]*np.exp(-(1/w0)*k*np.array([i for i in range(len(x))])*1j *2*np.pi/x_len)))
    return np.array(result)[:int(len(x)/2)] ,w0*np.array([i for i in range(len(x))])[:int(len(x)/2)]
class State_of_window(enum.Enum):
    symulation = 1
    drawing = 2

pg.init()
win = pg.display.set_mode((1000,500))
pg.display.set_caption("g")
run = True
main_body = Body(200,250)
T = 1
sampling_iter = 0
sampling_iter2 = 0
w0 = 4
A = 50
speed = 0.01
## aby odczytywać cos faza +np.pi/2
## aby odczytywać sin faza +0
## sygnał trójkątny bipolarny
"""
for i in range(0,20):
    main_body.add_part((A*2/np.pi)/(1+i),(1+i)*w0,0)#+np.pi/2
"""
## sygnał prostokąty:

for i in range(0,10):
    main_body.add_part((A*4/np.pi)/(1+2*i),(1+2*i)*w0,0)

##




state = State_of_window.symulation
k = (width+2, main_body.get_coords()[-1][1])
arr = np.array([k for i in range(1500)])
arr_samples = np.array([k for i in range(1500)])
arr2 = np.array([main_body.get_coords()[-1] for i in range(3000)])
while run:
    # obsługa zdarzeń 
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        
    #############count DFT

    #############Obiekty 
    win.fill((0,0,0))
    if(state == State_of_window.symulation):
        main_body.update(speed)
        if sampling_iter2 == 2:
            sampling_iter2 = 0
            arr = np.array([(i[0]+1,i[1]) for i in arr])
            arr_samples = np.array([(i[0]+1,i[1]) for i in arr_samples])
            arr[1:] = arr[:-1]
            arr[0] = (width+2, main_body.get_coords()[-1][1])
        if sampling_iter == T:
            sampling_iter = 0
            arr_samples[1:] = arr_samples[:-1]
            arr_samples[0] = (width+2, main_body.get_coords()[-1][1])
        arr2[1:] = arr2[:-1]
        arr2[0] = main_body.get_coords()[-1]
        sampling_iter +=1
        sampling_iter2 +=1
        #### display
        t = (i for i in main_body.get_coords())
        prev = next(t)
        for i in t:
                pg.draw.line(win,(255,255,255),prev,i)
                prev = i
        for i in range(len(arr2)-1):
            pg.draw.line(win,(255,255,255),arr2[i],arr2[i+1])
        pg.draw.line(win,(255,255,255),main_body.get_coords()[-1],(width,main_body.get_coords()[-1][1]))
        pg.draw.rect(win, (0,0,0), (width, 0, 1000-width, 500))

        for i in range(len(arr)-1):
            pg.draw.line(win,(255,255,255),arr[i],arr[i+1])
        for i in range(len(arr_samples)):
            pg.draw.circle(win,(255,0,0),arr_samples[i],1)
        pg.draw.line(win,(255,255,0),(width,0),(width,500))
        if(arr_samples[-1][1] != k[1]):
            pg.draw.rect(win, (0,255,0), (0, 0, 25, 25))
    pg.display.update()
pg.quit()
t = DFT(arr_samples,w0)
plt.plot(t[1]/150,np.array([np.linalg.norm(i) for i in t[0]]))#
plt.yscale("log")
plt.xlim([0,w0*len(t[1])/150])
plt.show()
print(scipy.signal.find_peaks(t[0]))




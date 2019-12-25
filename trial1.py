from tkinter import *
import nltk as mahedi
from PIL import ImageTk, Image


def check(x,y):
    x1 = x.split(" ") #submitted answer
    y1 = y.split(" ") #actual answer
    xlen = len(x1)
    ylen = len(y1)
    if ylen == 2:
        ye = edits1(y1[0])
        ye.add(y1[0])
        for i in ye:
            if i in x1:
                return True
    elif ylen == 3:
        counter = 0
        ye = edits1(y1[0])
        ye.add(y1[0])
        ye1 = edits1(y1[1])
        ye1.add(y1[1])
        for i in ye:
            if i in x1:
                counter += 1
                break
        for j in ye1:
            if j in x1:
                counter += 1
                break
        if counter >= 1:
            return True
    else:
        counter = 0
        ye = edits1(y1[ylen-2])
        ye.add(y1[ylen-2])
        ye1 = edits1(y1[ylen-3])
        ye1.add(y1[ylen-3])
        for i in ye:
            if i in x1:
                counter += 1
                break
        for j in ye1:
            if j in x1:
                counter += 1
                break
        if counter == 2:
            return True
    return False
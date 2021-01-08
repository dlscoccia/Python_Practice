#!/usr/bin/python3
from PIL import Image
import os, sys

path = "/home/dlscoccia/Repositories/Python-Test/images/"
dirs = os.listdir( path )

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((600,600))
            imResize.save(f + ' resized.jpg', 'JPEG', quality=90)

resize()

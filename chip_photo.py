import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from PIL import Image

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

img = mpimg.imread('chip.png')     
gray = rgb2gray(img)    
plt.imshow(gray, cmap = plt.get_cmap('gray'))
plt.show()
gray.shape
gray = gray * 255
numbers = []
'''for i in gray[:,20].any():
    if i not in number:
        number.append(i) '''
gray = gray.astype(int)
gray_target = gray[200:900,:]
print(gray_target.shape)
for i in range(700):
    for j in range(564):
        number = gray_target[i,j]
        if number not in numbers:
            numbers.append(number)
numbers = np.array(numbers)
numbers = numbers / 10
numbers = numbers.astype(int)
type_area = []
for i in numbers:
    if i not in type_area:
        type_area.append(i)
print(type_area)

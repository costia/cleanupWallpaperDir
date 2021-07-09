import os
import numpy as np
from PIL import Image

dirName = r'C:\Users\Costia\Pictures\Saved Wallpapers'
smallName = r'C:\Users\Costia\Documents\cofeePy\smallImage'
arName = r'C:\Users\Costia\Documents\cofeePy\aspectRatio'

minMP = 1024**2
requiredAspectRatio = 16/9

fileList=os.listdir(dirName)
fileList = list(filter(lambda x: os.path.isfile(dirName+'/'+x),fileList))
imageSizes=[]
smallImages = []
badAspectRatio = []
for fileName in fileList:
    im = Image.open(dirName+'/'+fileName)
    currentMP = im.size[0]*im.size[1]
    aspectRatio = im.size[0]/im.size[1]
    if currentMP<minMP:
        smallImages.append(fileName)
    elif abs(aspectRatio-requiredAspectRatio)/requiredAspectRatio>0.1:
        badAspectRatio.append(fileName)
    imageSizes.append([fileName,im.size])

print(f'Found {len(smallImages)} small images')
for fileName in smallImages:
    os.rename(dirName+'/'+fileName,smallName+'/'+fileName)

print(f'Found {len(badAspectRatio)} bad aspect ratio images')
for fileName in badAspectRatio:
    os.rename(dirName+'/'+fileName,arName+'/'+fileName)


print('Done')

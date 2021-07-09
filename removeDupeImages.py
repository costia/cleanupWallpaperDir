import os
import shutil
import hashlib

dirName = r'C:\Users\Costia\Pictures\Saved Wallpapers'
dupsPath = r'C:\Users\Costia\Documents\cofeePy\dups'
diffMd5dir = r'C:\Users\Costia\Documents\cofeePy\diffMD5'

fileList=os.listdir(dirName)
fileList = list(filter(lambda x: os.path.isfile(dirName+'/'+x),fileList))
fileSizes={}
duplicates=[]
for fileName in fileList:
    fileSize = os.path.getsize(dirName+'/'+fileName)
    if fileSize in fileSizes:
        duplicates.append([fileSizes[fileSize],fileName])
    else:
        fileSizes[fileSize]=fileName

print(f'Found {len(duplicates)} potential duplicates')


def isDuplicate(filePair):
    hash_md5 = hashlib.md5()
    f = open(dirName+'/'+filePair[0],'rb')
    while data:=f.read(1024**2):
        hash_md5.update(data)
    f.close()
    md5_1=hash_md5.hexdigest()

    hash_md5 = hashlib.md5()
    f = open(dirName+'/'+filePair[1],'rb')
    while data:=f.read(1024**2):
        hash_md5.update(data)
    f.close()
    md5_2=hash_md5.hexdigest()

    return md5_1==md5_2

diffMD5 = list(filter(lambda x: not isDuplicate(x),duplicates))
duplicates = list(filter(lambda x: isDuplicate(x),duplicates))

print(f'Found {len(duplicates)} duplicates with matching MD5')
for filePair in duplicates:
    print(filePair)
    shutil.copyfile(dirName+'/'+filePair[0],dupsPath+'/'+filePair[0])
    os.rename(dirName+'/'+filePair[1],dupsPath+'/'+filePair[1])

print(f'Found {len(diffMD5)} "duplicates" with different MD5')
for filePair in diffMD5:
    print(filePair)
    shutil.copyfile(dirName+'/'+filePair[0],diffMd5dir+'/'+filePair[0])
    shutil.copyfile(dirName+'/'+filePair[1],diffMd5dir+'/'+filePair[1])

print('Done')

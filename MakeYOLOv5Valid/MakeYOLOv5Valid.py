from pathlib import Path
import sys
import shutil

imagesDir = 'images'
labelsDir = 'labels'

trainPath = Path(sys.argv[1])
trainImagePath = trainPath / imagesDir
trainLabelPath = trainPath / labelsDir

validPath = trainPath.parent / 'valid'
validImagePath = validPath / imagesDir
validLabelPath = validPath / labelsDir

# valid 경로 생성
validPath.mkdir(exist_ok=True)
validImagePath.mkdir(exist_ok=True)
validLabelPath.mkdir(exist_ok=True)

# Copy
jpgList = list(trainImagePath.glob('*.jpg'))
copyRepeat = len(list(jpgList)) // 4

for i in range(copyRepeat) :
    name = jpgList[i].stem
    nameJpg = f"{name}.jpg"
    nameTxt = f"{name}.txt"

    trainJpg = trainImagePath / nameJpg
    trainTxt = trainLabelPath / nameTxt
    validJpg = validImagePath / nameJpg
    validTxt = validLabelPath / nameTxt

    shutil.move(trainImagePath / nameJpg, validImagePath / nameJpg)
    shutil.move(trainLabelPath / nameTxt, validLabelPath / nameTxt)

# 대상 디렉토리를 train으로 이름 변경
if trainPath.name != 'train' :
    trainPath = trainPath.rename(trainPath.parent / 'train')
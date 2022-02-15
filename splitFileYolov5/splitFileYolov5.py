import argparse
from ast import parse
from pathlib import Path
import sys
import shutil

imagesDir = 'images'
labelsDir = 'labels'

parser = argparse.ArgumentParser(description=
    "YOLOv5 Image Splitter \n Train Ratio + Valid Ratio + Test Ratio = 1"
)

parser.add_argument('--trainPath', '-p',
    help='train path on images and labels')
parser.add_argument('--trainRatio', '-t', type=float,
    help='Train Ratio for images and labels')
parser.add_argument('--validRatio', '-v', type=float,
    help='Valid Ratio for images and labels')
parser.add_argument('--testRatio', '-te', type=float, default=0,
    help='Test Ratio for images and labels')

args = parser.parse_args()
trainPath = Path(args.trainPath)
trainRatio = args.trainRatio
validRatio = args.validRatio
testRatio = args.testRatio

if trainRatio + validRatio + testRatio != 1 :
    sys.exit('Sum of ratios is not 1')

dataSetPath = trainPath.parent
# trainPath = ...
trainImagePath = trainPath / imagesDir
trainLabelPath = trainPath / labelsDir

validPath = dataSetPath / 'valid'
validImagePath = validPath / imagesDir
validLabelPath = validPath / labelsDir

# valid 경로 생성
validPath.mkdir(exist_ok=True)
validImagePath.mkdir(exist_ok=True)
validLabelPath.mkdir(exist_ok=True)

if trainRatio == 1 :
    testPath = dataSetPath / 'test'
    testImagePath = testPath / imagesDir
    testLabelPath = testPath / labelsDir
    
    #test 경로 생성
    testPath.mkdir(exist_ok=True)
    testImagePath.mkdir(exist_ok=True)
    testLabelPath.mkdir(exist_ok=True)


jpgList = list(trainImagePath.glob('*.jpg'))

allCount = len(list(jpgList))
otherRepeat = int(allCount * (validRatio + testRatio))
validReapeat = int(allCount * validRatio)

# 겹치지 않게 랜덤
import random
ran = random.sample(range(0, allCount - 1), otherRepeat)

for i in range(validReapeat) :
    name = jpgList[ran[i]].stem
    nameJpg = f"{name}.jpg"
    nameTxt = f"{name}.txt"

    trainJpg = trainImagePath / nameJpg
    trainTxt = trainLabelPath / nameTxt
    validJpg = validImagePath / nameJpg
    validTxt = validLabelPath / nameTxt

    shutil.move(trainImagePath / nameJpg, validImagePath / nameJpg)
    shutil.move(trainLabelPath / nameTxt, validLabelPath / nameTxt)

for i in range(validReapeat, otherRepeat) :
    name = jpgList[ran[i]].stem
    nameJpg = f"{name}.jpg"
    nameTxt = f"{name}.txt"

    trainJpg = trainImagePath / nameJpg
    trainTxt = trainLabelPath / nameTxt
    testJpg = testImagePath / nameJpg
    testTxt = testLabelPath / nameTxt

    shutil.move(trainImagePath / nameJpg, testImagePath / nameJpg)
    shutil.move(trainLabelPath / nameTxt, testLabelPath / nameTxt)

# 대상 디렉토리를 train으로 이름 변경
if trainPath.name != 'train' :
    trainPath = trainPath.rename(trainPath.parent / 'train')
import argparse
from pathlib import Path
import sys
import shutil

parser = argparse.ArgumentParser(description=
    "YOLOv5 Image Splitter \n Train Ratio + Valid Ratio + Test Ratio = 1"
)

parser.add_argument('--trainPath', '-p',
    help='path on images and labels, this is changed to \'train\' directory')
parser.add_argument('--trainRatio', '-t', type=float, default=0.6
    help='Train Ratio for images and labels')
parser.add_argument('--validRatio', '-v', type=float, default=0.2,
    help='Valid Ratio for images and labels')
parser.add_argument('--testRatio', '-te', type=float, default=0.2,
    help='Test Ratio for images and labels')
parser.add_argument('--imageType', '-it', type=str,
    help='data image type')

args = parser.parse_args()
trainPath = Path(args.trainPath)
trainRatio = args.trainRatio
validRatio = args.validRatio
testRatio = args.testRatio
imageType = args.imageType

if trainRatio + validRatio + testRatio != 1 :
    sys.exit('Sum of ratios is not 1')

dataSetPath = trainPath.parent

# trainPath = ...

# valid 경로 생성
validPath = dataSetPath / 'valid'
validPath.mkdir(exist_ok=True)

#test 경로 생성
testPath = dataSetPath / 'test'
testPath.mkdir(exist_ok=True)


imageList = list(trainPath.glob(f'*.{imageType}'))

allCount = len(list(imageList))
otherRepeat = int(allCount * (validRatio + testRatio))
validReapeat = int(allCount * validRatio)

# 겹치지 않게 랜덤
import random
ran = random.sample(range(0, allCount - 1), otherRepeat)

for i in range(validReapeat) :
    name = imageList[ran[i]].stem
    namepng = f"{name}.{imageType}"
    nameTxt = f"{name}.txt"

    trainpng = trainPath / namepng
    trainTxt = trainPath / nameTxt
    validpng = validPath / namepng
    validTxt = validPath / nameTxt

    shutil.move(trainPath / namepng, validPath / namepng)
    shutil.move(trainPath / nameTxt, validPath / nameTxt)

for i in range(validReapeat, otherRepeat) :
    name = imageList[ran[i]].stem
    namepng = f"{name}.{imageType}"
    nameTxt = f"{name}.txt"

    trainpng = trainPath / namepng
    trainTxt = trainPath / nameTxt
    testpng = testPath / namepng
    testTxt = testPath / nameTxt

    shutil.move(trainPath / namepng, testPath / namepng)
    shutil.move(trainPath / nameTxt, testPath / nameTxt)

# 대상 디렉토리를 train으로 이름 변경
if trainPath.name != 'train' :
    trainPath = trainPath.rename(trainPath.parent / 'train')
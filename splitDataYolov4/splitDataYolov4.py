import argparse
from pathlib import Path
import sys
import shutil

parser = argparse.ArgumentParser(description=
    "YOLOv5 Image Splitter \n Train Ratio + Valid Ratio + Test Ratio = 1"
)

parser.add_argument('--dataPath', '-p',
    help='path on images and labels, this is changed to \'train\' directory')
parser.add_argument('--trainRatio', '-t', type=float, default=0.7,
    help='Train Ratio for images and labels')
parser.add_argument('--validRatio', '-v', type=float, default=0.3,
    help='Valid Ratio for images and labels')
parser.add_argument('--testRatio', '-te', type=float, default=0,
    help='Test Ratio for images and labels')
parser.add_argument('--imageType', '-it', type=str,
    help='data image type')
parser.add_argument('--classTxt', '-ct', type=str, default='classes.txt',
    help='txt file for classes')


def main() :
    args = parser.parse_args()
    trainPath = Path(args.dataPath)
    trainRatio = args.trainRatio
    validRatio = args.validRatio
    testRatio = args.testRatio
    imageType = args.imageType
    classTxt = Path(args.classTxt)
    
    print(f'{trainRatio} : {validRatio} : {testRatio}')
    if trainRatio + validRatio + testRatio != 1 :
        sys.exit('Sum of ratios is not 1')

    global dataSetPath
    dataSetPath = trainPath.parent

    matchingFileChecker(dirPath=trainPath, firstFileExtension=imageType, secondFileExtension='txt', exclude=args.classTxt)

    imageList = list(trainPath.glob(f'*.{imageType}'))

    allCount = len(list(imageList))
    otherRepeat = int(allCount * (validRatio + testRatio))
    validRepeat = int(allCount * validRatio)

    # 겹치지 않게 랜덤
    import random
    ran = random.sample(range(0, allCount - 1), otherRepeat)

    # trainPath = ...

    # valid 경로 생성
    validPath = dataSetPath / 'valid'
    validPath.mkdir(exist_ok=True)

    validImageList = []
    shutil.copy(trainPath / classTxt, validPath / classTxt)
    for i in range(validRepeat) :
        name = imageList[ran[i]].stem
        validImagePath = copyFilePair(start=trainPath, destination=validPath, name=name, pairType1=imageType, pairType2='txt')
        validImageList.append(str(validImagePath.absolute()))
    
    validTxtPath = writePathTxt(pathList=validImageList, savedTxtName='valid.txt')

    testImageList = []
    testTxtPath = Path('')
    if testRatio :
        #test 경로 생성
        testPath = dataSetPath / 'test'
        testPath.mkdir(exist_ok=True)

        shutil.copy(trainPath / classTxt, testPath / classTxt)
        for i in range(validRepeat, otherRepeat) :
            name = imageList[ran[i]].stem
            testImagePath = copyFilePair(start=trainPath, destination=testPath, name=name, pairType1=imageType, pairType2='txt')
            testImageList.append(str(testImagePath.absolute()))
        
        testTxtPath = writePathTxt(pathList=testImageList, savedTxtName='test.txt')

    # train 디렉토리의 주소 경로를 적기 전에 대상 디렉토리를 train으로 이름 변경
    if trainPath.name != 'train' :
        trainName = trainPath.parent / 'train'
        trainPath.rename(trainName)
        trainPath = trainName

    trainpngList = list(trainPath.glob(f'*.{imageType}'))
    for i in range(len(trainpngList)) :
        trainpngList[i] = str(trainpngList[i].absolute())

    trainTxtPath = writePathTxt(pathList=trainpngList, savedTxtName='train.txt')

    # classes.txt -> obj.names
    namesPath = dataSetPath / Path('obj.names')
    classNum = 0
    with open(trainPath / classTxt, mode='r', encoding='utf-8') as f :
        longLine = f.read()
        lines = list(filter(None, longLine.split('\n')))
        classNum = len(lines)
        print(f"classes : {classNum}")
        print(longLine)
        
        with open(namesPath, mode='w', encoding='utf-8') as f :
            longLine = '\n'.join(lines)
            f.write(longLine)

    # obj.data
    dataPath = dataSetPath / Path('obj.data')
    with open(dataPath, mode='w', encoding='utf-8') as f :
        f.write(f"classes = {classNum}\n" \
                f"train = {trainTxtPath.absolute()}\n" \
                f"valid = {validTxtPath.absolute()}\n" \
                f"names = {namesPath.absolute()}\n" \
                f"backup = backup\n")

    print('Success')


def matchingFileChecker(dirPath, firstFileExtension, secondFileExtension, exclude = '') :
    firstFileList = list(dirPath.glob(f'*.{firstFileExtension}'))
    secondFileList = list(dirPath.glob(f'*.{secondFileExtension}'))

    soloList = []
    for file in firstFileList :
        filePath = dirPath / Path(f'{file.stem}.{secondFileExtension}')
        if not filePath.is_file() :
            fileNameStr = str(file.name)
            if fileNameStr == exclude :
                continue
            soloList.append(str(file.name))
            print(f'{filePath} is not matched')

    for file in secondFileList :
        filePath = dirPath / Path(f'{file.stem}.{firstFileExtension}')
        if not filePath.is_file() :
            fileNameStr = str(file.name)
            if fileNameStr == exclude :
                continue
            soloList.append(str(file.name))
            print(f'{filePath} is not matched')

    if len(soloList) :
        print('Not Matched : ', soloList)
        sys.exit('Check your files again')

    print('OK, FILE CHECK COMPLETE \n')


def writePathTxt(pathList, savedTxtName) :
    pathStr = '\n'.join(pathList)
    txtPath = dataSetPath / Path(savedTxtName)
    txtPath.write_text(pathStr)
    # print(savedTxtName)
    # print(pathStr)
    return txtPath


def copyFilePair(start, destination, name, pairType1, pairType2) :
    pair1Fullname = f"{name}.{pairType1}"
    pair2Fullname = f"{name}.{pairType2}"

    startPair1 = start / pair1Fullname
    startPair2 = start / pair2Fullname
    destinationPair1 = destination / pair1Fullname
    destinationPair2 = destination / pair2Fullname

    shutil.move(startPair1, destinationPair1)
    shutil.move(startPair2, destinationPair2)

    return destinationPair1


if __name__ == "__main__":
    main()
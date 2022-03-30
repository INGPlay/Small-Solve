import argparse
from pathlib import Path

parser = argparse.ArgumentParser(description=
    "Filename checker for matching name with other extension"
)

parser.add_argument('--dirPath', '-d',
    help='Directory Path')
parser.add_argument('--firstExtension', '-fe',
    help='matching file extension')
parser.add_argument('--secondExtension', '-se',
    help='matching file extension')

args = parser.parse_args()
dirPath = Path(args.dirPath)
firstFileExtension = args.firstExtension
secondFileExtension = args.secondExtension

firstFileList = list(dirPath.glob(f'*.{firstFileExtension}'))
secondFileList = list(dirPath.glob(f'*.{secondFileExtension}'))

soloList = []
for file in firstFileList :
    filePath = dirPath / Path(f'{file.stem}.{secondFileExtension}')
    if not filePath.is_file() :
        soloList.append(str(file.name))
        print(f'{filePath} is not matched')

for file in secondFileList :
    filePath = dirPath / Path(f'{file.stem}.{firstFileExtension}')
    if not filePath.is_file() :
        soloList.append(str(file.name))
        print(f'{filePath} is not matched')

print(soloList)
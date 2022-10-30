import pandas as pd
import glob
import argparse
from tqdm import tqdm
from multiprocessing import Pool

parser = argparse.ArgumentParser(description='get combined csv')

parser.add_argument("--paths", "-p", help= "target csv paths \n ex) *.csv")
parser.add_argument("--output_path", "-op", help= "output csv path \n ex) output.csv")
parser.add_argument("--encode", "-e", default= "cp949", help= "target csv encoding")
parser.add_argument("--output_encode", "-oe", default="utf-8-sig", help= "output encoding")
parser.add_argument("--process_count", "-pc", default= 4, type= int, help= "process for multiprocessing \n ex) 4")

args = parser.parse_args()

paths = args.paths
output_path = args.output_path
encode = args.encode
output_encode = args.output_encode
processes = args.process_count

# 병렬처리에 사용할 함수
def combine_csv(file_name) :
    result = pd.read_csv(file_name, encoding= encode)
    return result

if __name__ == '__main__':
    # 경로의 파일을 가져옴
    all_filenames = [x for x in glob.glob(paths)]
    # 병렬처리
    pool = Pool(processes= processes)
    combined_csv = pd.concat(pool.map(combine_csv, tqdm(all_filenames)))
    pool.close(); pool.join()
    
    # 결합된 csv 저장
    combined_csv.to_csv(output_path, index= False, encoding= output_encode)
    
    print("Complete!")
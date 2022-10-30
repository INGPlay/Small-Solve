import os
import zipfile
import argparse
from tqdm import tqdm
from multiprocessing import Pool

parser = argparse.ArgumentParser(description='unzip')

parser.add_argument("--zip_file", "-z", help= "target zip paths \n ex) archive.zip")
parser.add_argument("--process_count", "-pc", default= 4, type= int, help= "process for multiprocessing \n ex) 4")

args = parser.parse_args()
zip_path = args.zip_file
processes = args.process_count

output_dir = os.path.splitext(zip_path)[0]
zf = zipfile.ZipFile(zip_path, 'r')
def unzip(member) :
    member.filename = member.filename.encode('cp437').decode('euc-kr')
    zf.extract(member, path= output_dir)

if __name__ == '__main__':
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    # 병렬처리
    pool = Pool(processes= processes)
    pool.map(unzip, tqdm(zf.infolist()))
    pool.close(); pool.join()
    
    print("Complete!")
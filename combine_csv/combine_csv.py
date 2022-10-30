import pandas as pd
import glob
import argparse
from tqdm import tqdm
from multiprocessing import Pool

parser = argparse.ArgumentParser(description='get csv')

parser.add_argument("--paths", "-p", help= "target csv paths \n ex) *.csv")
parser.add_argument("--output_path", "-op", help= "output csv path \n ex) output.csv")
parser.add_argument("--encode", "-e", default= "cp949", help= "target csv encoding")
parser.add_argument("--output_encode", "-oe", default="utf-8", help= "output encoding")
parser.add_argument("--process_count", "-pc", default= 4, type= int, help= "process for multiprocessing")

args = parser.parse_args()

def combine_csv(all_filename) :
    result = pd.read_csv(all_filename, encoding= args.encode)
    return result

if __name__ == '__main__':
    all_filenames = [x for x in glob.glob(args.paths)]
    pool = Pool(processes= args.process_count)
    combine_csv = pd.concat(pool.map(combine_csv, tqdm(all_filenames)))
    pool.close()
    pool.join()
    
    combine_csv.to_csv(args.output_path, index= False, encoding= args.output_encode)
    print("Complete!")
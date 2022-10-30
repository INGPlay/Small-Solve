import pandas as pd
import glob
from tqdm import tqdm
import argparse

parser = argparse.ArgumentParser(description='get csv')

parser.add_argument("--paths", "-p", help= "target csv paths \n ex) *.csv")
parser.add_argument("--output_path", "-op", help= "output csv path \n ex) output.csv")
parser.add_argument("--encode", "-e", default= "cp949", help= "target csv encoding")
parser.add_argument("--output_encode", "-oe", default="utf-8", help= "output encoding")

args = parser.parse_args()

all_filenames = [i for i in glob.glob(args.paths)]
combine_csv = pd.concat([pd.read_csv(x, encoding= args.encode) for x in tqdm(all_filenames)])
combine_csv.to_csv(args.output_path, index= False, encoding= args.output_encode)
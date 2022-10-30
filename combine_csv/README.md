# combine_csv
```bash
python combine_csv.py --paths csv_paths --output_path output_csv_path --encode loaded_csv_encode --output_encode saved_csv_encode --process_count process_for_multiprocessing
```
  
## flag  
--paths, -p  
--output_path, -op 
--encode, -e, cp949
--output_encode, -oe, utf-8-sig
--process_count, -pc, 4
  
  
## feature  
파일별로 하나의 컬럼을 가지는 csv를 모아 하나의 파일로 변환한다
병렬처리를 통하여 속도를 높임
    
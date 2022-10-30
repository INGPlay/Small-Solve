# combine_csv
```bash
python --paths csv_paths --output_path output_csv_path --encode loaded_csv_encode --output_encode saved_csv_encode --process_count process_for_multiprocessing
```
  
## flag  
--paths, -p  
--output_path, -op 
--encode, -e
--output_encode, -oe  
--process_count, -pc
  
  
## feature  
파일별로 하나의 컬럼을 가지는 csv를 모아 하나의 파일로 변환한다
병렬처리를 통하여 속도를 높임
    
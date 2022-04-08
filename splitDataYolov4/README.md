# splitDataYolov4   
```bash
python splitDataYolov4.py --dataPath dataDirPath --trainRatio trainDataRatio --validRatio validDataRatio --testRatio testDataRatio --imageType dataImageType --classTxt classTextFile  
```
  
## flag  
--dataPath, -p,   
--trainRatio, -t, 0.7  
--validRatio, -v, 0.3  
--testRatio, -te 0  
--imageType, -it  
--classTxt, -ct, 'classes.txt'    
  
  
## feature  
### before
   
* splitDataYolov4.py
* ImagesAndLabels   
    * class.txt  
    * (Jpg and Label) * 100  
   
  
```bash
$ python splitDataYolov4.py -p ./ImagesAndLabels -t 0.6 -v 0.2 -te 0.2 -it jpg -ct class.txt  
```
### after
   
* splitDataYolov4.py    
* train.txt  
* valid.txt  
* test.txt  
* obj.names
* obj.data
* train    
    * class.txt  
    * (Jpg and Label) * 60    
* valid   
    * class.txt  
    * (Jpg and Label) * 20    
* test    
    * class.txt  
    * (Jpg and Label) * 20   
    
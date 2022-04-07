# splitDataYolov4   
```bash
python --trainPath trainDirPath --trainRatio trainDataRatio --validRatio validDataRatio --testRatio testDataRatio --imageType dataImageType --classTxt classTextFile  
```
  
## flag  
--trainPath, -p,   
--trainRatio, -t, 0.7  
--validRatio, -v, 0.3  
--testRatio, -te 0  
--imageType, -it  
--classTxt, -ct, 'classes.txt'    
  
  
## feature  
### before
   
* ImagesAndLabels   
    * class.txt  
    * (Jpg and Label) * 100  
   
  
```bash
$ python --trainPath ./ImagesAndLabels -p ./example -t 0.6 -v 0.2 -te 0.2 -it jpg -ct class.txt  
```
### after
     
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
    
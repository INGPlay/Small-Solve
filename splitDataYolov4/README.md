# splitDataYolov5  
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
   
* ImagesAndLabels  
    * (Image and Label) * 100  
   
  
```bash
$ python --trainPath ./ImagesAndLabels -p ./example -t 0.6 -v 0.2 -te 0.2 -it jpg -ct class.txt
```
     
      
* train    
    * (Image and Label) * 60    
* valid   
    * (Image and Label) * 20   
* test   
    * (Image and Label) * 20   
    
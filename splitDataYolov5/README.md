# splitDataYolov5  
```bash
python --trainPath trainDirPath --trainRatio trainDirRatio --validRatio validDirRatio --testRatio testDirRatio
```
  
## flag  
--trainPath, -p  
--trainRatio, -t  
--validRatio, -v  
--testRatio, -te  
  
  
## feature  
   
* ImagesAndLabels  
    * (Image and Label) * 100  
   
   
```bash
$ python --trainPath ./ImagesAndLabels --trainRatio 0.7 --validRatio 0.3
```
    
* train    
    * images  
        * (image) * 70  
    * labels  
        * (labels) * 70   
* valid   
    * images
        * (image) * 30
    * labels
        * (labels) * 30
    
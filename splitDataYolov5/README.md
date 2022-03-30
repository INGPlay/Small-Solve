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
   
ImagesAndLabels  
    (Images and Labels) * 100  
  

```bash
$ python --trainPath ./ImagesAndLabels --trainRatio 0.7 --validRatio 0.3
```
   
train    
    (Images and Labels) * 70    
valid   
    (Images and Labels) * 30  
    
# MatchingFileChecker  
```bash
python --dirPath dirPath --firstExtension fileExtension1 --secondExtension fileExtension2
```
  
## flag  
--dirPath, -d
--firstExtension, -fe
--secondExtension, -se
  
  
## feature  
  
### /directory  
1.txt  
1.jpg  
2.txt  
2.jpg  
3.txt  
4.jpg  
5.txt  
5.jpg  
.  
.  
.  
  
```bash  
python --dirPath /directory --firstExtension txt --secondExtension jpg  
```  
  
print out  
[3.txt, 4.jpg]  

var fs = require('fs');

var text = "test";

fs.writeFile('test.txt', test, 'utf-8', function(e){
    if(e){
        alert("파일을 쓰지 못했습니다!")
    }
})
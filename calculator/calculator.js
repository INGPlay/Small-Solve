const displays = {
  inputDisplay : function() {
    return document.querySelector('#input');
  },
  resultDisplay : function() {
    return document.querySelector('#result');
  }
}

const bools = {
  canSign : false
}

const calculator = {
  inputNum : function(num) {
    displays.inputDisplay().value += num;

    bools.canSign = true;
},

inputSign : function(sign) {
  if (bools.canSign === true) {
    displays.inputDisplay().value += sign;

    bools.canSign = false;
  }
},

deleteNum : function() {
  displays.inputDisplay().value = displays.inputDisplay().value.slice(0, -1);
},

allClear : function() {
  displays.inputDisplay().value = "";
  displays.resultDisplay().value = "";
},

answer : function() {
  const value = ( new Function( 'return ' + displays.inputDisplay().value ) )();
  if (value !== undefined) {
    displays.resultDisplay().value = value;
  }
}
}

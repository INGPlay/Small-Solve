const displays = {
  inputDisplay() {
    return document.querySelector('#input');
  },
  resultDisplay() {
    return document.querySelector('#result');
  }
}

const bools = {
  canSign : false
}

const calculator = {
  inputNum(num) {
    displays.inputDisplay().value += num;

    bools.canSign = true;
},

inputSign(sign) {
  if (bools.canSign === true) {
    displays.inputDisplay().value += sign;

    bools.canSign = false;
  }
},

deleteNum() {
  displays.inputDisplay().value = displays.inputDisplay().value.slice(0, -1);
},

allClear() {
  displays.inputDisplay().value = "";
  displays.resultDisplay().value = "";
},

answer() {
  const value = ( new Function( 'return ' + displays.inputDisplay().value ) )();
  if (value !== undefined) {
    displays.resultDisplay().value = value;
  }
}
}

let form = document.getElementById('form');
let first = document.getElementById('first');
let second = document.getElementById('second');
let add = document.getElementById('add');
let sub = document.getElementById('sub');
let mul = document.getElementById('mul');
let div = document.getElementById('div');
let result = document.getElementById('result');

function operation() {
  let first_num = first.value;
  let second_num = second.value;
  if (first_num == '' || second_num == '') {
    result.innerHTML = 'Enter both values';
  } else {
    if (add.checked) {
      a = parseInt(first_num);
      b = parseInt(second_num);
      result.innerHTML = 'Addition of two number : ' + (a + b);
    } else if (sub.checked) {
      result.innerHTML =
        'Subtraction of two number : ' + (first_num - second_num);
    } else if (mul.checked) {
      result.innerHTML =
        'Multiplication of two number : ' + first_num * second_num;
    } else {
      if (second_num == 0) {
        result.innerHTML = 'Divide by zero';
      } else {
        result.innerHTML = 'Division of two number : ' + first_num / second_num;
      }
    }
  }
}

form.addEventListener('submit', function (e) {
  e.preventDefault();
  operation();
});

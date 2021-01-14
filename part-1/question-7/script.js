let form = document.getElementById('form');
let number = document.getElementById('number');
let result = document.getElementById('result');

function check_divisiblity() {
  let value = number.value;
  if (value % 3 == 0 || value % 7 == 0) {
    result.innerText = 'The number is divisible by 3 or 7';
  } else {
    result.innerText = 'The number is not divisible by 3 or 7';
  }
}

form.addEventListener('submit', (e) => {
  e.preventDefault();
  check_divisiblity();
});

let form = document.getElementById('form');
let cake = document.getElementById('cake');
let cakeQuantity = document.getElementById('cakeQuantity');
let cookie = document.getElementById('cookie');
let cookieQuantity = document.getElementById('cookieQuantity');
let result = document.getElementById('result');

function order() {
  if (cake.checked && cakeQuantity.value > 0) {
    result.innerHTML =
      'The total cost for cake = ' + parseInt(cakeQuantity.value) * 5;
  } else if (cookie.checked && cookieQuantity.value > 0) {
    result.innerHTML =
      'The total cost for cookie = ' + parseInt(cookieQuantity.value) * 10;
  } else {
    alert('Enter a valid quantity');
  }
}

form.addEventListener('submit', function (e) {
  e.preventDefault();
  order();
});

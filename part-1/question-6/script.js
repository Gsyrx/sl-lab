let customer_name = document.getElementById('customer_name');
let other_feedback = document.getElementById('other_feedback');
let male = document.getElementById('male');
let female = document.getElementById('female');
let others = document.getElementById('others');
let customer_gender = document.getElementsByClassName('gender');
let form = document.getElementById('form');
let result_1 = document.getElementById('result_1');
let result_2 = document.getElementById('result_2');
let result_3 = document.getElementById('result_3');

function display() {
  result_1.innerHTML = 'Customer name = ' + customer_name.value;

  if (male.checked) {
    result_2.innerHTML = 'Customer gender = ' + male.value;
  } else if (female.checked) {
    result_2.innerHTML = 'Customer gender = ' + female.value;
  } else {
    result_2.innerHTML = 'Customer gender = ' + others.value;
  }
  result_3.innerHTML = 'Customer feedback = ' + other_feedback.value;
}

form.addEventListener('submit', (e) => {
  e.preventDefault();
  display();
});

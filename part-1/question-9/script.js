let form = document.getElementById('form');
let sentence = document.getElementById('sentence');
let result = document.getElementById('result');
let size = document.getElementById('size');

function longest() {
  let copy_sentence = sentence.value;
  splitted_sentence = copy_sentence.split(' ');
  word = '';
  len = 0;
  for (i = 0; i < splitted_sentence.length; i++) {
    if (len < splitted_sentence[i].length) {
      len = splitted_sentence[i].length;
      word = splitted_sentence[i];
    }
  }
  result.innerHTML = 'Longest word : ' + word;
  size.innerHTML = 'Length of longest word : ' + len;
}

form.addEventListener('submit', function (e) {
  e.preventDefault();
  longest();
});

window.onload = function () {
  let teslaModels = [
    {
      model: 'Model1',
      name: 'Car 1',
      price: 10000,
      year: 2017,
      image: './image-1.png',
    },
    {
      model: 'Model2',
      name: 'Car 2',
      price: 20000,
      year: 2018,
      image: './image-2.png',
    },
    {
      model: 'Model3',
      name: 'Car 3',
      price: 30000,
      year: 2019,
      image: './image-3.png',
    },
  ];

  const name = document.getElementById('name');
  const price = document.getElementById('price');
  const image = document.getElementById('image');
  const year = document.getElementById('year');
  const menu = document.getElementById('menu');

  teslaModels.forEach(function (item, index) {
    listElement = document.createElement('th');

    listElement.onmouseover = function () {
      name.innerHTML = teslaModels[index].name;
      price.innerHTML = teslaModels[index].price;
      year.innerHTML = teslaModels[index].year;
      image.src = teslaModels[index].image;
    };

    listElement.innerHTML = item.name;
    menu.appendChild(listElement);
  });
};

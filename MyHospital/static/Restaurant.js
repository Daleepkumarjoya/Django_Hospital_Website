let menu = document.querySelector('#menu-btn');
let navbar = document.querySelector('.navbar');

menu.onclick = () =>{
menu.classList.toggle('fa-times');
navbar.classList.toggle('active');
}

window.onscroll = () =>{
menu.classList.toggle('fa-times');
navbar.classList.toggle('active');
}

const imgDiv = document.querySelector('upload');
const img = document.querySelector('#photo');
const file = document.querySelector('#file');
const uploadbtn = document.querySelector('#uploadbtn');



file.addEventListener('change', function(){
  const choosedFile = this.files[0];
  if(choosedFile){
   const reader = new FileReader();
   reader.addEventListener('load', function(){
     img.setAttribute('src', reader.result);
});
  reader.readAsDataURL(choosedFile);
}
});

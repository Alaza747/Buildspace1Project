const IMAGES = document.querySelectorAll("img");

for (let i = 0; i<IMAGES.length; i++){
  let ImgSrc = IMAGES[i].getAttribute("src");
  console.log(ImgSrc);
}

// let slideIndex = 0;
// imageSlide()
// function imageSlide() {
//     let i;

//     let images = document.getElementsByClassName("imageSlide");
//     for (i = 0; i < images.length; i++) {
//         images[i].style.display = "none";
//     }
//     slideIndex++;
//     if (slideIndex > images.length) {
//         slideIndex = 1
//     }
//     images[slideIndex - 1].style.display = "block";
//     setTimeout(imageSlide, 3000);
// }

let slideIndex = 0;
imageSlide();

function imageSlide() {
    let i;
    let images = document.getElementsByClassName("imageSlide");
    for (i = 0; i < images.length; i++) {
        images[i].style.display = "none";
    }
    slideIndex++;
    if (slideIndex > images.length) {
        slideIndex = 1;
    }
    images[slideIndex - 1].style.display = "block";
    setTimeout(imageSlide, 3000); // Change image every 3 seconds
}



let scrollAmount = 0;

function slideLeft() {
    const cards = document.getElementsByClassName("cards");
    scrollAmount -= 250;
    cards.style.transform = `translateX(${scrollAmount}px)`;
}
function slideRight() {
    const cards = document.getElementsByClassName("cards");
    scrollAmount += 250;
    cards.style.transform = `translateX(${scrollAmount}px)`;
}
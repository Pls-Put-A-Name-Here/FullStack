function toggleSize() {
  const inputField = document.querySelector(".search-field");
  const isLarge = inputField.classList.contains("show");

  if (isLarge) {
    inputField.classList.remove("show");
  } else {
    inputField.classList.add("show");
  }
}

document.addEventListener("click", function (event) {
  const inputField = document.querySelector(".search-field");
  const inputImg = document.querySelector(".search-btn");
  const isInputFocused =
    inputField === event.target || inputField.contains(event.target);
  const isImgHovered =
    inputImg === event.target || inputImg.contains(event.target);

  if (!isInputFocused && !isImgHovered) {
    inputField.classList.remove("show");
  }
});

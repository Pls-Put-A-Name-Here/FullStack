function toggleSize() {
    var inputField = document.querySelector('.search-field');
    var isLarge = inputField.classList.contains('show');

    if (isLarge) {
        inputField.classList.remove('show');
    } else {
        inputField.classList.add('show');
    }
}

document.addEventListener('click', function(event) {
    var inputField = document.querySelector('.search-field');
    var inputImg = document.querySelector('.search-btn');
    var isInputFocused = inputField === event.target || inputField.contains(event.target);
    var isImgHovered = inputImg === event.target || inputImg.contains(event.target);

    if (!isInputFocused && !isImgHovered) {
        inputField.classList.remove('show');
    }
});
// JS principal

function imageFileHandler(file) {
    const imagePostLabel = document.getElementById("imagePostLabel");
    imagePostLabel.textContent = file[0].name;
}
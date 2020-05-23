document.addEventListener("DOMContentLoaded", function () {

    const realFileButton = document.getElementById("real-file")
    const customButton = document.getElementById("customButton")
    const img = document.getElementById("chosen-image")
    const blockFile = document.getElementById("div-chosen-file")
    const sendButton = document.getElementById("sendButton");

    customButton.addEventListener("click", function () {
        realFileButton.click();
    });

    realFileButton.addEventListener("change", function () {

        let file = getPureFilename(realFileButton.value);
        blockFile.style.display = "block";
        sendButton.click();

        img.src = file;
        if (realFileButton.value) {
        } else {
        }
    });

});

function getPureFilename(fullPath) {
    if (fullPath) {
        var startIndex = (fullPath.indexOf('\\') >= 0 ? fullPath.lastIndexOf('\\') : fullPath.lastIndexOf('/'));
        var filename = fullPath.substring(startIndex);
        if (filename.indexOf('\\') === 0 || filename.indexOf('/') === 0) {
            filename = filename.substring(1);
        }
    }
    return filename;
}
document.addEventListener("DOMContentLoaded", function () {

    const realFileButton = document.getElementById("real-file")
    const customButton = document.getElementById("customButton")
    const customText = document.getElementById("custom-text")
    const sendButton = document.getElementById("sendButton")

    customButton.addEventListener("click", function () {
        realFileButton.click();
    });

    realFileButton.addEventListener("change", function () {
        if (realFileButton.value) {
            customText.innerHTML = realFileButton.value;
        } else {
            customText.innerHTML = "No file chose, yet";
        }
    });
});
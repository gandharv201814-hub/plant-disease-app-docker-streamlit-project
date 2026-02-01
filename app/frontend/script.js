const video = document.getElementById("video");
const canvas = document.getElementById("canvas");
const resultText = document.getElementById("result");
const context = canvas.getContext("2d");

// Start camera
navigator.mediaDevices.getUserMedia({ video: true })
    .then(stream => {
        video.srcObject = stream;
    })
    .catch(err => {
        console.error("Camera access denied:", err);
    });

// Upload image
function uploadImage() {
    const fileInput = document.getElementById("imageUpload");
    const file = fileInput.files[0];

    if (!file) {
        alert("Please upload an image");
        return;
    }

    const formData = new FormData();
    formData.append("image", file);

    fetch("http://127.0.0.1:8000/predict", {
        method: "POST",
        body: formData
    })
    .then(res => res.json())
    .then(data => {
        resultText.innerText = `\db Disease: ${data.prediction}`;
    })
    .catch(err => {
        console.error(err);
        resultText.innerText = "Error predicting disease";
    });
}

// Capture image from camera
function captureImage() {
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    context.drawImage(video, 0, 0, canvas.width, canvas.height);
}

// Send captured image
function sendCapturedImage() {
    canvas.toBlob(blob => {
        const formData = new FormData();
        formData.append("image", blob, "camera.jpg");

        fetch("http://127.0.0.1:8000/predict", {
            method: "POST",
            body: formData
        })
        .then(res => res.json())
        .then(data => {
            resultText.innerText = `🌿 Disease: ${data.prediction}`;
        })
        .catch(err => {
            console.error(err);
            resultText.innerText = "Error predicting disease";
        });
    });
}

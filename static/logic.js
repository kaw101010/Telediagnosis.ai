// eslint-disable-next-line no-unused-vars
function press() {
    window.location.href = '/predict';
}

const startRecordingBtn = document.querySelector('.mic');
    const predictionResult = document.querySelector('.result');
    startRecordingBtn.addEventListener("click", () => {
      fetch("/predict-api")
        .then(response => response.text())
        .then(prediction => {
          predictionResult.innerHTML = `Prediction: ${(prediction['prediction']).toString()}`;
        });
    });
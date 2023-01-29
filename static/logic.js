// eslint-disable-next-line no-unused-vars
function press() {
    window.location.href = '/predict';
}

// Call predict API created with Flask and display disease on web app
const startRecordingBtn = document.querySelector('.mic');
    const predictionResult = document.querySelector('.result');
    startRecordingBtn.addEventListener("click", () => {
      setInterval(1000)
      document.querySelector('.speak').innerText = 'Continue speaking...';
      document.querySelector('a').style.borderColor = 'green';
      fetch("/predict-api")
        .then(response => response.text())
        .then(prediction => {
          document.querySelector('a').style.borderColor = 'red'
          predictionResult.innerHTML = `Prediction: ${prediction}`;
        });
    });

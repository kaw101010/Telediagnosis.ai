# Telediagnosis.ai

## Table of Contents
* [Description](#description)
* [Technologies Used](#technologiesused)
* [Setup](#setup)
* [Features](#features)
* [License](#license)

## Description
An **NLP-powered Disease Prediction System** that allows user to express his symptoms through speech, extracts symptom, and returns a predicted ailment. Used *GPT-3* for extracting symptoms from user's speech and used *Random Forest Classifier* to train the machine learning model.

## Technologies Used
* Used Python's Speech Recognition with Google to accept user's speech as input for natural language processing and utilised OpenAI API to access GPT-3 in order t0 extract symptoms from the text input
* Used Python's **scikit-learn** library to train the model. The model was trained with a **Random Forest** algorithm.
* Used **HTML**, **CSS** and **JavaScript** to develop the front-end and used Python **Flask** web framework for the backend.
* Also used **Flask** to develop the API for the machine learning model

## Setup
Clone and Fork this repository. Then navigate to the project directory. Then run ```pip install -r requirements.txt``` to install the required packages and dependencies. Then run ```python -m flask run``` to run the project with Flask.

## Features
* You can express your symptoms/problems by speech. Due to the efficient speech recognition library, your speech will be converted to text for symptom extraction.
* Symptoms are being extracted by the most capable *Davinci* model of GPT-3.
* The machine learning model is trained with *Random Forest* algorithm in the scikit-learn library.
* The UI of the project is also simple and effective.

## License
This project is licensed under the **MIT License**. More information about this license can be found [here](https://opensource.org/licenses/MIT).

## Contributors
Krish Wadhwani, Sanjay Marison, @ZilD117

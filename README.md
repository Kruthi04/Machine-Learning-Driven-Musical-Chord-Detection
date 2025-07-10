# Machine Learning-Driven Musical Chord Detection


## Project Overview
This project focuses on using machine learning to detect and analyze the chord progressions in a song. The goal is to help musicians, music producers, and researchers better understand the underlying structure of musical compositions. By training models on a wide variety of music data, we built a system that can predict chords from input audio with high accuracy.

## Features
## Chord Structure Detection: Automatically identifies chords used in a song, even with complex arrangements.

## Machine Learning Models: Implemented and compared three ML algorithms –

1. Support Vector Machine (SVM)

2. K-Nearest Neighbors (KNN)

3. Random Forest
Each model was trained to classify chords based on extracted audio features.

## High Accuracy: Achieved a 96% prediction accuracy on the test set.

## Diverse Music Dataset: Collected and preprocessed a dataset containing chord annotations from various music genres.

## Technologies Used
## Programming Languages:
1. Python

2. JavaScript

## Libraries and Frameworks:
Python: pandas, numpy, matplotlib
(Used for data preprocessing, visualization, and model development)

## Database:
MySQL (used for storing training metadata and preprocessing information)

## How It Works
1. Data Collection: A dataset of songs with labeled chords was collected from public sources.

2. Feature Extraction: Musical features (like pitch, tone, chroma) were extracted from audio using signal processing techniques.

3. Model Training:

The extracted features were used to train three ML models: SVM, KNN, and Random Forest.

Models were evaluated and tuned for optimal performance.

Prediction: Given a new song input, the trained model predicts the sequence of chords used throughout the track.

## Results
1. Final model accuracy: 96%

2. Most accurate model: Random Forest (based on test set results)

## Future Improvements
1. Add real-time chord detection from live audio input

2. Improve feature extraction using libraries like librosa

3. Develop a web-based interface for users to upload songs and view chord predictions visually


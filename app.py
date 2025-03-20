import streamlit as st
import numpy as np
import librosa
import pickle
import soundfile as sf
import tempfile

# Load the trained model
with open("audio_classification.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Feature extraction function
def feature_extractor(file):
    audio, sample_rate = librosa.load(file, res_type="kaiser_fast")
    mfccs_feature = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
    mfccs_scaled_feature = np.mean(mfccs_feature.T, axis=0)
    return mfccs_scaled_feature

# Streamlit UI
st.title("🎵 Audio Classification App")
st.write("Upload an audio file to classify it!")

# Upload audio file
uploaded_file = st.file_uploader("Upload an audio file (WAV, MP3)", type=["wav", "mp3"])

if uploaded_file is not None:
    # Save the uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = tmp_file.name

    # Display the audio player
    st.audio(uploaded_file, format="audio/wav")

    # Extract features
    features = feature_extractor(tmp_path)
    features = features.reshape(1, -1)  # Reshape for model input

    # Make prediction
    # Get the predicted class index
    class_index = np.argmax(model.predict(features))

    # UrbanSound8K class labels
    class_labels = [
        "Air Conditioner", "Car Horn", "Children Playing", "Dog Bark",
        "Drilling", "Engine Idling", "Gunshot", "Jackhammer", "Siren", "Street Music"
    ]

    # Get the predicted class name
    predicted_class = class_labels[class_index]

    # Display the result
    st.success(f"🎤 Predicted Class: **{predicted_class}**")



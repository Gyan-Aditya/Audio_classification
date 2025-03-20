# 🎵Audio Classification using Machine Learning
This repository contains an audio classification model built using TensorFlow/Keras and Librosa for feature extraction. The model is trained on the UrbanSound8K dataset and deployed using Streamlit.

## 📌 Features
-🎧 Classifies different environmental sounds (e.g., Dog Bark, Siren, Gunshot).<br>
-📊 Uses MFCC feature extraction for audio processing.<br>
-🧠 Trained using a deep learning model (CNN/MLP).<br>
-🌍 Deployed using Streamlit for a user-friendly web interface.<br>

## 📂 Folder Structure
```bash
📦 Audio-Classification-Model
│-- 📁 assets/                # Contains saved model & label mapping
│-- 📁 metadata/                  # metadata of dataset
│-- 📁 images/                  # model-structure, confusion-matrix etc.
│-- 📁 media/                  # sample of dataset
│-- 📜 audio_classification.ipynb # Jupyter notebooks for training & analysis
│-- 📜 app.py                 # Streamlit app script
│-- 📜 requirements.txt       # Dependencie
│-- 📜 README.md              # Project documentation
```

## 🛠 Installation
🔹 Step 1: Clone the Repository<br>
```bash
git clone https://github.com/Gyan-Aditya/Audio-classification.git
cd audio-classification
```
🔹 Step 2: Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv envsource env/bin/activate   # For macOS/Linuxenv\Scripts\activate      # For Windows
```
🔹 Step 3: Install Dependencies
```
pip install -r requirements.txt
```
🔹 Step 4: Run the Streamlit App
```
streamlit run app.py
```

## 🎤 How to Use
1.Upload an audio file (.wav, .mp3).
2.Model processes the audio and extracts features.
3.The model predicts the sound category and displays the result.
4.Enjoy the animation when a prediction is made! 🎉

## 📊 Model Training
-Dataset: UrbanSound8K
-Features: MFCC (Mel-Frequency Cepstral Coefficients)
-Model: CNN/MLP using TensorFlow/Keras
-Optimizer: Adam
-Loss Function: Categorical Crossentropy
-Accuracy: 75% on validation set


## 📌 Example Prediction
-Uploaded Audio: dog_bark.wav
-🎤 Predicted Class: Dog Bark ✅


## 📷 Screenshots
**Uploading Audio	Prediction**
![Screenshot 2025-03-21 003229](https://github.com/user-attachments/assets/c0198a25-0277-4050-8cc9-501a524ddad0)
**Prediction**
![Screenshot 2025-03-21 003307](https://github.com/user-attachments/assets/c4376be2-81c7-48b2-a214-8bd8945d1578)



## 🤝 Contributing
Contributions are welcome! Feel free to fork the repo and submit a pull request.

## 📬 Contact
-💡 If you have any questions, feel free to reach out:

-✉️ Email: gyanaditya2903@gmail.com

-🐦 Twitter: gyanaditya9

🔗 GitHub: Gyan-Aditya

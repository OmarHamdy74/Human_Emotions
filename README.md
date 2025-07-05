# 🎭 Emotion Detection App

A simple and elegant web application that detects human emotions from images or video files using deep learning models powered by [DeepFace](https://github.com/serengil/deepface) and [Streamlit](https://streamlit.io/).

## 🧠 Features

- Detects **7 basic emotions**: `Angry`, `Disgust`, `Fear`, `Happy`, `Sad`, `Surprise`, and `Neutral`.
- Supports both **images** and **videos** as input.
- Shows emotion prediction scores and highlights the **dominant emotion**.
- Real-time video frame processing with emotion overlay.
- Interactive and user-friendly UI.

## 📦 Dependencies

Make sure you have Python 3.7+ installed.

Install the required packages with:

```bash
pip install -r requirements.txt
````

## 📁 Project Structure

```
emotion_detection_app/
│
├── app.py                # Main Streamlit app
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
```

## 🚀 How to Run

Launch the app using Streamlit:

```bash
streamlit run app.py
```

This will open the app in your browser.

## 🖼️ Image Example

1. Select `Image` from the sidebar.
2. Upload a JPG or PNG file.
3. The app will:

   * Display the uploaded image.
   * Analyze it using DeepFace.
   * Show the dominant emotion and a bar chart of all detected emotions.

## 🎞️ Video Example

1. Select `Video` from the sidebar.
2. Upload a video (`.mp4`, `.avi`, `.mov`).
3. The app will:

   * Analyze a frame every few seconds.
   * Display the detected emotion on each analyzed frame.

## 🛠️ Built With

* [Streamlit](https://streamlit.io/)
* [DeepFace](https://github.com/serengil/deepface)
* [OpenCV](https://opencv.org/)
* [PIL / Pillow](https://python-pillow.org/)

## 📌 Notes

* The app uses `enforce_detection=False` to avoid crashes on low-quality frames.
* For better accuracy, ensure clear and front-facing images or video.

## 📃 License

This project is open-source and free to use under the MIT License.
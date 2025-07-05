
import streamlit as st
import cv2
from deepface import DeepFace
from PIL import Image
import numpy as np
import tempfile

# Page config
st.set_page_config(page_title="Emotion Detection App", layout="centered")

# Title and description
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Emotion Detection App</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Upload an image or video to detect emotions using AI</p>", unsafe_allow_html=True)

# Helper function to analyze emotions
def analyze_emotion(img_vid):
    try:
        with st.spinner("Analyzing..."):
            analysis = DeepFace.analyze(img_vid, actions=['emotion'], enforce_detection=False)
        return analysis[0]['emotion']
    except ValueError as e:
        st.error(f"Error: {e}")
        return None

# Sidebar for option selection
st.sidebar.title("Options")
option = st.sidebar.radio("Select Media Type", ('Image', 'Video'))

if option == 'Image':
    uploaded_file = st.file_uploader("📷 Upload an Image", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        image = Image.open(uploaded_file)
        img_array = np.array(image)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        emotion_scores = analyze_emotion(img_array)
        if emotion_scores:
            detected_emotion = max(emotion_scores, key=emotion_scores.get)
            st.success(f"**Detected Emotion:** {detected_emotion}")

            # Display emotions as bar chart
            st.bar_chart(emotion_scores)
        else:
            st.warning("No emotion detected or an error occurred.")

elif option == 'Video':
    video_file = st.file_uploader("🎥 Upload a Video", type=["mp4", "avi", "mov"])
    if video_file:
        with tempfile.NamedTemporaryFile(delete=False) as temp_video:
            temp_video.write(video_file.read())
            video_path = temp_video.name

        video = cv2.VideoCapture(video_path)
        stframe = st.empty()
        frame_count = 0
        frame_rate = 50  # Analyze every 30th frame

        st.info("Processing video... please wait")

        while video.isOpened():
            ret, frame = video.read()
            if not ret:
                break

            frame_count += 1
            if frame_count % frame_rate == 0:
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                emotion_scores = analyze_emotion(frame_rgb)

                if emotion_scores:
                    detected_emotion = max(emotion_scores, key=emotion_scores.get)
                else:
                    detected_emotion = "No emotion"

                cv2.putText(frame_rgb, detected_emotion, (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 2)
                stframe.image(frame_rgb, channels="RGB", caption=f"Frame {frame_count}")

        video.release()
        st.success("✅ Video processing completed.")

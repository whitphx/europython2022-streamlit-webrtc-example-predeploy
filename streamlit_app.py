import streamlit as st
from streamlit_webrtc import webrtc_streamer
import cv2
import av

st.title("Hello EuroPython 2022! 😇")

st.markdown("""
This is our **first** _Streamlit_ app!
""")

th1 = st.slider("Threshold1", 0, 1000, 100)
th2 = st.slider("Threshold2", 0, 1000, 200)

def callback(frame):
    img = frame.to_ndarray(format="bgr24")
    img = cv2.Canny(img, th1, th2)
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    return av.VideoFrame(img, format="bgr24")


webrtc_streamer(key="sample", video_frame_callback=callback)

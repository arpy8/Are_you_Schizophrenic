import cv2
import torch
import numpy as np
import streamlit as st
import PIL.Image as Image

def count_people(image):
    model1 = torch.hub.load('ultralytics/yolov5', 'yolov5l')

    image_rgb = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    results = model1(image_rgb)
    labels = results.xyxy[0][:, -1].cpu().numpy().astype(int)

    return list(labels).count(0)

uploaded_file = None

with st.sidebar:
    st.write("<center><h1>Schizophrenia Detection App</h1><br><br></center>", unsafe_allow_html=True)
    input_source = st.radio("Choose input source", ("Camera", "Image"))

if input_source == "Image":
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    user_number = st.number_input("How many people are in the image?", min_value=0, max_value=100, value=0, step=1)

    if uploaded_file and st.button("Detect"): 
        process = st.empty()
        process.write("#### Processing...")    

        if count_people(cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), 1)) == user_number:
            st.write("##### Congrats you are not Schizophrenic!") 
        else:
            st.write("##### I have some bad news for you.")

        process.empty()
                    
elif input_source == "Camera":
    video_capture = st.camera_input(label="Camera")
    user_number = st.number_input("How many people are in the frame?", min_value=0, max_value=100, value=0, step=1)

    if video_capture and st.button("Detect"):
        process = st.empty()
        process.write("#### Processing...")    
             
        if count_people(cv2.imdecode(np.frombuffer(video_capture.read(), np.uint8), 1))==user_number:
            st.balloons()
            st.success("##### Congrats you are not Schizophrenic!") 
        else:
            st.write("##### I have some bad news for you.")
        
        process.empty()
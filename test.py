import cv2
import streamlit as st

st.title("Webcam Live Feed")
start = st.button('Run')
stop = st.button('Stop')
global flag
flag=0
def run():
    global flag
    FRAME_WINDOW = st.image([])
    camera = cv2.VideoCapture(0)
    while(flag==0):
        if stop:
            flag=1
            break
        _, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        FRAME_WINDOW.image(frame)
    else:
        st.write('Stopped')
if start:
    flag=0
    run()
if st.button("click me"):
    st.write("hello")

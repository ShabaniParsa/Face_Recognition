import streamlit as st
import cv2
import face_recognition as frg
import yaml 
from utils import recognize, build_dataset
import studentDB
import time
# Path: code\app.py


#Config
DB = studentDB.DataBase()
cfg = yaml.load(open('config.yaml','r'),Loader=yaml.FullLoader)
WEBCAM_PROMPT = cfg['INFO']['WEBCAM_PROMPT']






TOLERANCE = 0.5

#Infomation section 
st.sidebar.title("Student Information")
mode_container = st.sidebar.empty()
name_container = st.sidebar.empty()
id_container = st.sidebar.empty()
name_container.info('Name: Unknown')
id_container.success('ID: Unknown')
st.title("Face Recognition App")
st.write(WEBCAM_PROMPT)
#Camera Settings
r = st.sidebar.radio("Camera Input:",["Internal Camera",'External Camera'])
if r == "Internal Camera":
    cam = cv2.VideoCapture(0)
else:
    cam = cv2.VideoCapture(1)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
img_col = st.columns(2)
with img_col[0]:
    check_btn = st.camera_input("")
with img_col[1]:
    FRAME_WINDOW = st.image([])
# check_btn = st.button('Check Face')
if check_btn:
    ret, frame = cam.read()
    if not ret:
        st.error("Failed to capture frame from camera")
        st.info("Please turn off the other app that is using the camera and restart app")
        st.stop()
    image, name, id, names, ids = recognize(frame,TOLERANCE)

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    #Display name and ID of the person
    if (name != 'Unknown') and (id != 'Unknown'):
        name_container.info(f"Name: {name}")
        id_container.success(f"ID: {id}")
        with st.spinner('Saving To Database...'):
            
            for n,i in zip(names,ids):
                mode = DB.getMode(int(i))
                data = studentDB.GSADI(n.split(' ')[0],n.split(' ')[1],int(i),mode)
                DB.add(data)
        # if mode == True:
            # mode_container.success(f'{name} enter.')
        # else:
            # mode_container.error(f'{name} exit!')
        st.write(names)
        st.write(ids)
    else:
        st.sidebar.error("Please take a better photo!")
        st.error("Please take a better photo!")
    
    FRAME_WINDOW.image(image)
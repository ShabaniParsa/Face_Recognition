import streamlit as st 
import pickle 
import yaml 
import pandas as pd 
import studentDB
cfg = yaml.load(open("config.yaml", "r"), Loader=yaml.FullLoader)
PKL_PATH = cfg['PATH']["PKL_PATH"]
DATABASE_PROMPT = cfg['INFO']['DATABASE_PROMPT']
st.set_page_config(layout="wide")

#Load databse 
with open(PKL_PATH, 'rb') as file:
    database = pickle.load(file)
DB = studentDB.DataBase()

menu = ["Students","StudentsLog"]
choice = st.sidebar.selectbox("Options",menu)
if choice == "Students":
    st.title("Student Database")
    st.write(DATABASE_PROMPT)
    Index, Id, Name, Image  = st.columns([0.5,1.5,3,3])
    nb = 0
    for idx, person in database.items():
        with Index:
            st.write(nb+1)
        with Id: 
            st.write('ID:' + person['id'])
        with Name:     
            st.write(person['name'])
        with Image:     
            st.image(person['image'],width=200)
        nb += 1
else:
    st.title("Student Log Database")
    st.write(DATABASE_PROMPT)
    Data = DB.get()
    if Data != {}:
        col = st.columns([1,1.2,1.6,0.9,0.8,0.8,0.8,0.8,0.8,0.8])
        for a in Data:
            dt = Data[a]
            with col[0]:
                st.write(dt['name'])
            with col[1]:
                st.write(dt['lname'])
            with col[2]:
                st.write(dt['id'])
            with col[3]:
                st.write(dt['year'])
            with col[4]:
                st.write(dt['month'])
            with col[5]:
                st.write(dt['day'])
            with col[6]:
                st.write(dt['hour'])
            with col[7]:
                st.write(dt['minute'])
            with col[8]:
                st.write(dt['second'])
            with col[9]:
                if dt['mode']:
                    st.write("enter")
                else:
                    st.write('exit')
    else:
        st.title("")
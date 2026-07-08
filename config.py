import streamlit as st

ORS_API_KEY = st.secrets["ORS_API_KEY"]

origin = (24.657158182733657, 121.29515647888185)
destination = (24.677944698047206, 121.39403343200685)
disaster_center = (24.672446163199574, 121.33918762207033)

height = 100

disaster_mask_path = "data/landslide_mask.png"

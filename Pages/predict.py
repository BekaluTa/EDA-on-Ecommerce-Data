import pickle

import pandas as pd
import streamlit as st
from PIL import Image

def predict_app():
    st.title("Sales Prediction on Pharmacy Data")

    eng_score = st.slider("monthpromocat", min_value=0.0,
                          max_value=2.0, step=0.1)
    exp_score = st.slider("all day comp", min_value=0.0,
                          max_value=2.0, step=0.1)

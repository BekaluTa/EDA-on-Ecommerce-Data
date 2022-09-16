import os
# from matplotlib.pyplot import plt
import sys

import pandas as pd
import plotly.express as px
import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

sys.path.append(os.path.abspath(os.path.join('./scripts')))


def overview_app():
    st.title("Overview")
    st.write(
        "Sales Overview")
    number = st.number_input("Enter the number of rows and press enter: ", min_value=None, max_value=None, value=0,
                             step=None, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False)

    df = pd.read_csv('./Data/train.csv', nrows=number)
    st.write(df)

    st.header("Day of the Week")
    top_df = pd.read_csv('./Data/train.csv')

    fig = px.bar(top_df, x='Day of the Week', y='count', height=500)
    st.plotly_chart(fig)

    st.header("Top data usage per applications")
    image = Image.open('./Data/salescustomprln.png')
    st.image(image, caption="Applications", use_column_width=True)

    st.header("Application Duration distribution using deciles")
    image = Image.open('./image/Total session Gaming.png')
    st.image(image, caption="Applications Duration Distribution",
             use_column_width=True)

    st.header("Holliday Session")
    image = Image.open('./Data/holidayseason.png')
    st.image(image, caption="customer data based on holiday",
             use_column_width=True)


    st.header("Prediction")
    image = Image.open('./Data/Prediction image.png')
    st.image(image, caption="Sales Prediction",
             use_column_width=True)


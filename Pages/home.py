import streamlit as st
import streamlit.components.v1 as components
from PIL import Image


def home_app():
    st.title("Home")
    image = Image.open('./images/frequ_for_diff_mounth.png')
    st.image(image, caption="Frequncey for different mounth", use_column_width=True)
    image = Image.open('./images/moneyspent.png')
    st.image(image, caption="Money Spent", use_column_width=True)
    image = Image.open('./images/orderdiff_day.png')
    st.image(image, caption="Order Difference by Country", use_column_width=True)
    image = Image.open('./images/Numberoforder.png')
    st.image(image, caption="Number of order", use_column_width=True)
    # components.html(
    #     """<html><body><h3>A detailed analysis of customer's data of a</h3></body></html>""", width=200, height=200)
    st.write("Ecommerce EDA from Kaggle Dataset")
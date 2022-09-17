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
        "EDA on Ecommerce")
    number = st.number_input("Enter the number of rows and press enter: ", min_value=None, max_value=None, value=0,
                             step=None, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False)

    df = pd.read_csv('./Data/data-2.csv', nrows=number)
    st.write(df)

    st.header("Sales on on country wise")
    top_df = pd.read_csv('./Data/data-2.csv')

    fig = px.bar(top_df, x='InvoiceNo', y='InvoiceNo', height=500)
    st.plotly_chart(fig)

    st.header("Order differnce by Hour")
    image = Image.open('./images/orderonhour.png')
    st.image(image, caption="Order differnce by Hour", use_column_width=True)

    st.header("Distribution of Unit Pricing")
    image = Image.open('./image/unitprice.png')
    st.image(image, caption="Unit Price Distribution",
             use_column_width=True)

    st.header("Number of customers")
    image = Image.open('./Data/Numberofcust.png')
    st.image(image, caption="Number of Customers Detail",
             use_column_width=True)


    st.header("order by Countries")
    image = Image.open('./images/order for_countries.png')
    st.image(image, caption="Order by Countries",
             use_column_width=True)


import streamlit as st
import plotly.express as px


st.title("Weather Forecasting Website created using Streamlit and APIs")
place = st.text_input("Enter your Location")
days = st.slider("Select the No. of days:", min_value = 1, max_value = 5,
                 help = "Please select the number of days you want the forecast to be showm for!!")
option = st.selectbox("Select the data to be viewed:",  ("Temperature", "Rain Chances"))

st.subheader(f"{option} data for the Selected city {place} for {days} days is:")
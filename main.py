import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecasting Website created using Streamlit and APIs")
place = st.text_input("Enter your Location")
days = st.slider("Select the No. of days:", min_value = 1, max_value = 5,
                 help = "Please select the number of days you want the forecast to be showm for!!")
option = st.selectbox("Select the data to be viewed:",  ("Temperature", "Sky"))

st.subheader(f"{option} data for the Selected city {place} for {days} days is:")
if place:
    try:
        filtered_data = get_data(place, days)

        if option == "Temperature":
            temps = [dict["main"]["temp"] / 10 for dict in filtered_data]
            date = [dict ["dt_txt"] for dict in filtered_data]
            figure = px.line(x=date, y=temps, labels={x: "Date", y: "Temperature[C]"})
            st.plotly_chart(figure)

        if option == "Sky":
            images = {"Clear": "images/clear.png", "Cloud": "images/cloud.png",
                     "Rain": "images/rain.png", "Snow": "images/snow.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            images_path = [images[condition] for condition in sky_conditions]

            st.image(images_path, width = 115)

    except KeyError:
        st.write("This city does not exists")

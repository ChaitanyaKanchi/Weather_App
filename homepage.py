import streamlit as st
import plotly.express as px
from datetime import datetime, timedelta
import requests
import pytz

API_KEY = st.secrets["api_key"]

def get_data(place, forecast_days=None):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data

def get_nearest_value(current_time, weather_data, key):
    # Assume the times in the API data are in UTC and make them timezone-aware
    utc = pytz.UTC
    nearest_entry = min(
        weather_data,
        key=lambda x: abs(utc.localize(datetime.strptime(x["dt_txt"], '%Y-%m-%d %H:%M:%S')) - current_time)
    )
    return nearest_entry["main"][key], nearest_entry["dt_txt"]

def get_suggestions(temp=None, pressure=None):
    if temp is not None:
        if temp < 0:
            return "It's freezing! Wear warm clothes and stay indoors if possible."
        elif 0 <= temp < 10:
            return "It's quite cold outside. Consider wearing a coat and scarf."
        elif 10 <= temp < 20:
            return "The weather is cool. A light jacket should be fine."
        elif 20 <= temp < 30:
            return "Nice weather! You can wear comfortable, casual clothing."
        else:
            return "It's hot outside! Stay hydrated and wear light, breathable clothes."
        
    elif pressure is not None:
        if pressure < 1000:
            return "Low pressure! Prepare for possible rain or storms."
        elif 1000 <= pressure <= 1020:
            return "Normal pressure. Expect stable and calm weather."
        else:
            return "High pressure! Clear skies and calm weather ahead."
    return ""

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
option = st.sidebar.selectbox("Select data to view", ("Temperature", "Sky", "Pressure"))
days = st.sidebar.slider("Forecast Days", min_value=1, max_value=7, help="Select the number of forecast days")
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    try:
        filtered_data = get_data(place, days)
        current_time = datetime.now(pytz.UTC)  # Use your local timezone if needed

        if option == "Temperature":
            temperatures = [entry["main"]["temp"] for entry in filtered_data]
            dates = [entry["dt_txt"] for entry in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={"x": "Dates", "y": "Temperature (C)"})
            st.plotly_chart(figure)

            nearest_temp, nearest_time = get_nearest_value(current_time, filtered_data, "temp")
            st.header("Present Temperature")
            st.write(f"The nearest temperature at {nearest_time} is {nearest_temp}°C.")

            if st.button("Suggestion"):
                st.write(get_suggestions(temp=nearest_temp))

        elif option == "Pressure":
            pressure = [entry["main"]["pressure"] for entry in filtered_data]
            dates = [entry["dt_txt"] for entry in filtered_data]
            figure_1 = px.line(x=dates, y=pressure, labels={"x": "Dates", "y": "Pressure (hPa)"})
            st.plotly_chart(figure_1)

            nearest_pressure, nearest_time = get_nearest_value(current_time, filtered_data, "pressure")
            st.write(f"The nearest pressure at {nearest_time} is {nearest_pressure} hPa.")

            if st.button("Suggestion"):
                st.write(get_suggestions(pressure=nearest_pressure))

        elif option == "Sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}
            sky_conditions = [entry["weather"][0]["main"] for entry in filtered_data]
            dates = [entry["dt_txt"] for entry in filtered_data]
            image_paths = [images.get(condition, "images/default.png") for condition in sky_conditions]
            st.image(image_paths, width=115, caption=dates)

    except requests.exceptions.RequestException as e:
        st.write("Error fetching data. Please check your internet connection or try again later.")
    except KeyError:
        st.write("That place does not exist.")

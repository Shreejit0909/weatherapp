import streamlit as st
import requests

# Title
st.title("Weather Information App 🌤️")

# Description
st.write("Enter a city name below to get its current weather information.")

# Text Input with a Submit Button
with st.form("city_form"):
    city = st.text_input("Type the city name:", placeholder="Enter city name")
    submit = st.form_submit_button("Get Weather")

# Function to Fetch Weather
def get_weather(city_name):
    api_key = "911f88f4b480c76fdb0d9c8db4126f50"  # Replace with your OpenWeather API key
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city_name, "appid": api_key, "units": "metric"}
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Function to Fetch City Suggestions (Optional Improvement)
def get_city_suggestions(query):
    # Mock suggestions: Replace with actual API for autocomplete (e.g., Google Places API)
    cities = ["Pune", "Mumbai", "Delhi", "New York", "London", "Paris", "Berlin", "Tokyo"]
    return [city for city in cities if query.lower() in city.lower()]

# Display City Suggestions Dynamically
if city:
    suggestions = get_city_suggestions(city)
    if suggestions:
        st.write("Did you mean:")
        for suggestion in suggestions:
            st.write(f"- {suggestion}")

# Display Weather Details After Submitting
if submit and city:
    data = get_weather(city)
    if data and data.get('main'):  # Check for valid weather data
        st.subheader(f"Weather in {city}")
        st.write(f"**Temperature:** {data['main']['temp']}°C")
        st.write(f"**Weather:** {data['weather'][0]['description'].capitalize()}")
        st.write(f"**Humidity:** {data['main']['humidity']}%")
        st.write(f"**Wind Speed:** {data['wind']['speed']} m/s")
        st.write(f"**Pressure:** {data['main']['pressure']} hPa")
    else:
        st.error("City not found! Please enter a valid city name or check your API key.")

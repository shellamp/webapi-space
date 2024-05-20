import streamlit as st
import requests
import pandas as pd

st.title("People in Space and ISS Location")

# Astronauts
astronauts_response = requests.get("http://api.open-notify.org/astros.json")
astronauts_data = astronauts_response.json()
st.subheader(f"Total people in space: {astronauts_data['number']}")
st.write("Astronaut Names:")
for person in astronauts_data["people"]:
    st.write(person["name"])

# ISS Location
iss_response = requests.get("http://api.open-notify.org/iss-now.json")
iss_data = iss_response.json()
iss_location = pd.DataFrame({
    "lat": [float(iss_data["iss_position"]["latitude"])],
    "lon": [float(iss_data["iss_position"]["longitude"])]
})
st.subheader("ISS Location:")
st.map(iss_location)

import streamlit as st
import requests

# Flask API URL (make sure the Flask app is running on the same machine or adjust the URL)
FLASK_API_URL = "http://127.0.0.1:5000/events"

# Fetch events from the Flask API
def get_events_from_api():
    response = requests.get(FLASK_API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        return []

# Display events in Streamlit
def display_events(events):
    if not events:
        st.write("No events found!")
    else:
        for event in events:
            st.write(f"Event: {event['event']}, Date: {event['date']}")

# Streamlit app interface
st.title("Global Political Events Tracker")
events = get_events_from_api()
display_events(events)

import streamlit as st
import requests

FLASK_API_URL = "http://127.0.0.1:5000/events"

def get_events_from_api():
    response = requests.get(FLASK_API_URL)
    if response.status_code == 200:
        return response.json()
    return []

def display_events(events):
    for event in events:
        st.write(f"Event: {event['event']}, Date: {event['date']}")

st.title("Global Political Events Tracker")
events = get_events_from_api()
display_events(events)

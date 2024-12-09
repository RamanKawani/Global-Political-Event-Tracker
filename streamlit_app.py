import streamlit as st
import requests

# Flask API URL
FLASK_API_URL = "http://127.0.0.1:5000/api/events"  # Adjust this if Flask runs on a different URL

# Function to fetch events from Flask API
def get_events():
    try:
        response = requests.get(FLASK_API_URL)
        if response.status_code == 200:
            return response.json()
        else:
            st.error("Failed to fetch events")
            return []
    except requests.exceptions.RequestException as e:
        st.error(f"Error while fetching events: {e}")
        return []

# Streamlit app interface
st.title("Global Political Event Tracker")

# Fetch events and display them
events = get_events()

if events:
    for event in events:
        st.write(f"**{event['title']}**")
        st.write(f"Published at: {event['publishedAt']}")
        st.write(f"Description: {event['description']}")
        st.write(f"[Read More]({event['url']})")
else:
    st.write("No events found.")

from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# Sample API URL for fetching political events (replace with a real API)
EVENTS_API_URL = 'https://api.example.com/global-political-events'

def fetch_political_events():
    """
    Function to fetch political events from an API
    """
    try:
        response = requests.get(EVENTS_API_URL)
        if response.status_code == 200:
            return response.json()  # Return the event data in JSON format
        else:
            return []
    except Exception as e:
        print(f"Error fetching events: {e}")
        return []

@app.route('/')
def index():
    """
    Home route to render political events on the main page
    """
    events = fetch_political_events()
    return render_template('index.html', events=events)

@app.route('/api/events', methods=['GET'])
def get_events():
    """
    API route to return political events data in JSON format
    """
    events = fetch_political_events()
    return jsonify(events)

if __name__ == '__main__':
    app.run(debug=True)

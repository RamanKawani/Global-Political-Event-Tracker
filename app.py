from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# Replace this with your actual API key from NewsAPI (you can sign up for a free account)
NEWS_API_KEY = 'your_newsapi_key'
NEWS_API_URL = 'https://newsapi.org/v2/everything'

def fetch_political_events():
    """
    Function to fetch global political events from NewsAPI
    """
    params = {
        'q': 'politics',  # Search query for political events
        'apiKey': NEWS_API_KEY,  # Your API key for NewsAPI
        'language': 'en',  # Filter results to English
        'pageSize': 50,  # Adjust the number of results per page
        'sortBy': 'publishedAt'  # Sort by the most recent events
    }
    
    try:
        response = requests.get(NEWS_API_URL, params=params)
        if response.status_code == 200:
            return response.json()['articles']  # Return the articles section of the response
        else:
            return []
    except Exception as e:
        print(f"Error fetching events: {e}")
        return []

@app.route('/')
def index():
    """
    Home route to display political events
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

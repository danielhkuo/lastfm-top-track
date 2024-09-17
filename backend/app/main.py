from flask import Flask, jsonify
import os
import requests
from datetime import datetime, timedelta
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

LASTFM_API_KEY = os.environ.get('LASTFM_API_KEY')
LASTFM_USERNAME = os.environ.get('LASTFM_USERNAME')

def get_top_track():
    one_month_ago = datetime.now() - timedelta(days=30)
    from_timestamp = int(one_month_ago.timestamp())

    url = f"http://ws.audioscrobbler.com/2.0/?method=user.gettoptracks&user={LASTFM_USERNAME}&api_key={LASTFM_API_KEY}&format=json&period=1month&limit=1&from={from_timestamp}"
    response = requests.get(url)
    data = response.json()

    if 'toptracks' in data and 'track' in data['toptracks'] and len(data['toptracks']['track']) > 0:
        track = data['toptracks']['track'][0]
        return {
            'name': track['name'],
            'artist': track['artist']['name'],
            'playcount': track['playcount']
        }
    return None

@app.route('/api/top-track')
def top_track():
    track = get_top_track()
    return jsonify(track)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
from flask import Flask, request, jsonify, render_template
from voicegain_speech.api.transcribe_api import TranscribeApi
from voicegain_speech.api_client import ApiClient
from voicegain_speech.configuration import Configuration
import re

app = Flask(__name__)

# Initialize the Voicegain client
configuration = Configuration()
configuration.api_key['Authorization'] = 'Bearer knI8RKO+ufSnww3Zn9DYC6/xqQInUYD+6uOtJpaDLRA='  # Replace with your API key
api_client = ApiClient(configuration)

transcribe_api = TranscribeApi(api_client)

keywords = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recognize', methods=['POST'])
def recognize():
    global keywords
    data = request.json
    transcript = data.get('transcript', '').lower()
    keyword_count = {keyword: len(re.findall(r'\b' + keyword + r'\b', transcript)) for keyword in keywords}
    return jsonify({'transcript': transcript, 'keyword_count': keyword_count})

@app.route('/keywords', methods=['POST'])
def set_keywords():
    global keywords
    data = request.json
    keywords = [keyword.strip().lower() for keyword in data.get('keywords', '').split(',')]
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

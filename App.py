from flask import Flask, request, jsonify
from voicegain_speech import VoicegainSpeech

app = Flask(__name__)

# Initialize the Voicegain client
voicegain = VoicegainSpeech(api_key='knI8RKO+ufSnww3Zn9DYC6/xqQInUYD+6uOtJpaDLRA=')

@app.route('/')
def home():
    return "Welcome to the Speech Recognition App!"

@app.route('/recognize', methods=['POST'])
def recognize():
    audio_file = request.files['file']
    result = voicegain.recognize(audio_file)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)

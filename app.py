from flask import Flask, jsonify, request, send_file, send_from_directory
from texttospeech import textToSpeech
import os
import random
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.static_folder = os.path.join(os.getcwd(), "oops")
app.static_url_path = "/static"
@app.route('/api', methods=['POST'])
def get_data():
  data = request.get_json()
  if data is None or 'text' not in data:
    return jsonify({'error': 'Invalid input'})
  
  filename = str(random.randint(1,10000))+'speech.wav'
  path = os.path.join(os.getcwd(),'oops', filename)
  text = data['text']
  textToSpeech(text, path)
  return jsonify({'file':filename})
    
 
@app.route('/static/<path:filename>', methods=['GET'])
def post_data(filename):
    print('test')
    return send_from_directory('oops', filename)

if __name__ == '__main__':
    app.run()


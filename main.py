from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_data():
  print("oops")
  data = {'message': 'Hello, Flask API!'}
  return jsonify(data)
 
@app.route('/api', methods=['POST'])
def post_data():
    data = request.get_json()
    if data is None:
        return jsonify({'error': 'Invalid JSON'}), 400

    # Process the data and return a response
    response = {'message': 'Data received', 'data': data}
    return jsonify(response)

if __name__ == '__main__':
    app.run()


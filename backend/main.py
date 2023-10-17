from flask import Flask
from flask_cors import CORS

### --- App Config --- ###
app = Flask(__name__)
app.config.from_object(__name__)

# Give green lights to the frontend
CORS(app, resources={r'/*': {'origins': 'http://localhost:8080', 'allow_headers': 'Access-Control-Allow-Origin'}})

### --- Routes --- ###
@app.route('/', methods=['GET'])
def index():
    return 'Hello World!'

@app.route('/sampledata', methods=['GET'])
def sample_data():
    return 'This message is from the backend!'

# --- Run App ---
if __name__ == '__main__':
    app.run(debug=True)

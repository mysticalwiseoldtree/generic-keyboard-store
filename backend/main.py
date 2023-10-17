from flask import Flask
from flask_cors import CORS

# --- App Config ---
app = Flask(__name__)

app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})
CORS(app, resources={r'/*': {'origins': 'http://localhost:8080', 'allow_headers': 'Access-Control-Allow-Origin'}})

# --- Routes ---
@app.route('/', methods=['GET'])
def index():
    return 'Hello World!'

# --- Run App ---
if __name__ == '__main__':
    app.run(debug=True)

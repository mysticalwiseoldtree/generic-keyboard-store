from flask import Flask, json
from flask_cors import CORS
from modules import keyboards

### --- App Config --- ###
app = Flask(__name__)
app.config.from_object(__name__)

# Give green lights to the frontend
CORS(
    app,
    resources={
        r"/*": {
            "origins": "http://localhost:8080",
            "allow_headers": "Access-Control-Allow-Origin",
        }
    },
)
CORS(
    app,
    resources={
        r"/*": {
            "origins": "http://127.0.0.1:8080",
            "allow_headers": "Access-Control-Allow-Origin",
        }
    },
)


### --- Routes --- ###
@app.route("/", methods=["GET"])
def index():
    return '<h1 style="margin: 15%; text-align: center;">Hello fellow traveller I think you went the wrong way</h1>'


@app.route("/samplekeyboard", methods=["GET"])
def sample_keyboard():
    return json.dumps(keyboards.sample_keyboard.__dict__)


# --- Run App ---
if __name__ == "__main__":
    app.run(debug=False)

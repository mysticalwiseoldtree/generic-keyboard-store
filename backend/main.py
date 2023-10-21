from flask import Flask, json
from flask_cors import CORS
from modules import product

### --- App Config --- ###
app = Flask(__name__)
app.config.from_object(__name__)

# Give green lights to the frontend
CORS(
    app,
    resources={
        r"/*": {
            "origins": ["http://localhost:5173", "http://127.0.0.1:5173"],
            "allow_headers": "Access-Control-Allow-Origin",
        }
    },
)


### --- Routes --- ###
@app.route("/", methods=["GET"])
def index():
    return """
    <h1 style="margin: 10%; text-align: center; font-family: Arial;">
        Hello fellow traveller I think you went the wrong way
    </h1>
    """


@app.route("/sampleproduct", methods=["GET"])
def sample_product():
    return json.dumps(product.sample_product.__dict__)


# --- Run App ---
if __name__ == "__main__":
    app.run(debug=False)

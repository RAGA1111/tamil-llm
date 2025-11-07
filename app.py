from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():
    user_msg = request.json.get('message', '')
    
    
    payload = {
        "model": "tamil-llama",  
        "messages": [
            {"role": "system", "content": "நீங்கள் ஒரு தமிழில் உதவிசெய்யும் குரல் மாதிரி."},
            {"role": "user", "content": user_msg}
        ]
    }

    try:
        r = requests.post("http://localhost:1234/v1/chat/completions", json=payload, timeout=60)
        data = r.json()
        reply = data["choices"][0]["message"]["content"]
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"reply": f"பிழை ஏற்பட்டது: {e}"})

if __name__ == '__main__':
    app.run(debug=True)

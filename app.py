from flask import Flask, request, jsonify
import whisper
import tempfile
import os

app = Flask(__name__)
model = whisper.load_model("base")

@app.route("/speech", methods=["POST"])
def speech():
    audio = request.files['audio']
    temp = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    audio.save(temp.name)

    result = model.transcribe(temp.name)
    text = result["text"]

    os.remove(temp.name)
    return jsonify({"text": text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

@app.route("/")
def home():
    return "ESP32 Speech Server Running"


from fastapi import FastAPI, File, UploadFile
import whisper
import torch

app = FastAPI()

# FORCE CPU
device = "cpu"
model = whisper.load_model("tiny", device=device)

@app.post("/stt")
async def stt(file: UploadFile = File(...)):
    audio_path = "audio.wav"

    with open(audio_path, "wb") as f:
        f.write(await file.read())

    result = model.transcribe(audio_path)
    return {"text": result["text"].strip()}

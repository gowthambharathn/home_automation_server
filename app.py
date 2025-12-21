from fastapi import FastAPI, File, UploadFile
import whisper

app = FastAPI()

model = whisper.load_model("base")

@app.post("/stt")
async def stt(file: UploadFile = File(...)):
    with open("audio.wav", "wb") as f:
        f.write(await file.read())

    result = model.transcribe("audio.wav")
    return {"text": result["text"]}

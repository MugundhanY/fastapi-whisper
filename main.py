from fastapi import FastAPI, UploadFile, File
import whisper
import os

app = FastAPI()

# Load the Whisper model (small model to save memory)
model = whisper.load_model("small")

@app.post("/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    # Save the uploaded file temporarily
    file_location = f"temp_{file.filename}"
    with open(file_location, "wb") as f:
        f.write(await file.read())
    
    # Use Whisper to transcribe the audio
    result = model.transcribe(file_location)
    
    # Remove the temporary file
    os.remove(file_location)
    
    # Return the transcription as JSON
    return {"text": result["text"]}

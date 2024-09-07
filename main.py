from fastapi import FastAPI, UploadFile, File, HTTPException
import whisper
import os
import tempfile

app = FastAPI()

# Load the Whisper model (small model to save memory)
model = whisper.load_model("tiny")

@app.post("/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    # Use tempfile to create a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_file:
        temp_file.write(await file.read())
        temp_file_path = temp_file.name

    try:
        # Use Whisper to transcribe the audio
        result = model.transcribe(temp_file_path)

        # Return the transcription as JSON
        return {"text": result["text"]}
    except Exception as e:
        # Log the exception and return an error response
        print(f"Error during transcription: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    finally:
        # Remove the temporary file
        os.remove(temp_file_path)

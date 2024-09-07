from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
import subprocess
import os
import tempfile

app = FastAPI()

class TextResponse(BaseModel):
    text: str

@app.post("/transcribe", response_model=TextResponse)
async def transcribe_audio(file: UploadFile = File(...)) -> TextResponse:
    # Save the uploaded file to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio_file:
        temp_audio_file.write(await file.read())
        temp_audio_file.close()

        # Define the output path
        output_file_path = temp_audio_file.name + ".txt"

        # Run the Whisper CLI command
        result = subprocess.run([
            'whisper', temp_audio_file.name, '--model', 'small', '--output', output_file_path
        ], capture_output=True, text=True)

        # Read the output file
        with open(output_file_path, 'r') as output_file:
            text = output_file.read()

        # Clean up temporary files
        os.remove(temp_audio_file.name)
        os.remove(output_file_path)

    return TextResponse(text=text)

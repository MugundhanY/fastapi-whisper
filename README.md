# Whisper STT Project with FastAPI

This project implements a Speech-to-Text (STT) service using OpenAI's Whisper CLI and FastAPI. It allows users to upload `.wav` audio files, which are transcribed into text using the Whisper Small model.

## Features
- Upload `.wav` audio files via a POST request.
- The Whisper CLI (small model) is used to process the audio and transcribe it to text.
- Returns the transcription as a JSON response.

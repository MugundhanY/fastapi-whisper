# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install ffmpeg and other dependencies
RUN apt-get update && apt-get install -y ffmpeg

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Install Whisper
RUN pip install git+https://github.com/openai/whisper.git

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run the FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# Use the official Python image
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Copy your app files into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port FastAPI runs on
EXPOSE 8000

# Run FastAPI
# CMD ["fastapi", "main:app", "--host", "0.0.0.0", "--port", "8000"]
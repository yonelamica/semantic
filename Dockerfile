# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Install the required system packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgomp1

# Copy the entire current directory into the container at /app
COPY . .

# Install the Python dependencies
RUN pip install --no-cache-dir spacy && \
    python -m spacy download en_core_web_md

# Run the Python script
CMD ["python", "semantic.py"]

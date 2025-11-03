# Use official Python base image
FROM python:3.9-slim-buster

# Set working directory
WORKDIR /

# Copy all files to container
COPY . .

# Install Flask directly
RUN pip install --no-cache-dir flask

# Expose port
EXPOSE 5000

# Run the Flask app
CMD ["python", "simplewebpage.py"]


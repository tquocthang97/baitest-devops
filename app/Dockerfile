# Use the official Python image
FROM python:3.12

# Set the working directory
WORKDIR /app

# Copy requirements and application files
COPY requirements.txt requirements.txt

COPY app.py app.py

# Install Python dependencies
RUN pip install -r requirements.txt

# Run the application
CMD ["python", "app.py"]

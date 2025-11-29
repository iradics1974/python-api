# Use the official lightweight Python image as base
FROM python:3.12-slim

# Set the working directory inside the container
# All following commands run relative to this folder
WORKDIR /app

# Copy dependency lists first (layer caching optimization)
COPY requirements.txt .

# Install dependencies inside the container
# --no-cache-dir keeps the image small
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files
COPY . .

# Expose the port your Python app listens on
# (Does nothing by itself; only for documentation)
EXPOSE 5000

# Define the command to start the application inside the container
# This is what runs when 'docker run' or Kubernetes executes the image
CMD ["python", "app.py"]

# Use Python 3.9 slim image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy all files from the current directory to the container's working directory
COPY . .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 80 to make the app accessible
EXPOSE 80

# Command to run the Flask app
CMD ["python", "app1.py"]

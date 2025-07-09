# Use Python 3.9 slim image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy contents
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose correct port (5001 matches your app)
EXPOSE 5001

# Start the Flask app
CMD ["python", "app1.py"]

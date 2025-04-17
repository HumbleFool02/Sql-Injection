FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy everything
COPY . .

# Install pip dependencies
RUN pip install --no-cache-dir -r requirement.txt

# Expose Flask port
EXPOSE 5000

# Run DB init + Flask app
CMD ["sh", "-c", "python init_db.py && python app.py"]
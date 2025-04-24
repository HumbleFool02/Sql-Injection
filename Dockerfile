FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirement.txt

EXPOSE 5000

CMD ["sh", "-c", "python init_db.py && python app.py"]

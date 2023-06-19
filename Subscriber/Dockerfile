FROM python:3

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY Subscriber.py .

CMD ["python", "-u", "Subscriber.py"]

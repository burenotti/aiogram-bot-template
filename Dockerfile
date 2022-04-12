FROM python:3.10

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

ENV PYTHONPATH=/app/bot

CMD ["python", "-m", "bot"]
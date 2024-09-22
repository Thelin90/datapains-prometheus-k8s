FROM python:3.11-alpine
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY main.py /app/main.py

RUN python -m pip install prometheus-client

EXPOSE 8000

ENTRYPOINT ["python3", "main.py"]

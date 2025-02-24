FROM python:3.9-slim-bullseye

WORKDIR /app

COPY pyproject.toml .

RUN pip install --no-cache-dir .

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]

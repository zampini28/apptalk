FROM python:3.9-slim-bullseye

WORKDIR /app

COPY pyproject.toml .

RUN pip install --no-cache-dir .

COPY . .

EXPOSE 5000

CMD ["python", "-m", "flask", "--app", ".", "init-db"]
CMD ["python", "-m", "flask", "--app", ".", "run", "--host=0.0.0.0", "--port=5000", "--debug"]

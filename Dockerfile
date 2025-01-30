FROM python:3.9-slim

WORKDIR /app

# Copy the entire application directory to the container
COPY . .

RUN pip install Flask

EXPOSE 5000

CMD ["python", "app.py"]


FROM python:3.7-alpine

# Creates work dir   
WORKDIR /app

# Copy python script to the container folder app
COPY copyright_insert.py /app/copyright_insert.py

ENTRYPOINT  ["python", "/app/copyright_insert.py"]
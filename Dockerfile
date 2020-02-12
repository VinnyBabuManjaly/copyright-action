FROM python:3.7-alpine

LABEL "com.github.actions.name"="Insert Copyright Action"
LABEL "com.github.actions.description"="Automatically inserts copyright to the required files in a repository"
# LABEL "com.github.actions.icon"="arrow-up-right"
# LABEL "com.github.actions.color"="gray-dark"

LABEL version="1.0.0"
LABEL repository="https://github.com/VinnyBabuManjaly/insert-copyright-action"
LABEL homepage="https://github.com/VinnyBabuManjaly/insert-copyright-action"
LABEL maintainer="Vinny Babu Manjaly <vinnybabumanjaly@gmail.com>"

# Creates work dir   
WORKDIR /app

# Copy python script to the container folder app
COPY copyright_insert.py /app/copyright_insert.py

ENTRYPOINT ["python", "/app/copyright_insert.py"]
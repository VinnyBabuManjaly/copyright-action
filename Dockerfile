FROM python:3.7-alpine
#add user group and ass user to that group
#RUN addgroup -S appgroup && adduser -S appuser -G appgroup

#creates work dir   
WORKDIR /app

#copy python script to the container folder app
COPY copyright_insert.py /app/copyright_insert.py

#user is appuser
#USER appuser

ENTRYPOINT  ["python", "/app/copyright_insert.py"]

#FROM python:slim-buster
#COPY "copyright_insert.py" "/copyright_insert.py"
#RUN echo 'we are running some # of cool things'
# CMD ["/copyright_insert.py"]
#COPY "copyright_insert.py" "/copyright_insert.py"
#RUN chmod +x /copyright_insert.py
#ENTRYPOINT ["/copyright_insert.py"]
#RUN echo 'we are running some # of cool things'
FROM python:slim-buster

COPY "copyright_insert.py" "/copyright_insert.py"
RUN echo 'we are running some # of cool things'
RUN chmod +x /copyright_insert.py
CMD ["/copyright_insert.py"]
RUN echo 'we are running some # of cool things'
FROM python:slim-buster

COPY "copyright_insert.py" "/copyright_insert.py"
RUN echo 'we are running some # of cool things'
# CMD ["/copyright_insert.py"]
COPY "copyright_insert.py" "/copyright_insert.py"
RUN chmod +x /copyright_insert.py
ENTRYPOINT ["/copyright_insert.py"]
RUN echo 'we are running some # of cool things'
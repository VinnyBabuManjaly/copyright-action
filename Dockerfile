FROM python:slim-buster

COPY "copyright_insert.py" "/copyright_insert.py"
RUN LS
CMD ["/copyright_insert.py"]
#define base image
FROM python:3.10.10-slim

#working dir
WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

#expose port 8000 to the outside world
EXPOSE 8000

#define environmental variable
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

#when container launches
CMD [ "python","manage.py","runserver","0.0.0.0:8000" ]

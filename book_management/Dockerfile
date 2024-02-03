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

# Copy entrypoint script
COPY entrypoint.sh /usr/src/app/entrypoint.sh

# Make entrypoint script executable
RUN chmod +x /usr/src/app/entrypoint.sh

# Set the entrypoint
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]


#when container launches
CMD [ "python","manage.py","runserver","0.0.0.0:8000" ]

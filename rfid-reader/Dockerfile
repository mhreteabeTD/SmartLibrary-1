FROM python:3.10.10-slim

WORKDIR /usr/src/rfid

COPY requirements.txt ./

RUN pip install --upgrade pip

RUN pip install  --no-cache-dir -r requirements.txt

COPY .  .

CMD [ "python","./rfid_simulator.py" ]
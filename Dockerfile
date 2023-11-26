FROM python:3.8

RUN apt-get -y install python3

RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.33.0/geckodriver-v0.33.0-linux64.tar.gz
RUN tar -xvzf geckodriver-v0.30.0-linux64.tar.gz
RUN cp geckodriver /usr/local/bin/


COPY . /app
WORKDIR /app


RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python3", "tests/CAFAP/AIS_CAFAP/ais_cafap.py"]
from python:3

MAINTAINER Adam Vollrath "axisofentropy@gmail.com"

WORKDIR /app

ADD requirements.txt /app

RUN pip3 install -r requirements.txt

ADD main.py /app

EXPOSE 5000

CMD ["gunicorn", "-w 4", "-b 0.0.0.0:5000", "main:app"]

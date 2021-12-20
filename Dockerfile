FROM python:3-alpine

LABEL maintainer="Adam Vollrath adam.d.vollrath@gmail.com"
LABEL org.opencontainers.image.authors="adam.d.vollrath@gmail.com"

WORKDIR /app

COPY requirements.txt /app

RUN pip3 install -r requirements.txt

COPY main.py /app

EXPOSE 5000

CMD ["gunicorn", "-w 4", "-b 0.0.0.0:5000", "main:app"]

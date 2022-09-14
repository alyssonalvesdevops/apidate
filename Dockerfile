FROM python:slim-buster
WORKDIR /app
RUN useradd -rm -d /home/app -s /bin/bash app

COPY requirements.txt /app
RUN pip install "elastic-apm[flask]"
RUN pip install -r requirements.txt

ARG SECRET_TOKEN
ARG SECRET_URL

COPY main.py /app
EXPOSE 80
USER app
CMD ["gunicorn", "-w 4", "-b", "0.0.0.0:80", "main:app"]
FROM python:3.7

ADD requirements.txt /
RUN pip install -r /requirements.txt

ADD src/ /app/

ENV PYTHONPATH="/app"
WORKDIR /app
#EXPOSE 9999
ENTRYPOINT python3.7 main/main.py
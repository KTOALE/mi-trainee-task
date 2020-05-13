FROM python:3.7

ADD requirements.txt /
RUN pip install -r /requirements.txt

ADD src/ /app/
#ADD src/main /app/main/
#ADD src/handlers /app/handlers/
#ADD src/utils /app/utils/
ENV PYTHONPATH="/app"
WORKDIR /app
ENTRYPOINT python3.7 main/app.py

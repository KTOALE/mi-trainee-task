FROM python:3.7

ADD requirements.txt /
RUN pip install -r /requirements.txt

ADD src/ /app/
#ADD src/main /main/main/
#ADD src/handlers /main/handlers/
#ADD src/utils /main/utils/
ENV PYTHONPATH="/app"
WORKDIR /app
EXPOSE 9999
ENTRYPOINT python3.7 -u main/app.py

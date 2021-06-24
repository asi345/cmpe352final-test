FROM python:3.9.5

LABEL MAINTAINER="CMPE352 Group 7 Spring 2021"

WORKDIR .

USER root

ADD . .
RUN pip3 install -r requirements.txt
ENV FLASK_APP=app
ENV FLASK_ENV=development

EXPOSE 5000

CMD ["python3", "-m", "flask", "run", "-h", "0.0.0.0"]

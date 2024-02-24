FROM python:3.9.18-slim
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8080

RUN mkdir code
WORKDIR code
RUN mkdir static
RUN mkdir templates
ADD . /code/
ADD /static/. /code/static/
ADD /templates/. /code/templates/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install -r requirements.txt

EXPOSE 8080
CMD [ "flask", "run" ]
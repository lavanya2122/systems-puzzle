FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir -p /opt/services/flaskapp/src
COPY requirements.txt /opt/services/flaskapp/src/
WORKDIR /opt/services/flaskapp/src
RUN pip install -r requirements.txt
COPY . /opt/services/flaskapp/src
# flask app server uses default port as 5000, 
# if we want to use port 5001, comment out 5000 and uncoment 5001
EXPOSE 5000
#EXPOSE 5001

CMD ["python", "app.py"]

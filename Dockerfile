# Importing the python
FROM python:3.8

RUN mkdir /app

COPY . /app

WORKDIR /app

#remove the venv
RUN rm -rf pred_api

#installing the libraries
RUN pip install -r requirements.txt

#run the app
CMD python app.py
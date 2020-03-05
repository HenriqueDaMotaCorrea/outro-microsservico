FROM python:3.7

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

SHELL ["/bin/bash", "-c"]

WORKDIR app/src

RUN apt-get -y update && apt-get -y install tesseract-ocr

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY /tesseract .

EXPOSE 8000

CMD ["python3", "tesseract/manage.py", "runserver"]

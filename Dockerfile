
FROM python:3.7

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

RUN mkdir /code
COPY . /code
WORKDIR /code/boardgamebro

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

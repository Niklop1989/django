FROM python:3.12.3

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt

COPY mysite .

CMD ["gunicorn", "mysite.wsgi:application", "--bine",'0.0.0.0:8000']
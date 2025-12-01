FROM python:3.12.3

ENV PYTHONUNBUFFERED=1

WORKDIR /app

# COPY requirements.txt requirements.txt

RUN pip install --upgrade pip "poetry==2.2.1"

RUN poetry config virtualenvs.create false --local
COPY pyproject.toml poetry.lock ./
RUN  poetry install --no-root

# RUN pip install -r /app/requirements.txt

COPY mysite .

CMD ["gunicorn", "mysite.wsgi:application", "--bine",'0.0.0.0:8000']
FROM python:3.9.1

COPY . /app
RUN make /app

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "alembic", "upgrade", "head"]
CMD [ "uvicorn", "main:app", "--reload", "--host",  "0.0.0.0"]

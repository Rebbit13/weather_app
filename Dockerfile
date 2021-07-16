FROM python:3.9.1

COPY . /app
RUN make /app

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt
RUN alembic revision --autogenerate -m "initial_commit"
RUN alembic upgrade head

CMD [ "uvicorn", "main:app", "--reload"]

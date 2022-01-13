FROM python:3.10-alpine

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

EXPOSE 5001

CMD ["uvicorn", "main:api", "--host", "0.0.0.0", "--port", "5001"]

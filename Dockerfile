FROM python:3.11-alpine as dev
WORKDIR /code
COPY requirements.txt ./
RUN apk add --no-cache gcc musl-dev python3-dev libffi-dev openssl-dev cargo
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY ./app ./app
CMD ["uvicorn", "app.core.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]

FROM python:3

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y default-mysql-client \
    dos2unix

COPY entrypoint.sh /app/entrypoint.sh

RUN chmod +x entrypoint.sh
RUN dos2unix /app/entrypoint.sh

ENTRYPOINT ["/bin/sh", "/app/entrypoint.sh"]

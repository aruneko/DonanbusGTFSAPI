FROM python:alpine3.6

WORKDIR /usr/src/app

ENV DOCKERIZE_VERSION v0.6.0

COPY requirements.txt ./
RUN pip install -U --no-cache-dir -r requirements.txt \
 && apk add --no-cache openssl \
 && wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
 && tar -C /usr/local/bin -xzvf dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
 && rm dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz

COPY . .
VOLUME /usr/src/app/gtfs
CMD [ "python", "gtfs_api/app.py" ]
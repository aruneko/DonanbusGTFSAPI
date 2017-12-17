FROM python:alpine3.6

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install -U --no-cache-dir -r requirements.txt

COPY . .
VOLUME /usr/src/app/gtfs
CMD ["python", "gtfs_api/app.py"]
FROM python:3.7.2-alpine3.9

RUN apk add --no-cache --virtual build-dev gcc libc-dev libxml2-dev libxslt-dev

WORKDIR /srv
COPY . /srv
RUN pip install --no-cache-dir -r requirements.txt

RUN apk del build-dev
RUN apk add --no-cache libxml2 libxslt

CMD ["python", "./printer.py"]

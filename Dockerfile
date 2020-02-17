FROM python:3.8.1-alpine3.11

RUN apk add --no-cache --virtual build-dev gcc libc-dev libxml2-dev libxslt-dev

WORKDIR /srv
COPY . /srv
RUN pip install --no-cache-dir -r requirements.txt

RUN apk del build-dev
RUN apk add --no-cache libxml2 libxslt

CMD ["python", "./printer.py", "--daemon"]

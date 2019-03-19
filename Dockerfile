FROM python:3.7.2-alpine3.9

RUN apk add --no-cache gcc
RUN apk add --no-cache libc-dev
RUN apk add --no-cache libxml2-dev
RUN apk add --no-cache libxslt-dev

WORKDIR /srv
COPY . /srv
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "./printer.py"]

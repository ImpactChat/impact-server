FROM python:3

WORKDIR /app
COPY . ./

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app/impact

EXPOSE 8000:8000
COPY ./docker-entrsypoint.sh /storage/
RUN ls /storage

ENTRYPOINT [ "sh", "/storage/docker-entrypoint.sh" ]

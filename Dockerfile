FROM python:3

WORKDIR /app
COPY . ./

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app/impact

EXPOSE 8000:8000
COPY ./docker-entrypoint.sh /app/impact/
RUN ls

ENTRYPOINT [ "sh", "/app/impact/docker-entrypoint.sh" ]

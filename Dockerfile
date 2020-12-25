FROM python:3

WORKDIR /app
COPY . ./

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app/impact

EXPOSE 8000:8000
COPY ./docker-entrypoint.sh /storage/
RUN chmod 755 /storage/docker-entrypoint.sh

RUN ls /storage/

ENTRYPOINT ["/storage/docker-entrypoint.sh"]

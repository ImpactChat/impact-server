FROM python:3

WORKDIR /app
COPY . ./

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app/impact

EXPOSE 8000:8000
ADD docker-entrypoint.sh ./docker-entrypoint.sh

ENTRYPOINT ["sh", "docker-entrypoint.sh"]

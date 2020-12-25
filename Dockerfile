FROM python:3

WORKDIR /app
COPY . ./

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app/impact

EXPOSE 8000:8000
ADD docker-entrypoint.sh ./docker-entrypoint.sh

RUN ls

ENTRYPOINT ["./docker-entrypoint.sh"]
# CMD ["sh", "/storage/docker-entrypoint.sh"]
# CMD [ "daphne", "impact.asgi:application", "-b", "0.0.0.0" ]
# CMD [ "daphne", "impact.asgi:application", "-b", "0.0.0.0" ]

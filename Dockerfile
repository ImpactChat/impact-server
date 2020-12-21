FROM python:3

WORKDIR /app
COPY . ./

RUN pip install -r requirements.txt

WORKDIR /app/impact
EXPOSE 8000:8000

CMD [ "daphne", "impact.asgi:application", "-b", "0.0.0.0" ]

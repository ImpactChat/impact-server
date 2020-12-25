FROM python:3

WORKDIR /app
COPY . ./

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app/impact

RUN ls
RUN ls ../

RUN python manage.py collectstatic --no-input
RUN python manage.py makemigrations
RUN python manage.py migrate

EXPOSE 8000:8000

CMD [ "daphne", "impact.asgi:application", "-b", "0.0.0.0" ]


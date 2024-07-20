FROM python:3.9

WORKDIR /app

COPY . /app/

RUN pip install -r requirements.txt --no-cache-dir

EXPOSE 8000

CMD [ "python", "manage.py"]
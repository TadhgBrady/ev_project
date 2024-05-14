FROM python:3.12.3

WORKDIR /root
RUN pip install --upgrade pip
COPY ./app.py app/web
COPY ./requirements.txt app/web

CMD ["python", "app/web/app.py"]
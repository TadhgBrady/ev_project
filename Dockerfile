FROM python:3.12.3

WORKDIR /root
RUN pip install --upgrade pip
COPY ./app.py app/app.py
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

CMD ["python", "app/app.py"]
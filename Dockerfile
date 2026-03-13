FROM python:3.10

WORKDIR /app

COPY App/ /app/

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
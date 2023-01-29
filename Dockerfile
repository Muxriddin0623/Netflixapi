FROM python:3.10

WORKDIR /Netflix

COPY . /Netflix

RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["./entrypoint.sh"]

FROM python:3.9-slim-buster

WORKDIR /main

COPY . /main

RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP=main.py
ENV FLASK_RUN_PORT=5000

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]

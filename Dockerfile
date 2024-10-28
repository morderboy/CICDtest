FROM python:3

WORKDIR 'app'

COPY . .

RUN pip install -r requirements.txt

CMD ['uvicorn', 'main:app', '--reload']


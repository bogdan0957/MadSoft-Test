FROM python:latest

WORKDIR /fastapi_app

COPY ./requirements.txt /fastapi_app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /fastapi_app/requirements.txt

COPY . .

#WORKDIR scr
#
#CMD ["fastapi", "run", "main.py", "--port", "80"]


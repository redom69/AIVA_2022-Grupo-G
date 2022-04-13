FROM python:3.8

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

# We copy just the requirements.txt first to leverage Docker cache
COPY . .

RUN pip install -r requirements.txt

CMD [ "python", "./src/main.py"]
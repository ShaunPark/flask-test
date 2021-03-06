FROM ubuntu:latest
MAINTAINER coolage "coolage73@gmail.com"
RUN apt-get update -y
RUN apt-get install -y curl
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
EXPOSE 5000:5000/tcp
CMD ["app.py"]

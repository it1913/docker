FROM ubuntu:20.04
RUN apt update -y && apt upgrade -y && apt install python3-pip -y
RUN pip install Flask
WORKDIR /flask
ENV FLASK_APP="script"
CMD ["flask","run","--host=0.0.0.0"]

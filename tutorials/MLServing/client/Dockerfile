FROM python:3.9

WORKDIR /client
RUN apt update
RUN apt install -y wget vim gcc python3-dev
RUN pip3 install requests
COPY . .

EXPOSE 5000
# USER nobody
ENTRYPOINT ["tail", "-f", "/dev/null"]
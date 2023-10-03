FROM python:3.11
WORKDIR /app
COPY . /app
COPY requirements.txt .
RUN pip install --upgrade pip
RUN apt-get update
RUN apt-get install python3-pip python3-cffi python3-brotli libpango-1.0-0 libpangoft2-1.0-0 -y
RUN pip install -r requirements.txt
ENV PYTHONUNBUFFERED 1
COPY entrypoint.sh /entrypoint
RUN chmod +x ./entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
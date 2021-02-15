FROM python:3.9.1-buster

WORKDIR /pylast-exporter

COPY requirements.txt .
RUN pip --no-cache-dir install -r requirements.txt

COPY pylast-exporter.py .
ENTRYPOINT ["python", "pylast-exporter.py"]

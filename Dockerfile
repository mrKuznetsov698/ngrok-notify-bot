FROM python:3.9-slim

COPY requirements.txt .

RUN pip install -r requirements.txt && \
    echo "Packages was installed successful"

COPY . .

CMD python main.py

FROM python:3.11.0

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x /app/entrypoint.sh

EXPOSE 8217

ENTRYPOINT ["/app/entrypoint.sh"]


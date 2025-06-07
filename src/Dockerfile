FROM python:3.11.0
EXPOSE 8213
COPY requirements.txt .
RUN python -m pip install -r requirements.txt
WORKDIR /app
COPY . /app
RUN chmod +x /app/entrypoint.sh
CMD ["/app/entrypoint.sh"]

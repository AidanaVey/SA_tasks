FROM python:3-alpine
RUN mkdir /app
WORKDIR /app
COPY main.py /app
RUN pip install flask

EXPOSE 80
CMD ["python", "main.py"]

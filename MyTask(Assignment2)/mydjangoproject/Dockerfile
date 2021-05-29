FROM python:3.8
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/app/dm_rest


COPY ./req.txt /usr/app/req.txt
RUN pip install -r /usr/app/req.txt

COPY . /usr/app/dm_rest

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
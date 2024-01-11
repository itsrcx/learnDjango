FROM python:3.10.2

ENV PYTHONDONTWRITEBYTECODE 1 
ENV PYTHONUNBUFFERED 1

WORKDIR /blogApp

COPY requirements.txt /blogApp/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . /blogApp/

EXPOSE 8000

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]

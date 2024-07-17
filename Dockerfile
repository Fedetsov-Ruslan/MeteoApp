FROM python:3.12.2-slim-bullseye

ENV PYTHONUNBUFFERED=1
ENV PYTHONUNBUFFERED=1

WORKDIR /METEOAPP

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


# SHELL [ "/bin/bash", "-c" ]

# ENV PYTHONUNBUFFERED=1
# ENV PYTHONUNBUFFERED=1

# WORKDIR /METEOAPP

# RUN python -m pip install --upgrade pip
# COPY . .
# RUN pip install -r requirements.txt

# CMD ["python", "manage.py", "runserver", "192.168.100.3:8000"]

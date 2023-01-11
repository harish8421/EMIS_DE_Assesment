#Dockerfile
FROM python:3.8

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

ADD FHIR2CSV.py . 

RUN pip install json csv

CMD ["python", "./FHIR2CSV.py"]
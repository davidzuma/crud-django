# pull official base image
FROM python:3.11.4-slim-buster

# set work directory
WORKDIR /usr/src/financial_project

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update && apt-get install -y netcat \
    python3-dev \
    gcc && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/financial_project/entrypoint.sh
RUN chmod +x /usr/src/financial_project/entrypoint.sh

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/usr/src/financial_project/entrypoint.sh"]
## base image
FROM python:slim-buster AS compile-image

## install dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential

## virtualenv
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

## add and install requirements
RUN pip install --upgrade pip

WORKDIR /usr/src/app

COPY requirements.install .
RUN pip install -r requirements.install

COPY . .
RUN pip install -e '.[dev]'

ENTRYPOINT ["./docker/entrypoint.sh"]

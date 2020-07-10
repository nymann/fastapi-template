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
COPY setup.cfg .
RUN python3 -c "import configparser; c = configparser.ConfigParser(); c.read('setup.cfg'); print(c['options']['install_requires'])" | xargs pip install

WORKDIR /usr/src/app
COPY . .
RUN pip install -e .

ENTRYPOINT ["./docker/entrypoint.sh"]

## base image
FROM python:slim-buster AS compile-image

## install dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc

## virtualenv
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Set git version number from arg.
ARG VERSION
ENV GIT_VERSION="$VERSION"

## add and install requirements
RUN pip install --upgrade pip
COPY setup.cfg .
RUN python3 -c "import configparser; c = configparser.ConfigParser(); c.read('setup.cfg'); print(c['options']['install_requires'])" | xargs pip install

WORKDIR /usr/src/app
COPY . .
RUN pip install .

#FROM python:slim-buster AS runtime-image
#
### install nc
#RUN apt-get update && \
#    apt-get install -y --no-install-recommends netcat-openbsd
#
### copy Python dependencies from build image
#COPY --from=compile-image /opt/venv /opt/venv
#
### set working directory
#WORKDIR /usr/src/app
#
### add user
#RUN addgroup --system user && adduser --system --no-create-home --group user
#RUN chown -R user:user /usr/src/app && chmod -R 755 /usr/src/app
#
### add entrypoint.sh
#COPY docker/entrypoint.sh /usr/src/app/entrypoint.sh
#RUN chmod +x /usr/src/app/entrypoint.sh
#
### switch to non-root user
#USER user
#
### add config
#COPY . /usr/src/app/
#
### set environment variables
#ENV PYTHONDONTWRITEBYTECODE 1
#ENV PYTHONUNBUFFERED 1
#ENV PATH="/opt/venv/bin:$PATH"
CMD ["./entrypoint.sh"]

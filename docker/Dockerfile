## base image
FROM python:slim-buster AS compile-image

## install dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential

RUN addgroup --gid 1000 fastapi_template
RUN adduser --uid 1000 \
            --gid 1000 \
            --home /home/fastapi_template \
            --quiet \
            --disabled-password \
            fastapi_template

USER fastapi_template
WORKDIR /home/fastapi_template

## virtualenv
ENV VIRTUAL_ENV=/home/fastapi_template/.venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN mkdir app
WORKDIR /home/fastapi_template/app

## add and install requirements
RUN pip install --upgrade pip

COPY --chown=fastapi_template:fastapi_template requirements.install .
RUN pip install -r requirements.install

COPY --chown=fastapi_template:fastapi_template . .
RUN pip install -e '.[dev]'

ENTRYPOINT ["./docker/entrypoint.sh"]

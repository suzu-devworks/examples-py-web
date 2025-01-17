FROM python:3-slim-bookworm AS dev-stage
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
RUN set -x \
    && apt update \
    && apt install --no-install-recommends -y sqlite3 \
    && apt install --no-install-recommends -y gcc python3-dev \
    ;

# build
FROM dev-stage AS build-stage
WORKDIR /app
COPY . /app
RUN uv sync --no-dev
RUN uv build

RUN uv pip --no-cache-dir install uwsgi

# deploy
FROM python:3-slim-bookworm AS deploy-stage
WORKDIR /app

RUN set -x \
    && apt update \
    && apt install --no-install-recommends -y libexpat1 \
    ;

# Warning: It's working but I don't know if it's correct.
COPY --from=build-stage /app/.venv/bin/uwsgi /usr/local/bin/

COPY --from=build-stage /app/dist/* /app/
RUN pip install --no-cache-dir /app/examples_flask-*.whl

RUN set -x \
    && apt clean -y \
    && rm -rf /var/lib/apt/lists/* \
    ;

COPY --from=build-stage /app/uwsgi.ini /app/
COPY --from=build-stage /app/src/examples_flask/wsgi.py /app/src/examples_flask/
COPY --from=build-stage /app/src/flaskr/wsgi.py /app/src/flaskr/

EXPOSE 3031
CMD [ "uwsgi", "--ini", "uwsgi.ini", "--uid", "nobody"]

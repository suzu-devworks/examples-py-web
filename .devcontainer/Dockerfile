ARG VARIANT="0-3.11"

# > docker build --target develop-stage .
FROM mcr.microsoft.com/devcontainers/python:${VARIANT} as develop-stage

## Configure apt and install packages
RUN set -x \
    && apt update \
    && apt sqlite3 \
    ;

# Clean up
RUN set -x \
    && apt autoremove -y \
    && apt clean -y \
    && rm -rf /var/lib/apt/lists/* \
    ;

FROM mcr.microsoft.com/devcontainers/base:bookworm as dev-stage

## Configure apt and install packages
RUN set -x \
    && apt update \
    && apt install -y sqlite3 \
    && apt install -y libgl1-mesa-dev netcat-openbsd netcat-traditional \
    ;

# Clean up
RUN set -x \
    && apt autoremove -y \
    && apt clean -y \
    && rm -rf /var/lib/apt/lists/* \
    ;

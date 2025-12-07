FROM mcr.microsoft.com/devcontainers/base:ubuntu

## Configure apt and install packages
RUN set -x \
    && apt update \
    && apt install --no-install-recommends -y libgl1-mesa-dev libglib2.0-0 \
    ;

# Clean up
RUN set -x \
    && apt autoremove -y \
    && apt clean -y \
    && rm -rf /var/lib/apt/lists/* \
    ;

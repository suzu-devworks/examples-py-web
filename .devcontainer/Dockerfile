ARG VARIANT="bookworm"
FROM mcr.microsoft.com/devcontainers/base:${VARIANT} as dev-stage

## Configure apt and install packages
RUN set -x \
    && apt update \
    && apt install -y sqlite3 \
    && apt install -y libgl1-mesa-dev netcat-openbsd netcat-traditional \
    ;

# https://cloud.google.com/sdk/docs/install-sdk?hl=ja
RUN echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list \
    && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo gpg --dearmor -o /usr/share/keyrings/cloud.google.gpg \
    && apt update -y \
    && apt install google-cloud-sdk -y

# Clean up
RUN set -x \
    && apt autoremove -y \
    && apt clean -y \
    && rm -rf /var/lib/apt/lists/* \
    ;

FROM ghcr.io/ludeeus/debian/python:stable

ENV DEBIAN_FRONTEND=noninteractive

COPY action /action/
COPY requirements.txt /tmp/requirements.txt

RUN \
    mkdir -p /github/workspace \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
        git \
    && python3 -m pip install \
        --no-cache-dir \
        -r /tmp/requirements.txt \
        --disable-pip-version-check \
    \
    && find /usr/local \
        \( -type d -a -name test -o -name tests -o -name '__pycache__' \) \
        -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
        -exec rm -rf '{}' \; \
    && apt-get clean -y \
    && rm -fr /var/lib/apt/lists/* \
    && rm -fr /tmp/* /var/{cache,log}/*

WORKDIR "/github/workspace"
ENTRYPOINT ["bash", "/action/run.sh"]
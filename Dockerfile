FROM ghcr.io/ludeeus/debian/python:stable

COPY action /action/
COPY requirements.txt /tmp/requirements.txt

RUN \
    python3 -m pip install \
        --no-cache-dir \
        -r /tmp/requirements.txt \
        --disable-pip-version-check \
    \
    && find /usr/local \
        \( -type d -a -name test -o -name tests -o -name '__pycache__' \) \
        -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
        -exec rm -rf '{}' \;

WORKDIR "/github/workspace"
ENTRYPOINT ["bash", "/action/run.sh"]
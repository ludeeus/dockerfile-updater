FROM ludeeus/container:python-base

COPY action /action/

RUN \
    python3 -m pip install --no-cache-dir -U \
        alpinepkgs==1.1.2 \
        PyGithub==1.47 \
    \
    && find /usr/local \
        \( -type d -a -name test -o -name tests -o -name '__pycache__' \) \
        -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
        -exec rm -rf '{}' \;

WORKDIR "/github/workspace"
ENTRYPOINT ["bash", "/action/run.sh"]
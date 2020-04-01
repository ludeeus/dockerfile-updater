FROM alpine:0.0.0
ARG S6_VERSION="0.0.0"

RUN \
    apk add --no-cache \
        test=0.0.0 \
        package=0.0.0

FROM debian:0.0

RUN \
    python3 -m pip install --no-cache-dir -U \
        test==0.0.0 \
        package==0.0.0 \
        not-valid>=0.0.0

RUN pip install test-package==0.0.0

FROM debian:0.0-slim

RUN \
    apt update \
    \
    && apt install -y --no-install-recommends  \
        test=0.0.0 \
        package=0.0.0
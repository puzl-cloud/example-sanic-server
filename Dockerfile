FROM python:3.8-slim

LABEL maintainer=sergey.monakhov@gmail.com \
      vendor=puzl.ee

ENV USER=ubuntu \
    UID=1000 \
    GID=1000

SHELL ["/bin/bash", "-c"]

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
         build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ARG TINI_VERSION=v0.19.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/local/bin/tini

RUN addgroup --gid "$GID" "$USER" \
    && adduser \
         --disabled-password \
         --gecos "" \
         --ingroup "$USER" \
         --uid "$UID" \
         --shell /bin/bash \
         "$USER"

COPY . /usr/src/app/

WORKDIR /usr/src/app/

RUN python3 -m pip install -r requirements.txt \
    && chown $USER:$USER /usr/src/app \
    && chmod +x /usr/local/bin/*

RUN apt-get remove -y \
      build-essential \
    && apt-get clean \
    && apt-get autoclean -y \
    && apt-get autoremove -y \
    && rm -rf \
        /var/cache/debconf \
        /tmp/*

USER $UID

EXPOSE 1616

ENTRYPOINT ["/usr/local/bin/tini", "--"]
CMD ["python3", "app.py"]

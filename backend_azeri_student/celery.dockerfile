FROM ubuntu:18.04
ENV PYTHONUNBUFFERED 1

ENV APP_ROOT /src
# Configure apt to get GDAL files from testing repository
RUN mkdir /src;

RUN apt-get update -y
RUN apt-get install software-properties-common -y
RUN add-apt-repository ppa:deadsnakes/ppa

RUN apt-get update -y && apt-get install -y \
  build-essential \
  python3.7 \
  python3.7-venv \
  python3.7-dev \
  libpq-dev \
  libjpeg-dev \
  binutils \
  libproj-dev \
  gdal-bin \
  libxml2-dev \
  libxslt1-dev \
  zlib1g-dev \
  libffi-dev \
  libssl-dev \
  language-pack-pt \
  python3-gdal


WORKDIR ${APP_ROOT}
RUN export DISPLAY=':0.0'
RUN mkdir /config
ADD requirements.txt /config/
RUN python3.7 -m venv /venv
RUN /venv/bin/pip install -U pip
RUN /venv/bin/pip install --no-cache-dir -r /config/requirements.txt

ADD . ${APP_ROOT}

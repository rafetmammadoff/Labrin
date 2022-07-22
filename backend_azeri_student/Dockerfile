FROM ubuntu:18.04

# Ensure that Python outputs everything that's printed inside
# the application rather than buffering it.
ENV PYTHONUNBUFFERED 1
ENV APP_ROOT /code

RUN apt-get update -y
RUN apt-get install software-properties-common -y
RUN add-apt-repository ppa:deadsnakes/ppa

RUN apt-get update && apt-get install -y \
  build-essential \
  python3.7 \
  python3.7-dev \
  python3.7-venv \
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

## Copy in your requirements file


ADD requirements.txt /requirements.txt
## Install build deps, then run `pip install`, then remove unneeded build deps all in a single step. Correct the path to your production requirements file, if needed.
RUN python3.7 -m venv /venv
RUN /venv/bin/pip install -U pip
RUN /venv/bin/pip install --no-cache-dir -r /requirements.txt
RUN /venv/bin/pip install --no-cache-dir uwsgi


# Copy your application code to the container (make sure you create a .dockerignore file if any large files or directories should be excluded)
RUN mkdir ${APP_ROOT}
WORKDIR ${APP_ROOT}
ADD . ${APP_ROOT}
COPY mime.types /etc/mime.types

# uWSGI will listen on this port
EXPOSE 8030

# Call collectstatic (customize the following line with the minimal environment variables needed for manage.py to run):
RUN #if [ -f manage.py ]; then /venv/bin/python manage.py collectstatic --noinput; fi

# Start uWSGI
CMD [ "/venv/bin/uwsgi", "--ini", "/code/uwsgi.ini"]

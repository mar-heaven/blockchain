FROM centos/python-38-centos7
USER root
WORKDIR /tmp

COPY requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt \
&&  rm -f /tmp/requirements.txt

COPY ./dist/* /tmp/build/

RUN pip install \
    /tmp/build/*  \
&&  rm -rf /tmp/build

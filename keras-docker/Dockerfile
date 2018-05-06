FROM tensorflow/tensorflow:latest-gpu

# Install system packages
RUN apt-get update && apt-get install -y --no-install-recommends \
      git \
      graphviz \
      libgl1-mesa-glx \
      libhdf5-dev \
      openmpi-bin \
      python3-pip \
      python3-venv && \
    rm -rf /var/lib/apt/lists/*

ENV NB_USER keras
ENV NB_UID 1000

RUN useradd -m -s /bin/bash -N -u $NB_UID $NB_USER

USER $NB_USER

ARG keras_version=2.1.6
RUN python3 -m pip install --user -U pip && \
    python3 -m pip install --user setuptools && \
    python3 -m pip install --user git+git://github.com/keras-team/keras.git@${keras_version}

WORKDIR /src

EXPOSE 8888

# CMD jupyter notebook --port=8888 --ip=0.0.0.0

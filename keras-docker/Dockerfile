ARG cuda_version=9.1
ARG cudnn_version=7
FROM nvidia/cuda:${cuda_version}-cudnn${cudnn_version}-devel

RUN apt-get update && apt-get install -y --no-install-recommends \
      git \
      graphviz \
      libgl1-mesa-glx \
      libhdf5-dev \
      openmpi-bin \
      software-properties-common && \
    rm -rf /var/lib/apt/lists/*

# Recent Python version
RUN add-apt-repository ppa:deadsnakes/ppa
ARG python_version=3.6
RUN apt-get update && apt-get install -y --no-install-recommends \
      python3-pip \
      python3-wheel \
      python${python_version} \
      python${python_version}-dev \
      python${python_version}-venv && \
    rm -rf /var/lib/apt/lists/*
RUN ln -sf /usr/bin/python3{.6,}

ENV NB_USER keras
ENV NB_UID 1000

RUN useradd -m -s /bin/bash -N -u $NB_UID $NB_USER && \
    mkdir -p /venv && \
    chown $NB_USER /venv

# TensorFlow doesn't currently build with Bazel 0.13.0
# RUN echo "deb [arch=amd64] http://storage.googleapis.com/bazel-apt stable jdk1.8" > /etc/apt/sources.list.d/bazel.list && \
#     wget -qO- https://bazel.build/bazel-release.pub.gpg | apt-key add - && \
#     apt-get update && \
#     apt-get install -y bazel && \
#     rm -rf /var/lib/apt/lists/*

USER $NB_USER
WORKDIR /home/$NB_USER

ARG keras_version=2.1.6

RUN python${python_version} -m pip install --user -U pip && \
    python${python_version} -m pip install --user numpy setuptools && \
    python${python_version} -m pip install --user tensorflow==1.5.0 && \
    python${python_version} -m pip install --user git+git://github.com/keras-team/keras.git@${keras_version}

WORKDIR /src

EXPOSE 8888

# CMD jupyter notebook --port=8888 --ip=0.0.0.0

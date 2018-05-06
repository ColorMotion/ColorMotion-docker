ARG cuda_version=9.0
ARG cudnn_version=7
FROM nvidia/cuda:${cuda_version}-cudnn${cudnn_version}-devel

# Install system packages
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
      python${python_version} \
      python${python_version}-venv && \
    rm -rf /var/lib/apt/lists/*

# Install Python packages and keras
ENV NB_USER keras
ENV NB_UID 1000

RUN useradd -m -s /bin/bash -N -u $NB_UID $NB_USER && \
    mkdir -p /venv && \
    chown $NB_USER /venv

USER $NB_USER

ARG keras_version=2.1.6

RUN python${python_version} -m pip install -U pip && \
    python${python_version} -m pip install setuptools && \
    python${python_version} -m pip install \
      tensorflow-gpu==1.8.0 \
      https://cntk.ai/PythonWheel/GPU/cntk-2.1-cp36-cp36m-linux_x86_64.whl && \
    python${python_version} -m pip install git+git://github.com/keras-team/keras.git@${keras_version}

WORKDIR /src

EXPOSE 8888

# CMD jupyter notebook --port=8888 --ip=0.0.0.0

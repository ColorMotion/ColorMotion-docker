ARG cuda_version=9.1
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
      python3-dev \
      python3-numpy \
      python3-pip \
      python3-wheel \
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

RUN python${python_version} -m pip install --user -U pip && \
    python${python_version} -m pip install --user setuptools && \
    python${python_version} -m pip install --user git+git://github.com/keras-team/keras.git@${keras_version}

RUN git clone https://github.com/tensorflow/tensorflow && \
    cd tensorflow && \
    git checkout r1.8 && \
    CC_OPT_FLAGS="-march=native" \
    CUDA_TOOLKIT_PATH=/usr/local/cuda \
    CUDNN_INSTALL_PATH=/usr/lib/x86_64-linux-gnu \
    GCC_HOST_COMPILER_PATH=$(which gcc) \
    PYTHON_BIN_PATH=$(which python3.5) \
    PYTHON_LIB_PATH="$($PYTHON_BIN_PATH -c 'import site; print(site.getsitepackages()[0])')" \
    TF_CUDA_CLANG=0 \
    TF_CUDA_COMPUTE_CAPABILITIES=6.1 \
    TF_CUDA_VERSION=9.1 \
    TF_CUDNN_VERSION=7.0 \
    TF_DOWNLOAD_MKL=0 \
    TF_ENABLE_XLA=0 \
    TF_NCCL_VERSION=1.3 \
    TF_NEED_CUDA=1 \
    TF_NEED_GCP=0 \
    TF_NEED_GDR=0 \
    TF_NEED_HDFS=0 \
    TF_NEED_JEMALLOC=1 \
    TF_NEED_KAFKA=0 \
    TF_NEED_MKL=0 \
    TF_NEED_MPI=0 \
    TF_NEED_OPENCL_SYCL=0 \
    TF_NEED_OPENCL=0 \
    TF_NEED_S3=0 \
    TF_NEED_TENSORRT=0 \
    TF_NEED_VERBS=0 \
    TF_SET_ANDROID_WORKSPACE=0 \
    ./configure

WORKDIR /src

EXPOSE 8888

# CMD jupyter notebook --port=8888 --ip=0.0.0.0

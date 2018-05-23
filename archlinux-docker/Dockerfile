FROM base/archlinux

RUN pacman -Syu --noconfirm \
    git \
    hdf5 \
    libsm \
    libxrender \
    python-pip \
    python-tensorflow-cuda \
    tensorflow-cuda \
    && yes | pacman -Scc

WORKDIR /volume

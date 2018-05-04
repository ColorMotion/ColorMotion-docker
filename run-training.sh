if which nvidia-docker > /dev/null 2>&1 ; then
    DOCKER=nvidia-docker
else
    cat >&2 << EOF
*********************************
************ WARNING ************
*********************************
nvidia-docker not found, GPU acceleration won't be supported!
*********************************
EOF
    DOCKER=docker
fi

sudo $DOCKER run --rm -v "$PWD/volume:/volume" tiagoshibata/keras:latest /volume/run $@

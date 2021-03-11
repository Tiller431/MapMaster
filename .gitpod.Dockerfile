FROM gitpod/workspace-full

USER gitpod

RUN sudo apt-get -q update && \
    sudo apt install -y python3 python3-pip


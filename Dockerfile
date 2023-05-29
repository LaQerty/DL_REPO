FROM ubuntu:22.10
FROM python:3.8.16

RUN apt-get update
RUN python3.8 -m venv my_venv

RUN . my_venv/bin/activate && \
    pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118 &&\
    pip install https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.8.0-py3-none-any.whl &&\
    pip install --upgrade jax jaxlib flax timm &&\
    pip install git+https://github.com/huggingface/transformers

COPY entrypoint.sh .
COPY lab1.py .
COPY my_result.txt .

RUN chmod +x entrypoint.sh

ENTRYPOINT ./entrypoint.sh

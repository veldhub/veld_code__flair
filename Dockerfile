FROM python:3.11.11
RUN pip install notebook==7.3.2
RUN pip install flair==0.15.0
WORKDIR /veld/code/notebooks/
ENV FLAIR_CACHE_ROOT="/veld/input/models_cache/"


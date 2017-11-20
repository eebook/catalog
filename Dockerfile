FROM python:3.6.0rc2-alpine
LABEL maintainer="knarfeh@outlook.com"

# build pkgs
RUN apk --update add gcc g++ python3-dev musl-dev make curl

COPY requirements.txt /requirements.txt
RUN pip3 install -U pip \
    && pip install -i https://pypi.douban.com/simple -r requirements.txt
COPY . /src/
WORKDIR /src
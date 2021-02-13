FROM python:3.7-alpine

ENV PATH="/scripts:${PATH}"

COPY requirements.txt /requirements.txt

RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers
RUN pip install -r /requirements.txt

RUN mkdir /app
COPY ./src /app
WORKDIR /app
COPY ./scripts /scripts

# executable permissions to all scripts
RUN chmod +x /scripts/*

# add folders for media and static
RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

# create user
RUN adduser -D user
RUN chown -R user:user /vol

#provide folder permissions to the user
RUN chmod -R 755 /vol/web

# run as user instead of root
USER user

# expose docker 8000 portions
# EXPOSE 8000

# commands
CMD entrypoint.sh
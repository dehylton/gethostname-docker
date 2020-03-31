FROM alpine:latest
RUN apk add --no-cache py3-aiohttp \
    && rm -f /var/cache/apk/*
EXPOSE 8080
COPY server.py /
CMD [ "python3", "-u", "server.py" ]

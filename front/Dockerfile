FROM node:lts-alpine

WORKDIR /usr/src/app
COPY vue.config.js .

RUN npm install -g npm @vue/cli@3.11.0

# EXPOSE 8080

CMD ["/bin/sh"]
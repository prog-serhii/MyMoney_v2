# BUILDER
# pull official base image
FROM node:13.12.0-alpine as builder

# set work directory
WORKDIR /usr/src/frontend

# copy react project
# install dependencies and avoid `node-gyp rebuild` errors
COPY ./package.json .
RUN apk add --no-cache --virtual .gyp \
        python \
        make \
        g++ \
    && npm install \
    && apk del .gyp

COPY . .

RUN npm run build

# FINAL
# pull official base image
FROM node:13.12.0-alpine

# set work directory
WORKDIR /usr/src/frontend

# install serve - deployment static server suggested by official create-react-app
RUN npm install -g serve

# copy our build files from our builder stage
COPY --from=builder /usr/src/frontend/build ./build
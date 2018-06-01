#!/usr/bin/env bash

VERSION=1.0

docker build --force-rm -t aviasales_hakaton:${VERSION} -f ./Dockerfile ..

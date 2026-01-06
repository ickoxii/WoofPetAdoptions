#!/usr/bin/env bash

set -x

kill -9 $(lsof -ti :8080)
pkill node

docker compose -f docker/local.docker-compose.yml down db -v

pushd pet-adoption-frontend
rm -r node_modules .next
popd

pushd mock-data
rm -r uploads _json .venv logs
popd

# prune
docker image prune -af
docker system prune -f

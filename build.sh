#!/usr/bin/env bash

set -x

docker compose -f docker/local.docker-compose.yml up db -d --build

pushd pet-adoption-frontend
yarn install
yarn run dev &
popd

pushd pet-adoption-api
./gradlew build --no-daemon -p . -x test
java -jar build/libs/pet-adoption-api-1.0.0-SNAPSHOT.jar &
popd

pushd mock-data
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 generate.py local small --new
deactivate
popd

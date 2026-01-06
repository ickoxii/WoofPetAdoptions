# Local Bootstrap

## Start the Database

```sh
docker compose -f docker/local.docker-compose.yml up db -d
```

## Start the Backend

```sh
cd pet-adoption-api
./gradlew build --no-daemon -p . -x test
java -jar build/libs/pet-adoption-api-1.0.0-SNAPSHOT.jar
```

## Start the Frontend

```sh
cd pet-adoption-frontend
yarn install
yarn run dev
```

## Seed with Mock Data

```sh
cd mock-data

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python3 generate.py local small --new
```

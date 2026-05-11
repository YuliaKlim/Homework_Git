docker network create academy-net

docker run --name db_postgres --network academy-net -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=academy -d postgres

docker build -t academy-app .
docker run --rm --network academy-net academy-app


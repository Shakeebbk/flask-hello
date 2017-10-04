# flask-hello

docker build -t hello .
docker run -p 4000:80 -v <local-path>:/app hello

docker swarm init
docker stack deploy -c docker-compose.yml hello

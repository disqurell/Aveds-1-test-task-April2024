# TestTask Readme 

## To run project:
1. Install `docker`

```sh
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh ./get-docker.sh
```

2. Create `.env` file inside `aveds_1_test_task` with:
```sh
DB_NAME=""
DB_USER=""
DB_PASSWORD=""
DB_HOST=""
DB_PORT=""
```

3. Run this commands:
```sh
# Copy docker files to root dir
cp aveds_1_test_task/deploy/docker-compose.yml ./ && cp aveds_1_test_task/deploy/Dockerfile ./

# Run docker compose file
sudo docker compose up -d
```

### Check [api docs at browser](http://localhost:8090/api/docs/)

## To stop and delete containers 
```sh
# Warning: It removes containers, volumes and networks.

# If you want to restart/stop better use docker compose restart/stop

sudo docker compose down
```
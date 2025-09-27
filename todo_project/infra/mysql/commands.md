## you can either use docker-compose.yml file to run the mysql instance

cd infra/mysql
docker compose up -d

# logs (optional)
docker compose logs -f

# keeps data (volume persists)
docker compose down       




## or can use script (powershell)


# start_mysql.ps1 (PowerShell)
docker volume create mysql_data | Out-Null
docker run --name mysqllocal --restart unless-stopped -d `
  -e MYSQL_ROOT_PASSWORD=RootPass!123 `
  -e MYSQL_DATABASE=todo_db `
  -e MYSQL_USER=todo_user `
  -e MYSQL_PASSWORD=StrongPassword!123 `
  -p 3306:3306 `
  -v mysql_data:/var/lib/mysql `
  mysql:8

# Verify it’s up
docker ps
docker logs -f mysqllocal   
# wait for “ready for connections”

# stop_mysql.ps1
# volume mysql_data remains (your data stays)
docker stop mysqllocal
docker rm mysqllocal



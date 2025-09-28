


# --- Compose workflow ---
# you can use service name here

# go to the compose folder
cd infra/mysql

# start MySQL (uses .env next to compose file)
docker compose up -d

# tail logs (Ctrl+C to stop viewing)
docker compose logs -f mysql

# check service + port mapping
docker compose ps
docker compose port mysql 3306   # expect 0.0.0.0:3306

# open a MySQL shell as root (will prompt for MYSQL_ROOT_PASSWORD)
docker compose exec mysql mysql -uroot -p

# if succesfull; will get into mysql terminal. there you have to run this to create new db, user, privilages for your project
CREATE DATABASE IF NOT EXISTS <MYSQL_DATABASE>
  CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

  CREATE USER IF NOT EXISTS '<MYSQL_USER>'@'%'
  IDENTIFIED WITH caching_sha2_password BY '<MYSQL_PASSWORD>';

ALTER USER '<MYSQL_USER>'@'%' IDENTIFIED BY '<MYSQL_PASSWORD>';
GRANT ALL PRIVILEGES ON <MYSQL_DATABASE>.* TO '<MYSQL_USER>'@'%';
FLUSH PRIVILEGES;

-- sanity checks
SELECT user,host,plugin FROM mysql.user WHERE user='<MYSQL_USER>';
SHOW GRANTS FOR '<MYSQL_USER>'@'%';

<!-- # with sample value

CREATE DATABASE IF NOT EXISTS e_store_db
  CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

  CREATE USER IF NOT EXISTS 'e_store_user'@'%'
  IDENTIFIED WITH caching_sha2_password BY 'sFDFH,!123';

ALTER USER 'e_store_user'@'%' IDENTIFIED BY 'sFDFH,!123';
GRANT ALL PRIVILEGES ON e_store_db.* TO 'e_store_user'@'%';
FLUSH PRIVILEGES;

-- sanity checks
SELECT user,host,plugin FROM mysql.user WHERE user='e_store_user';
SHOW GRANTS FOR 'e_store_user'@'%';
 -->


# if all works fine, exit from the mysql terminal and go to README.md from where you had come here. And run the application. After completion; route again to this path and run following commands to stop docker container.

# to stop container (keeps data volume)
docker compose down

# DANGER: remove container + data volume
docker compose down -v







#    ---------OR-----------








# --- Docker run workflow (PowerShell) ---
# you need to use container name here

# ensure the compose container isn't running
# (only needed if you used compose earlier)
docker compose -f infra/mysql/docker-compose.yml down

# create/keep a named volume for persistent data
docker volume create mysql_data | Out-Null

# start container with the SAME creds you use in .env/compose
docker run --name mysqllocal --restart unless-stopped -d `
  -e MYSQL_ROOT_PASSWORD=RootPassword `
  -e MYSQL_DATABASE=dbName `
  -e MYSQL_USER=userName `
  -e MYSQL_PASSWORD="dbPassword" `
  -p 3306:3306 `
  -v mysql_data:/var/lib/mysql `
  mysql:8

# verify it's up
docker ps
docker logs -f mysqllocal
docker port mysqllocal 3306

# stop/remove container only (keeps data in mysql_data)
docker stop mysqllocal
docker rm mysqllocal

# DANGER: remove the data volume entirely
docker volume rm mysql_data





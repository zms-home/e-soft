Запускаем контейнеры
docker-compose up -d

Далее настраиваем конфигурацию ведущий-ведомый

Заходим на подчиненный узел:

docker-compose exec -it mysql_slave bash

mysql -u root -p

mysql> CHANGE MASTER TO MASTER_HOST='mysql_master', MASTER_USER='root', MASTER_PASSWORD='password'
mysql> start slave;

Проверьте статус подчиненного узла:

mysql> show slave status\G;

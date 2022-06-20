Запускаем контейнеры

<blockquote>docker-compose up -d</blockquote>

Далее настраиваем конфигурацию ведущий-ведомый

Заходим на подчиненный узел:

<blockquote>docker-compose exec -it mysql_slave bash</blockquote>

<blockquote>mysql -u root -p</blockquote>

<blockquote>mysql> CHANGE MASTER TO MASTER_HOST='mysql_master', MASTER_USER='root', MASTER_PASSWORD='password'</blockquote>
<blockquote>mysql> start slave;</blockquote>

Проверьте статус подчиненного узла:

<blockquote>mysql> show slave status\G;</blockquote>

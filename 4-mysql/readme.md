Запускаем контейнеры

<blockquote>docker-compose up -d</blockquote>

Далее настраиваем конфигурацию ведущий-ведомый

Заходим на подчиненный узел:

<blockquote>docker-compose exec -it mysql_slave bash</blockquote>

Вводим

<blockquote>mysql -u root -p</blockquote>

Указываем слэйву мастер хост

<blockquote>mysql> CHANGE MASTER TO MASTER_HOST='mysql_master', MASTER_USER='root', MASTER_PASSWORD='password'</blockquote>

Устанавливаем этот хост как слэйв

<blockquote>mysql> start slave;</blockquote>

Проверяем статус слэйва:

<blockquote>mysql> show slave status\G;</blockquote>

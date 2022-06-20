<blockquote> 
version: '3'</br>

services:</br>
  nginx:</br>
    #Указываем образ и тэг</br>
    image: nginx:1.21.6</br>
    #Задаем контейнеру имя</br>
    container_name: webserver</br>
    restart: on-failure</br>
    #Пробрасываем порты</br>
    ports:</br>
      - 8080:80</br>
      - 443:443</br>
    #Монтируем волумы</br>
    volumes:</br>
     - ./www:/var/www</br>
     - ./conf.d:/etc/nginx/conf.d</br>
     - ./conf/nginx.conf:/etc/nginx/nginx.conf</br>
     - ./modules:/modules</br>
     
</blockquote> 



<p>Настройки блока server ложим в ./conf.d в файл cfg.conf в котором настраиваем определение UserAgent и дальнейшее действие:

<blockquote>
</br>
server {
        listen 80;
        listen [::]:80;

        if ($http_user_agent ~* "(iphone|android|blackberry)") {
        rewrite ^(.*)$ /liteversion/index.html break;
        }
        root /var/www/;
        index index.html index.htm index.nginx-debian.html;

        server_name localhost;

        location / {
                try_files $uri $uri/ =404;

}
}
  
</blockquote>

<p>В нашем случае при  UserAgent "(iphone|android|blackberry)" будем открывать страницу, которая лежит в директории www/liteversion/


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

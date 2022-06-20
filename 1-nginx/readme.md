version: '3'

services:
  nginx:
    #Указываем образ и тэг
    image: nginx:1.21.6
    #Задаем контейнеру имя
    container_name: webserver
    restart: on-failure
    #Пробрасываем порты
    ports:
      - 8080:80
      - 443:443
    #Монтируем волумы
    volumes:
     - ./www:/var/www
     - ./conf.d:/etc/nginx/conf.d
     - ./conf/nginx.conf:/etc/nginx/nginx.conf
     - ./modules:/modules

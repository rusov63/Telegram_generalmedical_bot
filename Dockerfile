### чистые настройки для бота без redis
#FROM python:3.12-slim
## Debian GNU/Linux 10, python без компилятора
#
## устанавливаем рабочую директорию внутри контейнера.
#WORKDIR /projects
#
## Копируем и устанавливаем зависимости Python
#COPY requirements.txt .
#RUN pip install --no-cache-dir -r requirements.txt
#
## Копируем все файлы из текущей директории в рабочую директорию контейнера
#COPY . .
#
## Команда запуска контейнера
#CMD ["python", "run.py"]

# Настройка Redis c запуском python bota
FROM python:3.12-slim

# Устанавливаем необходимые пакеты, включая Redis
RUN apt-get update && apt-get install -y redis-server

# Указываем, что контейнер будет слушать на порту 6379
EXPOSE 6379

# Устанавливаем рабочую директорию внутри контейнера.
WORKDIR /projects

# Копируем и устанавливаем зависимости Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы из текущей директории в рабочую директорию контейнера
COPY . .

# Копируем конфигурационный файл Redis и прокладываем путь где будет храниться файл
COPY redis.conf /projects/redis.conf

# Запускаем Redis с конфигурационным файлом, затем приложение
CMD redis-server /projects/redis.conf & python run.py


## Используем официальный образ Redis
#FROM redis:alpine3.20
#
## Устанавливаем рабочую директорию
#WORKDIR /projects
#
## Копируем конфигурационный файл Redis, если он есть
#COPY redis.conf /projects/redis.conf
#
## Открываем порт для Redis
#EXPOSE 6379
#
## Запускаем Redis с указанным конфигурационным файлом
#CMD ["redis-server", "/projects/redis.conf"]

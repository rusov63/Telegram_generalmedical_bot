## чистые настройки для бота без redis
#FROM python:3.12-slim
## Debian GNU/Linux 10, python без компилятора
#
## устанавливаем рабочую директорию внутри контейнера.
#WORKDIR /app
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


FROM python:3.12-slim

# Устанавливаем необходимые пакеты, включая Redis
RUN apt-get update && apt-get install -y redis-server

# Указываем, что контейнер будет слушать на порту 6379
EXPOSE 6379

# Устанавливаем рабочую директорию внутри контейнера.
WORKDIR /app

# Копируем и устанавливаем зависимости Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы из текущей директории в рабочую директорию контейнера
COPY . .

# Копируем конфигурационный файл Redis
COPY redis.conf /etc/redis/redis.conf

# Запускаем Redis с конфигурационным файлом, затем приложение
CMD redis-server /etc/redis/redis.conf & python run.py
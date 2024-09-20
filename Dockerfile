FROM python:3.12-slim

# Устанавливаем необходимые пакеты, включая Redis
RUN apt-get update && apt-get install -y redis-server && apt-get clean

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
CMD service redis-server start && python run.py



#FROM python:3.12-slim
##Debian GNU/Linux 10, python без компилятора
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
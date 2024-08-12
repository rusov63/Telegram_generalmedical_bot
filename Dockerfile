FROM python:3.12-slim
#Debian GNU/Linux 10, python без компилятора

# устанавливаем рабочую директорию внутри контейнера.
WORKDIR /app

# Копируем и устанавливаем зависимости Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы из текущей директории в рабочую директорию контейнера
COPY . .

# Команда запуска контейнера
CMD ["python", "run.py"]
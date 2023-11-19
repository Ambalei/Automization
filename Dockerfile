# Используем базовый образ с Python
FROM python:3.8-slim

# Установка необходимых пакетов для поддержки русских символов
RUN yum update && yum -y install locales
RUN locale-gen ru_RU.UTF-8
RUN dpkg-reconfigure locales

# Задаем переменные окружения для правильной локали
ENV LC_ALL ru_RU.UTF-8
ENV LANG ru_RU.UTF-8
ENV LANGUAGE ru_RU.UTF-8

# Устанавливаем зависимости
RUN yum update && yum install -y \
    firefox-esr \
    wget \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем Geckodriver
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz \
    && tar -xzvf geckodriver-v0.30.0-linux64.tar.gz \
    && chmod +x geckodriver \
    && mv geckodriver /usr/local/bin/ \
    && rm geckodriver-v0.30.0-linux64.tar.gz

# Создаем и переключаемся в рабочую директорию
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем тестовый код
COPY . .

# Команда для запуска тестов
CMD ["pytest", "tests"]

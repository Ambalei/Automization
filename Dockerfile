# Используем базовый образ CentOS
FROM centos:latest

# Обновляем пакеты
RUN sudo yum -y update

# Устанавливаем необходимые пакеты
RUN sudo yum -y install epel-release \
    && sudo yum -y install python3 \
    && sudo yum -y install python3-pip \
    && sudo yum -y install wget \
    && sudo yum -y install unzip \
    && sudo yum -y install Xvfb \
    && sudo yum -y install libX11 libXcomposite libXcursor libXdamage libXext libXi libXtst libXrandr libXScrnSaver libXss libXxf86vm libXinerama libpng-devel libXrandr-devel GConf2

# Устанавливаем ChromeDriver
RUN wget https://chromedriver.storage.googleapis.com/94.0.4606.61/chromedriver_linux64.zip \
    && unzip chromedriver_linux64.zip \
    && mv chromedriver /usr/local/bin/chromedriver \
    && chmod +x /usr/local/bin/chromedriver \
    && rm chromedriver_linux64.zip

# Устанавливаем Google Chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm \
    && sudo yum -y localinstall google-chrome-stable_current_x86_64.rpm \
    && rm google-chrome-stable_current_x86_64.rpm

# Копируем зависимости для тестов
COPY requirements.txt /app/requirements.txt

# Устанавливаем зависимости
WORKDIR /app
RUN pip3 install --no-cache-dir -r requirements.txt

# Копируем тестовый код
COPY . /app

# Запускаем тесты
CMD ["python3", "CAFAP/AIS_CAFAP/ais_cafap/py"]

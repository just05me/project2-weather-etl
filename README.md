WeatherETL

License Status

WeatherETL — это ETL-процесс (Extract, Transform, Load) для сбора, обработки и хранения данных о погоде. Проект использует API OpenWeatherMap для получения погоды, pandas для обработки данных и MySQL для хранения. Автоматизация процесса реализована через Apache Airflow, который запускает задачу каждые 10 минут.
Основные возможности

    Сбор данных: Получение текущей погоды (температура, скорость ветра) для указанного города через OpenWeatherMap API.
    Обработка: Преобразование данных в DataFrame с помощью pandas и вывод средней температуры.
    Хранение: Сохранение данных в MySQL базе данных.
    Автоматизация: Планирование задач через Airflow DAG с интервалом в 10 минут.

Технологии

    Язык: Python 3.10+
    Библиотеки:
        requests — для работы с API.
        pandas — для обработки данных.
        mysql-connector-python — для подключения к MySQL.
        apache-airflow — для автоматизации ETL-процесса.
    База данных: MySQL.
    Виртуальное окружение: Используется для изоляции зависимостей.

Структура проекта

    weather_etl.py — основной скрипт с логикой ETL (сбор, обработка, сохранение данных).
    weather_etl_dag.py — файл DAG для Airflow, планирующий выполнение задачи.
    weather_db — база данных MySQL (создаётся автоматически при первом запуске).

Установка

Следуй этим шагам, чтобы настроить и запустить проект:
Требования

    Python 3.10 или выше.
    Установленный MySQL сервер.
    Apache Airflow (настроенный локально или на сервере).
    Виртуальное окружение с зависимостями.

Шаги

    Склонируйте репозиторий:
    bash

git clone https://github.com/username/WeatherETL.git
Замени username на свой GitHub-ник.
Перейдите в директорию проекта:
bash
cd WeatherETL
Создайте и активируйте виртуальное окружение (если ещё не создано):

    Создание:
    bash

python -m venv weatherenv
Активация:

    Windows:
    bash

weatherenv\Scripts\activate
Linux/MacOS:
bash

        source weatherenv/bin/activate

Установите зависимости:
bash
pip install requests pandas mysql-connector-python apache-airflow
Настройте MySQL:

    Убедись, что MySQL работает на localhost с пользователем root и паролем itsmyfirstlinux (или измени параметры в weather_etl.py под свои).
    База данных weather_db будет создана автоматически.

Настройте Airflow:

    Помести weather_etl_dag.py в папку dags/ твоего Airflow (обычно ~/airflow/dags).
    Убедись, что weather_etl.py доступен в той же директории или указан правильный путь в импорте.
    Запусти Airflow:
    bash

        airflow webserver --port 8080
        airflow scheduler
    Настройте API ключ:
        В weather_etl.py используется ключ OpenWeatherMap (bdc7d1928553766d0c06bee6ae6c9dcd). Зарегистрируйся на OpenWeatherMap и замени его на свой, если нужно.

Использование

    Ручной запуск (без Airflow):
    bash

    python weather_etl.py
    Это выполнит ETL-процесс для города "Tashkent" и сохранит данные в MySQL.
    Через Airflow:
        Открой веб-интерфейс Airflow (обычно http://localhost:8080).
        Найди DAG weather_etl_dag и включи его.
        Задача будет запускаться каждые 10 минут автоматически.

Пример вывода

После запуска:
text
Средняя температура: 25.5
Данные сохранены!

Проверь данные в MySQL:
sql
SELECT * FROM weather;
Конфигурация

    Город: Измени переменную city в weather_etl.py на любой другой (например, "Moscow").
    Интервал: Настрой schedule_interval в weather_etl_dag.py (сейчас каждые 10 минут: "*/10 * * * *").

Требования

    Python 3.10+.
    MySQL сервер.
    Airflow 2.x.
    Зависимости: requests, pandas, mysql-connector-python, apache-airflow.

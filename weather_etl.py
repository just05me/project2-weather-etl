import requests
import pandas as pd
import mysql.connector
from datetime import datetime

# Для получения погоды из API
def get_weather_data(city):
    api_key = "APIkey"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if data["cod"] == 200:
        weather = {
            "city": city,
            "temp": data["main"]["temp"],
            "wind": data["wind"]["speed"],
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        return weather
    else:
        return None

# Для обработки данных
def process_data(weather):
    df = pd.DataFrame([weather])
    avg_temp = df["temp"].mean()
    print(f"Средняя температура: {avg_temp}")
    return df

# Для подключения к MySQL
def connect_to_database():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="ur password",
        database="weather_db"
    )
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather (
            id INT AUTO_INCREMENT PRIMARY KEY,
            city VARCHAR(50),
            temp FLOAT,
            wind FLOAT,
            date VARCHAR(50)
        )
    """)
    conn.commit()
    return conn, cursor

# Для сохранения данных в MySQL
def save_to_database(df, cursor, conn):
    for index, row in df.iterrows():
        cursor.execute("""
            INSERT INTO weather (city, temp, wind, date)
            VALUES (%s, %s, %s, %s)
        """, (row["city"], row["temp"], row["wind"], row["date"]))
    conn.commit()


def main():
    city = "Tashkent"  # Можно поменять город
    weather = get_weather_data(city)
    if weather:
        df = process_data(weather)
        conn, cursor = connect_to_database()
        save_to_database(df, cursor, conn)
        conn.close()
        print("Данные сохранены!")
    else:
        print("Не удалось взять погоду!")

if __name__ == "__main__":
    main()

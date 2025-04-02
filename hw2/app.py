import requests
from datetime import datetime
import time

CACHE = {
    "timestamp": None,
    "html": None
}

CACHE_TTL = 900

def app(environ, start_response):
    now = time.time()

    if CACHE["timestamp"] and (now - CACHE["timestamp"]) < CACHE_TTL:
        html = CACHE["html"]
    else:
        url = (
            "https://api.open-meteo.com/v1/forecast"
            "?latitude=55.75&longitude=37.61"
            "&current_weather=true"
            "&timezone=Europe%2FMoscow"
        )

        try:
            r = requests.get(url, timeout=3)
            data = r.json()
            weather = data.get("current_weather", {})
            temperature = weather.get("temperature", "N/A")
            wind = weather.get("windspeed", "N/A")
            weather_time_str = weather.get("time", "")

            if weather_time_str:
                weather_time = datetime.fromisoformat(weather_time_str).strftime("%d.%m.%Y %H:%M")
            else:
                weather_time = "неизвестно"

            title = "Погода в Москве"
            content = f"""
                <p>Температура: {temperature}°C</p>
                <p>Ветер: {wind} км/ч</p>
                <p>Время обновления: {weather_time}</p>
            """
        except Exception as e:
            title = "Ошибка"
            content = f"<p>Не удалось получить данные о погоде.<br>{str(e)}</p>"

        html = f"""
        <html>
            <head><title>{title}</title></head>
            <body>
                <h1>{title}</h1>
                {content}
            </body>
        </html>
        """

        CACHE["timestamp"] = now
        CACHE["html"] = html

    start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
    return [html.encode("utf-8")]

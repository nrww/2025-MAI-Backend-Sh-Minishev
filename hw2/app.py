import requests
from datetime import datetime

def app(environ, start_response):
    url = (
        "https://api.open-meteo.com/v1/forecast"
        "?latitude=55.75&longitude=37.61"
        "&current_weather=true"
        "&timezone=Europe%2FMoscow"
    )

    try:
        r = requests.get(url)
        data = r.json()
        weather = data.get("current_weather", {})
        temperature = weather.get("temperature", "N/A")
        wind = weather.get("windspeed", "N/A")
        time = weather.get("time", "")
        time = datetime.fromisoformat(time).strftime("%d.%m.%Y %H:%M") if time else ""

        title = "Погода в Москве"
        content = f"""
            <p>Температура: {temperature}°C</p>
            <p>Ветер: {wind} км/ч</p>
            <p>Время обновления: {time}</p>
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

    start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
    return [html.encode("utf-8")]

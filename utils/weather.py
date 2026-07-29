import requests

API_KEY = "bc06bb17402bf6a38ac46fab2ae2135d"


def get_weather(city):

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    try:
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()

        else:
            return None

    except Exception as e:
        print("Error:", e)
        return None